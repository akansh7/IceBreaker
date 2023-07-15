from flask import Flask, request, jsonify
from goose3 import Goose
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Function to generate a chat response from ChatGPT
def generate_chat_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

@app.route('/extract_description', methods=['POST'])
def extract_description():
    url = request.json['url']

    # Use Goose to extract the description from the provided URL
    g = Goose()
    article = g.extract(url=url)
    description = article.meta_description

    # Generate ice breaker prompt using ChatGPT
    prompt = f"Based on this company description = '{description}', generate a compliment I can use in my outreach. Praise them for something based on the statement I provided. We will be targeting CEO or the CMO. Start with 'Love how you guys...', And make sure you end the sentence with exactly this phrase '...and I think SARAL might help you discover new influencers fast to spread the word about this to even more consumers on Instagram.'"
    ice_breaker = generate_chat_response(prompt)

    return jsonify({'description': description, 'ice_breaker': ice_breaker})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
