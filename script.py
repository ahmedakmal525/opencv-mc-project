import numpy as np
import cv2
import serial 
 
portlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
    for port1 in portlist:     
        try: 
            arduino = serial.Serial(port1,9600,timeout = 1)     
        except: 
            print "Failed to Connect to UART interface." 
capture = cv2.VideoCapture(1)

    while True:
        ret, frame = capture.read()
        output = frame.copy()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(5,5),0)
        gray = cv2.medianBlur(gray,5)     
        gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3.5) 
 
        kernel = np.ones((2.6,2.7),np.uint8) 
        gray = cv2.erode(gray,kernel,iterations=1)
        gray = cv2.dilate(gray,kernel,iterations=1)
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,260,param1=30,param2=65,minRadius=0,maxRadi us=0)
        if circles is not None: 
            circles = np.round(circles[0,:]).astype("int")
            for (x,y,r) in circles: 
                cv2.circle(output,(x,y),r,(0,255,0),4)
                cv2.rectangle(output,(x-5,y-5),(x+5,y+5),(255,0,0),-1) 
    
                arduino.write('Y')             
                arduino.flush()             
                arduino.write('N')             
                arduino.flush() 
        else:      
            arduino.flush() 
            cv2.imshow('Gray-Scale-Image',gray)    
            cv2.imshow('Camera-Frame',output)
   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

arduino.write('N')   
arduino.close()
capture.release()
 
