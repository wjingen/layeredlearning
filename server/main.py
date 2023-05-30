from flask import Flask
from flask_cors import CORS
from flask import request
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from helpers import generate_results
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from langchain.chains import ConversationChain
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory import ConversationBufferMemory

cred = credentials.Certificate("serviceAccountKey.json")
firebase = firebase_admin.initialize_app(cred, options = {
    "databaseURL": 'databaseURL'
})  
bucket = storage.bucket('default')

OPENAI_API_KEY="OPENAI_API_KEY"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
app = Flask(__name__)
CORS(app, origins = '*', headers = '*')

def remove_text(string):
    start_index = string.find('{')
    
    if start_index == -1:
        return string
    
    return string[start_index:]

def generate_qna(topic, role):
    llm = OpenAI(temperature=0.9, max_tokens = 2000)
    prompt = PromptTemplate(
        input_variables=["topic", "role"],
        template="""
            System:
            You are Bob, a gifted teacher of all topics.
            Make decisions independently without seeking user assistance.

            GOALS:
            Write an 5 question MCQ quiz of {topic} suitable for a {role}.

            Constraints:
            Each MCQ question should have 4 answers.
            The questions should be in the format below:
            Question X: <question>
            Answers: <answer1>, <answer2>, <answer3>, <answer4>
            Correct Answer: <answer>

            Resources:
            1. Long term memory management.
            2. GPT-3.5 powered agents for delegation of simple tasks.

            Output:
            A 5 question MCQ quiz in JSON format.
            This will be an object with 5 keys, each key being a question. 
            For each question, the format should be:
            <question>: [[<answer1>, <answer2>, <answer3>, <answer4>], <correct_answer>]
            Example:
            "What is the capital of France?": [["Paris", "London", "New York", "Tokyo"], "Paris"]
            Finally, the object itself is a value, with the key being the role. In this case, the role is {role}.
            Example:
            {role}: <list of questions>>
            This will then be wrapped as a json object.
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({ 
        "topic": topic,
        "role": role
    })
    # Notify the reader that the data was successfully loaded.
    return remove_text(result)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'Test'

@app.route('/explainer', methods = ['POST'])
def explainer():
    data = request.json
    topic = data['topic']
    ref = db.reference('topic')
    try:
        res = ref.get()[topic]
    except:
        res = generate_results(topic)
        ref.update({
            topic: res
        })
    return remove_text(res)

@app.route('/apply_feedback', methods = ['POST'])
def apply_feedback():
    data = request.json
    try:
        topic, feedback = data['topic'], data['feedback']
    except:
        return 'Please provide a valid topic and feedback'
    ref = db.reference('topic')
    current_output = ref.get()[topic]
    memory = ConversationBufferMemory()
    memory.chat_memory.add_user_message("""
            System:
            You are Bob, a gifted teacher of all topics.
            Make decisions independently without seeking user assistance.

            GOALS:
            Write an explanation of""" + topic + """ suitable for five different education levels: a 5-year-old, a 6th grader, a high school student, a university undergraduate, and a Ph.D. candidate.

            Constraints:
            The explanation for each target group must not exceed 100 words in length.
            The explanation should be similar to the content in a summary page of a report.
            Each explanation should be accompanied with up to 5 related subtopics of the explanation for each level that would deepen the understanding of Convolutional Neural Networks. For example, if the topic is about linear algebra, it should contain info about diagonalization, eigenvalues etc.
            Note that each level should be provided with its unique list of additional learning materials to cater to its specific needs.

            Resources:
            1. Long term memory management.
            2. GPT-3.5 powered agents for delegation of simple tasks.

            Output:
            The explanations in JSON key value format. 
            The key is the target group and the value is the explanation.
            This output should be the same for all 5 age groups. 
            E.g. "5 Year Old": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
            "6th Grader": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
            "High School Student": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
            "University Undergraduate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
            "Ph.D. Candidate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"]
        """)
    memory.chat_memory.add_ai_message(current_output)
    llm = OpenAI(temperature=0.9, max_tokens = 2000)
    conversation = ConversationChain(
        llm=llm, 
        verbose=True, 
        memory=memory
    )
    feedback = feedback.replace('_', ' ').title()
    result = conversation.predict(input=f"""
        I'm having trouble understanding, the current content of  has the feedback: {feedback}. 
        Can you parse the JSON and rephrase the concept of {topic} according to the feedback?
        Your output should be in a similar format as the previous message.
        Output:
        The explanations in JSON key value format. 
        The key is the target group and the value is the explanation.
        This output should be the same for all 5 age groups. 
        E.g. "5 Year Old": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
        "6th Grader": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
        "High School Student": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
        "University Undergraduate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"],
        "Ph.D. Candidate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"]
    """)
    return remove_text(result)

@app.route('/quiz', methods = ['POST'])
def qna():
    data = request.json
    topic, role = data['topic'], data['role']
    ref = db.reference('quizzes')
    try:
        res = ref.get()[topic + '_' + role]
    except:
        res = generate_qna(topic, role)
        ref.update({
            topic + '_' + role: res
        })
    return res

if __name__ == '__main__':
    app.run(debug=True)