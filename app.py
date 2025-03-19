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
import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import shutil

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Create a folder to save stories and images
if not os.path.exists('stories'):
    os.makedirs('stories')
if not os.path.exists('images'):
    os.makedirs('images')

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

        # Save the story to a file
        story_filename = f"stories/{secure_filename(emojis + '_story.txt')}"
        with open(story_filename, 'w') as story_file:
            story_file.write(story)

        # For simplicity, let's assume an image file is uploaded (for example purposes)
        # Here you can save the image with the filename

        # Simulate saving an image from URL (for now we are skipping actual image generation)
        image_filename = f"images/{secure_filename(emojis + '_image.png')}"
        shutil.copy("default_image.png", image_filename)  # Placeholder, replace with image logic

        # Return the story and image as JSON response
        return jsonify({'story': story, 'image': image_filename})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
