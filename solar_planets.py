import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,"Mercury",(110,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Venus",(200,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Earth",(300,230),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Mars",(400,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Jupiter",(500,230),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"Saturn",(800,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Uranus",(970,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Neptune",(1100,230),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))

cv2.imshow("output",img)

cv2.waitKey(0)
