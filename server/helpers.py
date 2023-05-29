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
            The explanation for each target group must not exceed 100 words in length.
            The explanation should be similar to the content in a summary page of a report.
            Each explanation should be accompanied with up to 5 related subtopics of the explanation for each level that would deepen the understanding of Convolutional Neural Networks. For example, if the topic is about linear algebra, it should contain info about diagonalization, eigenvalues etc.
            Note that each level should be provided with its unique list of additional learning materials to cater to its specific needs.

            Resources:
            1. Long term memory management.
            2. GPT-3.5 powered agents for delegation of simple tasks.
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
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({ 
        "topic": topic,
        "role": role
    })
    # Notify the reader that the data was successfully loaded.
    return result

def validate_email_format(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email) is not None

def validate_password_strength(password):
    # Min and max length constraints
    min_length = 8
    max_length = 128
    if len(password) < min_length or len(password) > max_length:
        return False

    # At least one upper case letter check
    if not re.search(r'[A-Z]', password):
        return False

    # At least one lower case letter check
    if not re.search(r'[a-z]', password):
        return False

    # At least one digit check  
    if not re.search(r'\d', password):
        return False

    # At least one special character check
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # No repetitive or sequential characters check
    if re.search(r'(.)\1+', password) or '1234' in password or 'abcd' in password:
        return False

    # No common passwords check
    common_passwords = ["password", "12345678", "qwerty", "admin"]
    if password in common_passwords:
        return False

    # If the password passed all the checks, return True
    return True