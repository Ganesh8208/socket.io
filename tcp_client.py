import socketio,base64,cv2
import numpy as np

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
    # print('Received response:', data['response'])
    print('Received response:')

    dec = base64.b64decode(s=data['response'])
    # print('\n',dec,'\n')
    image_array = np.frombuffer(buffer=dec,dtype=np.uint8)

    cv2.namedWindow(winname='Live',flags=cv2.WINDOW_NORMAL)
    cv2.imshow(winname='Live',mat=image_array)
    cv2.waitKey(delay=0)
    cv2.destroyWindow(winname='Live')


# Connect to the server
sio.connect('http://localhost:5000')

# Wait for events
sio.wait()
sio.disconnect()