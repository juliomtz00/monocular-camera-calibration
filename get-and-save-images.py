"""get-and-save-images.py"""

# Import standard libraries
import cv2 
import numpy as np
import textwrap
import argparse
import os 

# Parse user's arguments
parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\Add documentation'''))
parser.add_argument("--camera_id", 
                    type=int, 
                    default=0,
                    help="Device ID. Default value: 0")
parser.add_argument("--path_to_saved_images",
                    type=str,
                    default='captured-images',
                    help='Folder where the captured images will be stored')
parser.add_argument("--base_name",
					type=str,
					default='calibration-image',
					help='Base name used to save the captured images, e.g., calibration-image-0001.png, etc.')
args = parser.parse_args()

# Create a VideoCapture object
video_capture = cv2.VideoCapture(args.camera_id)

# Check if the folder exists, if not, it is created
folder_exist = os.path.exists(args.path_to_saved_images)
if not folder_exist:

   # Create a new directory because it does not exist
   os.makedirs(args.path_to_saved_images)
   print("A new directory to save the captured images has been created!")

# Create a new window for visualisation purposess
cv2.namedWindow("Current frame", cv2.WINDOW_NORMAL)

# Main loop to save images
i = 0
while(video_capture.isOpened()):

	# Retrieve the current frame
   ret, img = video_capture.read()

   # If the current frame cannot be captured...
   if not ret:
      print("Frame missed!")		    

   # If so, it is then visualised
   cv2.imshow("Current frame", img)

   # Wait for the user to press a key
   cha = cv2.waitKey(10)

    # If 'q' is pressed, the program finishes
   if  cha & 0xFF == ord('q'):
      break

   # If 's' is pressed, the current frame is saved in the specified folder
   elif cha & 0xFF == ord('s'):
      path_and_image_name = args.path_to_saved_images+'calibration-image'+"-"+str(f"{i:04d}.png")
      print('Captured image saved in: ' + path_and_image_name)
      cv2.imwrite(path_and_image_name, img)
      i += 1

# Destroy the 'videoCapture' object
video_capture.release()

# Destroy all windows
cv2.destroyAllWindows()

print("Program finished!")
