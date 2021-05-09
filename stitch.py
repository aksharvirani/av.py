# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png
# python stitch.py --first images/shelf1_left.jpg --second images/shelf1_right.jpg
# images are passed as an argument left to right

# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--https://github.com/aksharvirani/av.py/blob/main/S1.jpg", required=True,
	help="path to the first image")
ap.add_argument("-s", "--https://github.com/aksharvirani/av.py/blob/main/S2.jpg", required=True,
	help="path to the second image")
ap.add_argument("-o", "--https://github.com/aksharvirani/av.py/blob/main/output", required=True,
	help="name of the output image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

#imageA = imutils.resize(imageA, width=500)
#imageB = imutils.resize(imageB, width=500)
print(imageA.shape,"  ",imageB.shape)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.imwrite("Results/"+args["output_file"],result)
cv2.waitKey(0)
