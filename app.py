from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def chat():
    return render_template('chatroom.html')

@socketio.on('send_message')
def sent_message_event(data):
    app.logger.info(f'message sent {data}')
    socketio.emit('receive_message', data)


if __name__ == '__main__':
    socketio.run(app, debug = True)