from flask import Flask, request
import os

app = Flask(__name__)
FLAG = "flag{simple_web_100}"

@app.route('/')
def home():
    return "Merhaba! Bu bir Web challenge. IP, User-Agent gibi bilgilerini dikkatle incele :)"

@app.route('/flag')
def flag():
    # Basit bir kontrol ile sadece User-Agent 'CTFPlayer' ise flag ver
    if request.headers.get("User-Agent") == "CTFPlayer":
        return FLAG
    return "Flag bulamadınız. İpucu: User-Agent değiştirin!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
