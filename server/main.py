from flask import Flask
from flask_cors import CORS
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
CORS(app)

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
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({ 
        "topic": topic,
        "role": role
    })
    # Notify the reader that the data was successfully loaded.
    return result

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'Test'

@app.route('/explainer/<topic>')
def explainer(topic):
    ref = db.reference('topic')
    try:
        res = ref.get()[topic]
    except:
        res = generate_results(topic)
        ref.update({
            topic: res
        })
    return res

@app.route('/apply_feedback/<topic>/<feedback>')
def apply_feedback(topic, feedback):
    ref = db.reference('topic')
    current_output = ref.get()[topic]
    memory = ConversationBufferMemory()
    memory.chat_memory.add_user_message(f"""
            System:
            You are Bob, a gifted teacher of all topics.
            Make decisions independently without seeking user assistance.

            GOALS:
            Write an explanation of {topic} suitable for five different education levels: a 5-year-old, a 6th grader, a high school student, a university undergraduate, and a Ph.D. candidate.

            Constraints:
            The explanation for each target group must not exceed 100 words in length.
            The explanation should be similar to the content in a summary page of a report.
            Each explanation should be accompanied with up to 5 related subtopics of the explanation for each level that would deepen the understanding of Convolutional Neural Networks. For example, if the topic is about linear algebra, it should contain info about diagonalization, eigenvalues etc.
            Note that each level should be provided with its unique list of additional learning materials to cater to its specific needs.

            Resources:
            1. Long term memory management.
            2. GPT-3.5 powered agents for delegation of simple tasks.
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
        I'm having trouble understanding, the current content is {feedback}. Can you rephrase the concept according to the feedback?
        Your output should be in a similar format as the previous message. i.e.
        5 Year Old: <explanation>
        6th Grader: <explanation>
        and so on.
    """)
    return result

@app.route('/quiz/<topic>/<role>')
def qna(topic, role):
    return generate_qna(topic, role)

# @app.route('/get_pdf_text')
# def extract_text_from_pdf():
#     # from a firebase cloud storage bucket,
#     # obtain a pdf file and extract the text
#     # return the text
#     blob = bucket.blob("BT3017_Cheatsheet.pdf")
#     blob.download_to_filename("BT3017_Cheatsheet.pdf")

if __name__ == '__main__':
    app.run(debug=True)
