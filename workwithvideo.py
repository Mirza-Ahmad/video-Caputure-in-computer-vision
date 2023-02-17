import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
 ret, Frame=cap.read()
 img_gary=cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
 out.write(img_gary)
 cv2.imshow('webcam', Frame)
 print(ret)
 if cv2.waitKey(1) & 0xFF==ord('x'):
  break
out.release()
cv2.destroyAllWindows()