import socketio,base64,cv2
import numpy as np

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