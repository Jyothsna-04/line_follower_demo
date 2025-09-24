# line_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/line', methods=['POST'])
def line():
    data = request.get_json()
    print("✅ LINE FOLLOWER CMD:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(port=5003)
