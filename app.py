from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the One Thousand and One Nights Web App!"


@app.route('/generate', methods=['POST'])
def generate():
    # Get emojis and theme from the POST request
    data = request.get_json()
    emojis = data.get('emojis')
    theme = data.get('theme')

    # Prepare prompt
    prompt = f"Create a story with these emojis: {emojis} and the theme: {theme}"

    try:
        # Use OpenAI's ChatCompletion API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or another GPT-3.5 version model
            messages=[{"role": "user", "content": prompt}]
        )

        # Get the story from the response
        story = response['choices'][0]['message']['content']

        # Return the story as JSON response
        return jsonify({'story': story})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
