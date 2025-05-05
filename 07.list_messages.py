 
import requests

# OpenAI API URL
api_url = f"https://api.openai.com/v1/threads/{3.スレッドの生成（会話の場を作る）で取得したスレッドID}/messages"

# OpenAI API key
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 実際のAPIキーを指定してください

# ヘッダーの設定
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Beta": "assistants=v2"
}


# GETリクエストを送信
response = requests.get(api_url, headers=headers)

# レスポンスの確認
if response.status_code == 200:
    data = response.json()
    
    # 必要なデータをすべて出力する
    if data.get('data'):
        for message in data['data']:
            # 各メッセージのコンテンツを取得
            content_list = message.get('content', [])
            if content_list:
                value = content_list[0].get('text', {}).get('value', '内容が見つかりません')
                print(f"回答: {value}")
                print(f"--------------------")
            else:
                print("Response structure does not match the expected format.")
    else:
        print("Response structure does not match the expected format.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
