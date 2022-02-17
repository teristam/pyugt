"""
Demo Flask application to test the operation of Flask with socket.io

Aim is to create a webpage that is constantly updated with random numbers from a background python process.

30th May 2014

===================

Updated 13th April 2018

+ Upgraded code to Python 3
+ Used Python3 SocketIO implementation
+ Updated CDN Javascript and CSS sources

"""




# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import randint
from time import sleep
from threading import Thread, Event
from pyugt import main

__author__ = 'slynn'
textSent = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.data = ''
app.old_data = ''

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()


def emitMessage(app):
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    while not thread_stop_event.isSet():
        if app.data != app.old_data:
            print('Emitting new text')
            socketio.emit('text', {'text': app.data }, namespace='/test')
            socketio.sleep(1)
            app.old_data = app.data


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the text message thread
    if not thread.is_alive():
        print("Starting Thread")
        thread = socketio.start_background_task(emitMessage,app)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    pyugtThread = Thread(target=main, args=(app,))
    pyugtThread.start()
    socketio.run(app)
