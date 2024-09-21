import cv2
import time


cam = cv2.VideoCapture(1) # the number is the camera index, if you have only one camera, it should be 0
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _, frame = cam.read() # _ is a dummy variable, it is not used
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert the frame to HSV

    h, w, _ = frame.shape # get the height and width of the frame

    #center pixel x and y values
    cx = int(w/2) 
    cy = int(h/2) 

    center = hsv_frame[cy,cx] 
    hue = center[0] 
    sat = center[1]
    val = center[2]

    color = ""

    if val <= 50 and sat <= 180: color = "preto" #black
    elif val >= 200 and sat <= 50: color = "branco" #white
    elif hue <= 5: color = "vermelho" #red
    elif hue <= 22: color = "laranja" #orange
    elif hue <= 35: color = "amarelo" #yellow
    elif hue <= 78: color = "verde" #green
    elif hue <= 140: color = "azul" #blue
    elif hue <= 170: color = "roxo" #purple
    elif 10 <= hue < 20 and 100 <= sat < 255 and 50 <= val < 200: color = "castanho" #brown
    else: color = "vermelho" #red
    
    print(f"{color}: {center}") #used for debugging

    #display the color name on the frame with its respective color
    pixelbgr = frame[cy,cx] 
    b,g,r = int(pixelbgr[0]), int(pixelbgr[1]), int(pixelbgr[2])
    cv2.putText(frame, color, (10,50), 1, 1, (b,g,r), 2)

    cv2.circle(frame, (cx,cy), 4, (255,255,255), 3)
    
    cv2.imshow('frame', frame)

    #time.sleep(0.5) -> used for slowing down the frame rate, useful for debugging
    key = cv2.waitKey(1) 

    if key == 27: break

cam.release() 
cv2.destroyAllWindows()
