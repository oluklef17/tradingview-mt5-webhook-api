from flask import Flask, request, jsonify
from threading import Lock

app = Flask(__name__)

# Cache to store the message and lock for thread safety
message_cache = {"message": None}
cache_lock = Lock()

# Webhook route to receive messages
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    data = request.data.decode('utf-8')
    message = f"{data}"
    print('Server received:', message)

    # Save the message to the cache (overwrites previous messages)
    with cache_lock:
        message_cache["message"] = message

    return "Message received and cached", 200

# Retrieve the message (only once)
@app.route('/retrieve', methods=['GET'])
def retrieve_message():
    with cache_lock:
        if message_cache["message"]:
            # Retrieve and delete the message
            retrieved_message = message_cache.pop("message")
            return jsonify({"message": retrieved_message}), 200
        else:
            return jsonify({"error": "No message available"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
