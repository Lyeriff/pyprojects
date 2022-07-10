import cv2
import numpy as np

rainbow = [(148, 0, 211),(75, 0, 130),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 127, 0), (255, 0 , 0)]

#preprocessing

# img = cv2.imread('mohg.jpg')
# img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
# mask = np.zeros(img.shape[:2],np.uint8)
# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)
# rect = (50,50,450,290)
# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis]
# img[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]

#test_test

img = cv2.imread("test.jpg")
img = cv2.resize(img, (0, 0), fx = 0.3, fy = 0.3)
img[np.where((img==[0,0,0]).all(axis=2))] = [54, 57, 63]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = np.chararray(gray.shape)
blank_image = np.zeros((10,10,3), np.uint8)
print(blank_image.shape)
colours = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
font = cv2.FONT_HERSHEY_SIMPLEX
for (x,y), pixel in np.ndenumerate(gray):
   res[x][y] = colours[pixel//4]
out_array  =[]
output = ""
# for gray2 in gray:
#    output = ""
#    for dark in gray2:
#       output += colours[dark // 4] * 2
#    out_array.append(output)
# point = 0
# point2 = 0
# for i in range(gray.shape[1]):
#    try:
#       cv2.putText(blank_image, out_array[point], (0,point2), font, 0.3, (0,0,255), 2, cv2.LINE_AA)
#    except:
#       break
#    point+=1
#    point2+=10
# cv2.imwrite('out.jpg', blank_image)
# # with open("output.txt", mode="w") as f:
# #     f.write(output)

for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colours[dark // 4] * 2

with open("output.txt", mode="w") as f:
    f.write(output)