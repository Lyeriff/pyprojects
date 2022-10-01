import cv2
import numpy as np

rainbow = [(148, 0, 211),(75, 0, 130),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 127, 0), (255, 0 , 0)]

img = cv2.imread("test.jpg")
img = cv2.resize(img, (0, 0), fx = 0.2, fy = 0.2)

img[np.where((img==[0,0,0]).all(axis=2))] = [54, 57, 63]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = np.chararray(gray.shape)

blank_image = np.zeros((10,10,3), np.uint8)
# print(blank_image.shape)
colours = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
font = cv2.FONT_HERSHEY_SIMPLEX
for (x,y), pixel in np.ndenumerate(gray):
   res[x][y] = colours[pixel//4]
out_array  =[]
output = ""


for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colours[dark // 4] * 2

with open("output.txt", mode="w") as f:
    f.write(output)