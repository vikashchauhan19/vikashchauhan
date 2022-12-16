import cv2

camera = cv2.VideoCapture(0)  # 0,means the first webcamera
while camera.isOpened():
    status, image = camera.read()
    if not status:
        print('Could not read image')
        break

    # do something with the camera 
    cv2.imshow("webcam window",image)
    if cv2.waitKey(1)==27: 
        break
camera.release()
cv2.distroyALLWindows()