import socketio,base64,cv2
import numpy as np

# Create a Socket.IO server instance
sio = socketio.Server()

# Define event handlers
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

@sio.event
def my_event(sid, data):
    image = cv2.imread(filename="D:\images\JhonSeena.jpeg")
    _,encoded_image = cv2.imencode(ext='.jpg',img=image)
    dec = base64.b64encode(s=encoded_image)
    print('Received data:', data)
    sio.emit('my_response', {'response': dec}, room=sid)

# Create a WSGI app and mount the Socket.IO server on it
app = socketio.WSGIApp(sio)

# Run the server
if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

