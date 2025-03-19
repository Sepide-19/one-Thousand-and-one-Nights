import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# OpenAI API Key
openai.api_key = 'your-openai-api-key-here'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    emojis = request.form.get('emojis')
    theme = request.form.get('theme')

    # Estefadeh az OpenAI baray generate kardan story
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a story based on these emojis: {emojis} and the theme: {theme}.",
        max_tokens=150
    )
    story = response.choices[0].text.strip()
    return render_template('index.html', story=story)


if __name__ == '__main__':
    app.run(debug=True)
