#!/usr/local/bin/python

import numpy as np
import cv2

cap = cv2.VideoCapture('test.avi')
fcount = 0
ftotal = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

print "total"
print ftotal


while(cap.isOpened() and fcount<=ftotal):
    fcount += 1
    flag, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if (fcount>ftotal):
      break
    else:
      cv2.imwrite('frame'+ str(fcount) + ".jpeg" ,gray)

    print fcount


    cv2.imshow('frame',gray)
    if cv2.waitKey(3) & 0xFF == ord('q'):
              break
cap.release()
cv2.destroyAllWindows()
