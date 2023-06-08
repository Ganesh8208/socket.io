import socketio,base64,cv2
import numpy as np

# # Create a Socket.IO server instance
# sio = socketio.Server()

# # Define event handlers
# @sio.event
# def connect(sid, environ):
#     print('Client connected:', sid)

# @sio.event
# def disconnect(sid):
#     print('Client disconnected:', sid)

# @sio.event
# def my_event(sid, data):
#     print('Received data:', data)
#     sio.emit('my_response', {'response': 'Server response'}, room=sid)

# # Create a WSGI app and mount the Socket.IO server on it
# app = socketio.WSGIApp(sio)

# # Run the server
# if __name__ == '__main__':
#     import eventlet
#     eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

image = cv2.imread(filename="D:\images\JhonSeena.jpeg")
_,encoded_image = cv2.imencode(ext='.jpg',img=image)
data = base64.b64encode(s=encoded_image)
print('\n',data,'\n')
dec = base64.b64decode(s=data)
print('\n',dec,'\n')
image_array = np.frombuffer(buffer=dec,dtype=np.uint8)


cv2.namedWindow(winname='Live',flags=cv2.WINDOW_NORMAL)
cv2.imshow(winname='Live',mat=image_array)
cv2.waitKey(delay=0)
cv2.destroyWindow(winname='Live')
