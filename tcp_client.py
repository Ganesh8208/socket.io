import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print('Connected to server')
    sio.emit('my_event', {'data': 'Client message'})

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def my_response(data):
    print('Received response:', data)

# Connect to the server
sio.connect('http://localhost:5000')

# Wait for events
sio.wait()
sio.disconnect()