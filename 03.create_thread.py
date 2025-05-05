import requests
import json

# OpenAI API URL
api_url = "https://api.openai.com/v1/threads"

# OpenAI API key
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 実際のAPIキーを入れてください

# ヘッダーの設定
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Beta": "assistants=v2"
}

# リクエストボディ（空のJSONデータを送信）
data = {}

# POSTリクエストを送信
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# レスポンスの確認
if response.status_code == 200:
    response_data = response.json()  # レスポンス内容をJSONとして取得
    
    # 'id' を取得して thread_id に代入
    thread_id = response_data.get("id")
    if thread_id:
        print(f"Thread ID: {thread_id}")  # 取得したIDを表示
    else:
        print("Thread ID not found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
