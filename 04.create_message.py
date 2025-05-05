 
import requests
import json

# OpenAI API URL（スレッドIDを含む）
api_url = "https://api.openai.com/v1/threads/{3.スレッドの生成（会話の場を作る）で取得したスレッドID}/messages"

# OpenAI API key
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 実際のAPIキーを入れてください

# ヘッダーの設定
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Beta": "assistants=v2"
}

# リクエストボディ（メッセージの内容）
data = {
    "role": "user",
    "content": "日本国憲法に定められている基本的人権の概要を書いて"
}

# POSTリクエストを送信
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# レスポンスの確認
if response.status_code == 200:
    print("Message sent successfully!")
    print(response.json())  # レスポンス内容を表示
else:
    print(f"Error: {response.status_code}")
    print(response.text)
