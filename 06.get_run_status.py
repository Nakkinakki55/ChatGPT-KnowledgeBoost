 
import requests

# OpenAI API URL（スレッドIDとランIDを指定）
api_url = f"https://api.openai.com/v1/threads/{3.スレッドの生成（会話の場を作る）で取得したスレッドID}/runs/{5.ランを実行(AIに考えさせる)で取得したランID}"

# OpenAI API key
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 実際のAPIキーを入れてください

# ヘッダーの設定
headers = {
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Beta": "assistants=v2"
}

# GETリクエストを送信
response = requests.get(api_url, headers=headers)

# レスポンスの確認
if response.status_code == 200:
    # statusの値のみを取得して表示
    response_content = response.json()
    status_value = response_content.get("status", "Status not found")
    print(f"Status: {status_value}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
