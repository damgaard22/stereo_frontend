import time
import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_cors import CORS



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')


@socketio.on('connect')
def connect():
    send('Connected :)')
    join_room('replay')


@socketio.on('get_replay')
def send_replay():
    f = open('time.txt', 'r')
    replay_time, replay_date = f.read().strip().split(' ')
    print(replay_time, replay_date)
    emit('replay_time', {'replay_time': replay_time, 'replay_date': replay_date})
    f.close()


@socketio.on('disconnect')
def disconnect():
    print('Disconnected :(')
    leave_room('replay')


if __name__ == '__main__':
    print('Hello world')
    socketio.run(app, debug=True)

