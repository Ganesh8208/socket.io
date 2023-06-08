import socketio,base64,cv2
import numpy as np


                                                                            ########## Video sorce code#################
cap = cv2.VideoCapture()
print(f'Height of video :- {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}\nWidth of video :- {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}\nFps :- {cap.get(cv2.CAP_PROP_FPS)}')
while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        _,encoded_image = cv2.imencode(ext='.jpg',img=frame)
        if _ == True:
            data = base64.b64encode(s=encoded_image)
            dec = base64.b64decode(s=data)
            image_array = np.frombuffer(buffer=dec,dtype=np.uint8)
            cv2.namedWindow(winname='Live',flags=cv2.WINDOW_NORMAL)
            cv2.imshow(winname='Live',mat=image_array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    else:
        break

cap.release()
cv2.destroyWindow(winname='Live')