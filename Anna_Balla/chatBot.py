# API url
# https://aimlapi.com/app/keys

import requests

def chatbot(query):
    api_key = '04f459fbf2bf453e9d08899ef'
    url = 'https://api.aimlapi.com/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": query}
        ],
        "max_tokens": 512,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return "Sorry, something went wrong with the chat service."
    except Exception as err:
        print(f"An error occurred: {err}")
        return "Sorry, something went wrong."

