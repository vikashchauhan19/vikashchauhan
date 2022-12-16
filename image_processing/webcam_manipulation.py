import cv2

camera = cv2.VideoCapture(0)  # 0,means the first webcamera
while camera.isOpened():
    status, image = camera.read()
    if not status:
        print('Could not read image')
        break
    h,w,_= image.shape # underscore(_) means garbage value,many values
    image_bigger = cv2.resize(image,(1.5*w,1.5*h))
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    cv2.imshow("webcam window", image)
    cv2.imshow("webcam window 2", image_bw)
    # do something with the camera 
    #cv2.imshow("webcam window",image_bigger)
    if cv2.waitKey(1)==27: # 27 means ESC TO STOP
        break
camera.release()
cv2.distroyALLWindows()