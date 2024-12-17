from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    data = request.data.decode('utf-8')
    message = f"{data}"
    print('Server received:', message)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
