from dotenv import load_dotenv
load_dotenv()  # loading all the environment 

import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question, max_lines=100):
    response = model.generate_content(question)
    response_lines = response.text.split('\n')[:max_lines]  # Get the first 5 lines of the response
    # Filter out lines that start with a template or heading
    response_comments = [line for line in response_lines if not line.startswith("Start") and not line.startswith("Increase") and not line.startswith("Eat") and not line.startswith("Incorporate")]

    return '\n'.join(response_comments)



def rs(Pedometer: int,CalorieBurnt: int, WaterCount: int, HeartRate: int, currWgt: int, tgWgt: int, Question: str):
    response = get_gemini_response(f"Act like you are a personal Health trainer for me. Here are my Health stats Pedometer is {Pedometer},Calorie Burnt is {CalorieBurnt}, Water Count is {WaterCount}, Heart Rate is {HeartRate}, Current Weight is {currWgt}, Target Weight is {tgWgt}. My question to you is: {Question}")
    return response


