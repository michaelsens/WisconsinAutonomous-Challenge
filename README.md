![answer](https://user-images.githubusercontent.com/33575951/223028478-906836ff-cfeb-4d73-80ef-d81c6f2edc5f.png)
# WisconsinAutonomous-Challenge

Methodology:
I knew I needed to generate two straight lines based on a series of cones in the image. And the best way I knew to accomplish this is with simple linear algebra based on a series of x and y coordinates. 

So, I needed to use cv2 to accurately identify and transform red cones into a single point.

I realized that the cones color of the cones were very unique from most of the rest of the image, so I wanted to filter out everything that wasnt distinctly red. In order to do this I used the cv2 inRange function to turn the color image into a binary image, with red colors within a certain range having the value of 255 and any other color having the value of 0. The result image left the cones clearly defined, howver there was still a large amount of noise.

I then fed the binary image into the cv2 findContours function which gave returned the outlines of all of the shapes in the binary images, both cones and noise. 

Libraries: numpy, cv2
