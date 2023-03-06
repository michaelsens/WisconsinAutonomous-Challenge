#Author: Michael Sensale

import numpy as np
import cv2

img = cv2.imread('red.png')

# Filtered out everything but the red pixels in a binary image (a decent amount of noise still remains)
# Also findContours requires a binary image input
thresh = cv2.inRange(img, (0, 0, 168), (100, 100, 255))

# Found the contours of the red cones, used RETR_EXTERNAL to only find the outline of the contours, simplified output 
# with CHAIN_APPROX_SIMPLE
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Want to turn each cone into one point so it is possible to compute lines of best fit for them
centroids = np.zeros((len(contours), 2))
for i, contour in enumerate(contours):
    #Filter out some of the noise by ignoring small contours
    area = cv2.contourArea(contour)
    if area > 100:
        #Getting the distribution of the of the pixles of a specific cone (and a lot of noise that will be filtered out later)
        M = cv2.moments(contour) 
        if M['m00'] > 0: #Don't want to divide by 0
            #Finding the center point by dividing the sum of points in the x (and y) directions by the overall sum of the points
            centroids[i] = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

centroids = centroids[centroids[:,0] > 0] #For some reason there are a ton of centroids at 0,0 so those are filtered out

# Putting the centroids for the two lines of cones in seperate arrays
# Accomplished by filtering by the x coordinate of the centroid being on the left or right half of the image
left_centroids = centroids[centroids[:,0] < img.shape[1] / 2]
right_centroids = centroids[centroids[:,0] >= img.shape[1] / 2]

# Need to use np linear algebra to compute the line of best fit for the left and right generated centroids

x_left = left_centroids[:,0]
y_left = left_centroids[:,1]
#generate a matrix of the x coords and 1's
A_left = np.vstack([x_left, np.ones(len(x_left))]).T 
#Solve for the slope and the y intercept
slope_left, intercept_left = np.linalg.lstsq(A_left, y_left, rcond=None)[0]

x_right = right_centroids[:,0]
y_right = right_centroids[:,1]
#generate a matrix of the y coords and 1's
A = np.vstack([x_right, np.ones(len(x_right))]).T
#Solve for the slope and the y intercept
slope_right, intercept_right = np.linalg.lstsq(A, y_right, rcond=None)[0]

#The y coordinates for the endpoints of each line, both the left and right lines end at the top and the bottom of the screen
y1 = img.shape[0]  
y2 = 0  

#Calculate the x value at the top and bottom of the image based on the slope and intercept
x1 = int((y1 - intercept_left) / slope_left)
x2 = int((y2 - intercept_left) / slope_left)
#Draw the left line on the image
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)

#Calculate the x value at the top and bottom of the image based on the slope and intercept
x1 = int((y1 - intercept_right) / slope_right)
x2 = int((y2 - intercept_right) / slope_right)
#Draw the left right on the image
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)

# Save the modified image
cv2.imwrite('answer.png', img)
