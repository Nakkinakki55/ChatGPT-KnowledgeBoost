import requests

# OpenAI APIのファイルアップロード用URL
api_url = "https://api.openai.com/v1/files"

# OpenAI APIキー
api_key = "{「通常のChatGPT APIを使用する」で取得したAPI}"  # 適切なAPIキーを指定

# アップロードするファイルのパス（4つのファイル: 刑法、民法、商法、日本国憲法）
file_paths = [
    "C:\\Users\\user\\Downloads\\criminal_code_of_japan.html",
    "C:\\Users\\user\\Downloads\\civil_code_of_japan.html",
    "C:\\Users\\user\\Downloads\\commercial_code_of_japan.html",
    "C:\\Users\\user\\Downloads\\japan_constitution_1947.html"
]

# ヘッダーの設定
headers = {
    "Authorization": f"Bearer {api_key}"
}

# 取得したfile_idを格納する配列
file_ids = []

# 各ファイルをアップロード
for file_path in file_paths:
    files = {
        'purpose': (None, 'assistants'),  # ファイルの目的を指定
        'file': (open(file_path, 'rb'))  # ファイルをバイナリモードで開く
    }

    # リクエストを送信
    response = requests.post(api_url, headers=headers, files=files)

    # レスポンスを処理
    if response.status_code == 200:
        # 成功した場合、file_idを配列に追加
        response_content = response.json()
        file_id = response_content.get('id', 'ID not found')
        file_ids.append(file_id)
    else:
        # エラーが発生した場合の処理
        print(f"エラー: {response.status_code} - ファイル: {file_path}")
        print(response.text)

# すべてのfile_idを出力
print("取得したファイルID:")
for file_id in file_ids:
    print(file_id)

