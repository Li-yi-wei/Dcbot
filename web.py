import os
import threading
from flask import Flask

# 建立一個 Flask 應用
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is a placeholder web server for a Discord bot."

# 啟動 HTTP 服務的函數
def run():
    port = int(os.getenv("PORT", 5000))  # 使用 Render 提供的 PORT 環境變數
    app.run(host="0.0.0.0", port=port)

# 在獨立執行緒中運行 HTTP 服務
threading.Thread(target = run).start()
