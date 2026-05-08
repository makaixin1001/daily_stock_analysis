from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/futures', methods=['GET'])
def get_futures():
    # 使用东财官方延迟版API（反爬成功率最高）
    url = "https://push2delay.eastmoney.com/api/qt/clist/get"
    params = {
        "np": "1",
        "fltt": "2",
        "invt": "2",
        "fields": "f12,f14,f2,f3,f4,f5,f6,f15,f16,f17,f18,f22,f23",
        "fs": "m:113,m:114,m:115,m:116,m:117,m:118,m:119,m:120,m:121,m:122,m:123,m:124,m:125,m:126,m:127,m:128,m:129,m:130,m:131,m:132,m:133,m:134,m:135,m:136,m:137,m:138,m:139,m:140,m:141,m:142",
        "ut": "bd1d9ddb040897e8b1a2a5c0a5a2f5d4",
    }
    headers = {
        "Host": "push2delay.eastmoney.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "Origin": "https://quote.eastmoney.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
    }
    
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e), "status": "proxy_failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
