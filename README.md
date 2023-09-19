# monocular-camera-calibration

Please become familiar with a calibration process applied to a monocular camera to estimate its intrinsic and extrinsic calibration parameters. These parameters will then be saved in a calibration file to correct the radial and tangential distortion in future images captured by the same camera.

## Materials
•	A personal computer.
•	A chessboard calibration board - download the calibration panel
•	A monocular camera.
•	Internet connectivity, as you may need to install Python libraries.
•	Python ≥ 3.10 using the following libraries: OpenCV, NumPy, ArgParse, glob, and textwrap.
•	Visual Studio Code.

## Methodology
An image folder, containing around 30-40 images from the camera that wants to be calibrated, can be generated through the get-and-save-images.py document. This folder shows several positions of an office with a chessboard at the center, allowing for the correct centering of the used camera. It can be seen in the images that the camera is not correctly calibrated as many pictures are distorted mainly at the corners, or at the points further away from the center. Nevertheless, this distortion can be corrected by the following process

The camera calibration software, developed in Python, estimates the intrinsic camera parameters such as the focal length, principal point (center of the image), and the distortion lens (radial and tangential distortions). After obtaining these parameters, the image distortion can be compensated, which can be seen in the following images.

Within the Python code, the points inside the chessboard are defined and searched for, which then allows to save them on a matrix per pixel and see if there is any curvature that shouldn’t be there on the lines, resulting in the correction of the images by changing the input images with the parameters obtained.
The goal of the project is to replicate the previously shown image distortion with the help of the provided images by following the next steps:
1.	Download the calibration image dataset into your host computer and save it in a folder named cal-images.
2.	Download this Python script and name it camera-calibration.py; it will be used together with the calibration image dataset to find the intrinsic and extrinsic parameters of the GoPro Hero 3+ camera that captured the calibration images.
3.	Run the camera-calibration.py script as follows:  $ python camera-calibration.py --path_to_calibration_images cal-images/ --path_to_distorted_images cal-images/  --path_to_undistorted_images undistorted-images/ make sure the folder undistorted-images exists before running the above command. this list continues until the image corner detection process reaches the image GOPR3109.JPG. Having the intrinsic camera calibration parameters we can then compensate for the image distortion. this list continues until the calibration process corrects the image GOPR3109.JPG. Good on you, guys! - You have just completed a camera calibration process.
4.	Go to the folder named undistorted-images and make sure the calibration images have been saved and have been corrected. Provide a sample set of undistorted images in your technical report. 
5.	Although not included in this Python script, it should be able to save the camera matrix and the lens distortion parameters into a TXT file named calibration-parameters.txt. Thus, write a function that performs this task and call that function right after the camera calibration total error is reported. Use the argparse library to allow the user to specify this directory from the Linux terminal using the flag --path_to_calibration_file. 
