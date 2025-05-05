 
import requests
import json

# OpenAI API URL（スレッドIDとrunのエンドポイント）
api_url = "https://api.openai.com/v1/threads/{3.スレッドの生成（会話の場を作る）で取得したスレッドID}/runs"

# OpenAI API key
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 実際のAPIキーを入れてください

# ヘッダーの設定
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "OpenAI-Beta": "assistants=v2"
}

# リクエストボディ（assistant_idを含む）
data = {
    "assistant_id": "{2.アシスタントの生成（AIを設定する）で取得したアシスタントID}"  # 実際のassistant_idを指定
}

# POSTリクエストを送信
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# レスポンスの確認
if response.status_code == 200:
    response_data = response.json()  # レスポンス内容をJSONとして取得

    # 'id' を取得して run_id に代入
    run_id = response_data.get("id")
    
    if run_id:
        print(f"Run ID: {run_id}")  # 取得したIDを表示
    else:
        print("Run ID not found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
