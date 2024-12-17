from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Webhook route to receive messages
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    data = request.data.decode('utf-8')
    message = f"{data}"
    print('Server received:', message)

    socketio.emit('new_message', {'message': message})

    return "ok", 200


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)
