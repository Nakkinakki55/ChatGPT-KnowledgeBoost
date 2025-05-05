 
import requests
import json

# API URL for OpenAI chat completion
api_url = "https://api.openai.com/v1/chat/completions"

# API key for authentication
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 適切なAPIキーを指定

# Request body
request_body = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "日本で一番高い山を教えて"}
    ],
    "temperature": 0
}

# Headers for the request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Sending the POST request
response = requests.post(api_url, headers=headers, data=json.dumps(request_body))

# Processing the response
if response.status_code == 200:
    response_content = response.json()
    answer = response_content['choices'][0]['message']['content']
    print(answer)  # Display the response content
else:
    # Handle errors
    print(f"Error: {response.status_code}")
    print(response.text)
