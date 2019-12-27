# Crop Tool
A Command Line Tool for cropping images, written in Python.  
Inspired by Adrian Rosebrock's " Capturing mouse click events with Python and OpenCV " tutorial at the following link:  
http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

Modified from the version of Sarvaswa at the following link:
https://github.com/Sarvaswa/Crop-Tool

# Added Features
* Save Crops to file
* Make multiple crops in a single session
* Crop independent of the crop direction
* Backward compatibility (Written in Python 3.5, works in Python 2.7)
* Auto resizing the image to fit the screen
* Use other library to read screen resolution instead of Win32API

# Requirements
* Pyhton (Tested on 2.7 and 3.5)
* OpenCV
* screeninfo

# Usage 
## Crop image
Open Command Line and type the following command (Edit file path)
``` python crop_tool.py ```  

This opens a window displaying the image  
Click on the starting point of the crop, drag the mouse till the end point and release it  
A green rectangle would appear  

Press 'c' to preview the crop  
Press 's' to save the crop to the 'Crops' directory  
Press 'r' to reset the image (removes the green rectangle from the original image)  
Press 'd' to end the cropping session and change to the next image
**NOTE:** Saving can only work after pressing 'c' i.e. after previewing the crop

## Assign text to each image and stored as text file
Open Command Line and type the following command (Edit file path)
``` python write_label.py ``` 

Click to the displayed image in the beginning
Type the content from the keyboard, observe the pressed key on the console
Press 'Enter' to save the label and change to the next image


