from dotenv import load_dotenv
load_dotenv()  # loading all the environment 

import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question, max_lines=5):
    response = model.generate_content(question)
    response_lines = response.text.split('\n')[:max_lines]  # Get the first 5 lines of the response
    # Filter out lines that start with a template or heading
    response_comments = [line for line in response_lines if not line.startswith("Start") and not line.startswith("Increase") and not line.startswith("Eat") and not line.startswith("Incorporate")]

    return '\n'.join(response_comments)



def response():
    response = get_gemini_response("What is the capital of India?")
    print(response)

