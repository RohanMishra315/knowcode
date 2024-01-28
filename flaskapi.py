from flask import Flask, jsonify, request
from dotenv import load_dotenv
from PIL import Image
import os
import google.generativeai as genai
from flask_cors import CORS
load_dotenv()  # loading all the environment

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

app = Flask(__name__)
CORS(app)  

@app.route('/gemini_llm_vision', methods=['GET', 'POST'])
def gemini_llm_vision():
    try:
        if request.method == 'POST':
            data = request.form
            input_text = "Act like you are my nutrionist and you tell me about the food image which I sent you. Tell me about the nutrition in the food. Tell me its pros and cons. Also whether I should consume this or not."
            uploaded_file = request.files.get('image')

            if input_text != "" and uploaded_file is not None:
                response = model.generate_content([input_text, Image.open(uploaded_file)])
            elif uploaded_file is not None:
                response = model.generate_content(Image.open(uploaded_file))
            else:
                return jsonify({"error": "No input provided"}), 400
            print(response.text)
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "Method Not Allowed"}), 405
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port="5001")
    