from utils.ai_response import get_ai_response

def generate_quiz(topic):

    prompt = f'''
    Create 5 MCQ questions with answers from:
    {topic}
    '''

    return get_ai_response(prompt)
