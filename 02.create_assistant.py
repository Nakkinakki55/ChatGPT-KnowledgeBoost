import requests
import json

# OpenAI APIのエンドポイントURL
api_url = "https://api.openai.com/v1/assistants"

# OpenAI APIキー
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 適切なAPIキーを指定

# リクエストボディ（JSON形式）
request_body = {
    "instructions": "You are a bot that provides legal information. Tell me the contents of the file you loaded.",
    "name": "secretary",
    "tools": [
        {"type": "code_interpreter"}
    ],
    "model": "gpt-4o",
    "tool_resources": {
        "code_interpreter": {
            "file_ids": [
                # ファイルのアップロード（データを用意して読み込む）で取得したファイルIDを代入
                "file-111111111111", 
                "file-222222222222",
                "file-333333333333",
                "file-444444444444"
            ]
        }
    }
}

# ヘッダー設定
headers = {
    "Content-Type": "application/json",  # JSON形式を指定
    "Authorization": f"Bearer {api_key}",  # APIキーを設定
    "OpenAI-Beta": "assistants=v2"  # OpenAI APIのベータ機能指定
}

# POSTリクエストを送信
response = requests.post(api_url, headers=headers, data=json.dumps(request_body))

# レスポンスの確認
if response.status_code == 200:
    # 成功した場合の処理
    response_content = response.json()
    
    # レスポンスから"id"を抽出して変数に代入
    assistant_id = response_content.get("id", "ID not found")
    
    print("Assistant ID:", assistant_id)
else:
    # エラーが発生した場合の処理
    print(f"エラー: {response.status_code}")
    print(response.text)

