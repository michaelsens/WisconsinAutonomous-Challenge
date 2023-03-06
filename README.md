![answer](https://user-images.githubusercontent.com/33575951/223028478-906836ff-cfeb-4d73-80ef-d81c6f2edc5f.png)
# WisconsinAutonomous-Challenge

Methodology:
I knew I needed to generate two straight lines based on a series of cones in the image. And the best way I knew to accomplish this is with linear algebra based on a series of x and y coordinates. 

So, I needed to use cv2 to accurately identify and transform red cones into a single point.

I realized that the color of the cones were very unique from most of the rest of the image, so I wanted to filter out everything that wasn't distinctly red. In order to do this I used the cv2 inRange function to turn the color image into a binary image, with red colors within a certain range having the value of 255 and any other color having the value of 0. The result image left the cones clearly defined, however there was still a large amount of noise.

I then fed the binary image into the cv2 findContours function which returned the outlines of all of the shapes in the binary images, both cones and noise. 

Then, as the final step in turning each cone into a single x and y coordinate I looped through the contours and computed a center point for each one. This was done using the moments function from cv2 that returned detailed information about the distribution of individual points in the passed contour. I extracted the zeroth and first order x and y moments and used them to calculate the center point of the cone (centroids). During this step I also used the cs2 contourArea functuon to calculate the area of each contour and used that information to help filter out more of the noise based on the approximate size of a cone.

At this stage, all of the image processing work I needed to do with cv2 was completed and all that remained was linear algebra work with numpy and some final data filtering. 

For some reason my code was outputting a large number of centroids with the coordinates 0,0 that obviously weren't correct. I wasn't able to figure out the source of this issue, but filtering them out of the array was simple and this step left me with only the coordinates of the 14 cones.

I split the array of centroids into two different arrays for the left and right half of the screen. I then used numpy to solve a linear equation based on the sequence of points utilizing linalg.lstsq to find a solution that minimizes the sum of the squares of the residuals. This outputted both the intercept and slope of the lines of best fit and I used this information to plot both the lines on the image.

Failures:
For me, there were two stages in solving this problem. The first stage involved gaining an understanding of both the fundemental steps I needed to follow to arrive at the solution along with learning the specific functions and code that would help me accomplish each step of my soltuion. For example, I first approached this problem with the fundemental misconception that I needed to use opencv to identify lines. This approach eventually lead me to an output that drew lines on every edge and contour but failed to identify the signifigance of the lines made by the cones. Despite such failures being so far from the solution, each one taught me new skills that would eventually contribute to me successfully solve the problem such as gaining a preliminary understanding of the contour tracing that would later help me identify the centroids of the cones.

The second stage of solving this problem involved a lot of refining. At this point I had established the fundemental steps I needed to take to solve the problem, along with the general functions I needed to use. However there were still many issues, primarily around noise in the filtered image that were processed as cones and wildly threw off the lines. At this point I needed to analyze the data at each step and either refine the processing or think of unique ways to filter out incorrect data. This long process eventually allowed me to both arrive at a successful soltuion and gain a deeper understanding of some of the functionality of opencv.

Libraries: numpy, cv2
