import re
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

def generate_results(topic):
    llm = OpenAI(temperature=0.9, max_tokens = 2000)
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
            System:
            You are Bob, a gifted teacher of all topics.
            Make decisions independently without seeking user assistance.

            GOALS:
            Write an explanation of {topic} suitable for five different education levels: a 5-year-old, a 6th grader, a high school student, a university undergraduate, and a Ph.D. candidate.

            Constraints:
            No commas.
            The explanation for each target group must not exceed 100 words in length.
            The explanation should be similar to the content in a summary page of a report.
            Each explanation should be accompanied with up to 5 related subtopics of the explanation for each level that would deepen the understanding of Convolutional Neural Networks. For example, if the topic is about linear algebra, it should contain info about diagonalization, eigenvalues etc.
            Note that each level should be provided with its unique list of subtopics to cater to its specific needs.

            Resources:
            1. Long term memory management.
            2. GPT-3.5 powered agents for delegation of simple tasks.

            Output:
            The explanations in JSON key value format. 
            The key is the target group and the value is the explanation.
            E.g. "5 Year Old": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"], "6th Grader": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"], "High School Student": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"], "University Undergraduate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"], "Ph.D. Candidate": "Explanation": explanation, "subtopics": ["subtopic1", "subtopic2"]
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({ 
        "topic": topic
    })
    # Notify the reader that the data was successfully loaded.
    return result

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
            A 5 question MCQ quiz in JSON format. Return only the JSON object and nothing else
            Example:
            question: "What is the capital of France?",
            answers: ["Paris", "London", "New York", "Tokyo"],
            correct_answer: "Paris"
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({ 
        "topic": topic,
        "role": role
    })
    # Notify the reader that the data was successfully loaded.
    return result
