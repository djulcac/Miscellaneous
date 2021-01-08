from flask import Flask, render_template, session, copy_current_request_context, request
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock


async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

clients = 0

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect', namespace='/test')
def test_connect():
    global clients
    clients += 1
    print('client connected', clients, request.sid)

@socketio.on('my_event', namespace='/test')
def test_message(message):
    emit('my_response', {'data': message['data']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    emit('my_response', {'data': message['data']}, broadcast=True)


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        global clients
        clients -= 1
        disconnect()

    emit('my_response', {'data': 'Disconnected!'}, callback=can_disconnect)

if __name__ == '__main__':
    socketio.run(app, debug=True)