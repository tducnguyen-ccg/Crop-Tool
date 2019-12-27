# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:17:18 2017

@author: Sarvaswa
"""
## CROP TOOL

## Import for backward compatibility
from __future__ import print_function
from __future__ import division

import cv2
from screeninfo import get_monitors
import glob

## Initialize the list of reference points and boolean indicating
## whether cropping is being performed or not
refPt = []
is_cropping = False

def click_and_crop(event, x, y, flags, param):
    
    # grab references to the global variables
    global refPt, is_cropping
    
    # If left mouse button was pressed, record starting points of the crop
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
        is_cropping = True
    
    # If left mouse button was released, record end points of the crop and
    # create a rectangle around the ROI
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        is_cropping = False

        refPt.sort()
        if refPt[0][1] > refPt[1][1]:
            pt1 = (refPt[0][0], refPt[1][1])
            pt2 = (refPt[1][0], refPt[0][1])
            refPt = [pt1, pt2]
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow('Image', image)

# Path to images folder
images_path = '/home/tducnguyen/NguyenTran/Project/12_5G/Data/car_long'

print('Starting Crop Tool ...')
list_files = glob.glob(images_path + '/*.jpg')
for image_path in list_files:
    image = cv2.imread(image_path)
    clone = image.copy()
    image_name = image_path.split('/')[-1].split('.')[0]

    ## Resize image if bigger than screen resolution
    # Choose your monitor index
    main_monitor = get_monitors()[0]
    screen_width, screen_height = main_monitor.width, main_monitor.height
    img_height, img_width = image[:,:,0].shape
    factor = 1
    if (img_width > screen_width) or (img_height > screen_height):
        widthDiff = img_width - screen_width
        heightDiff = img_height - screen_height
        if widthDiff > heightDiff:
            print('Original image is wider than the screen, resizing ...')
            factor = screen_width/img_width
            image = cv2.resize(image, (int(img_width*factor), int(img_height*factor)),
                                interpolation = cv2.INTER_LANCZOS4)
        else:
            print('Original image is taller than the screen, resizing ...')
            factor = screen_height/img_height
            image = cv2.resizes(image, (int(img_width*factor), int(img_height*factor)),
                                interpolation=cv2.INTER_LANCZOS4)

    clone_resized = image.copy()

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', click_and_crop)

    # Keep looping until 'c' is pressed
    while True:
        cv2.imshow('Image', image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            image = clone_resized.copy()
        elif key == ord('c'):
            if len(refPt) == 2:
                refPt = [(int(pt[0]/factor), int(pt[1]/factor)) for pt in refPt]
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.imshow('ROI', roi)
                key1 = cv2.waitKey(0)
                cv2.destroyWindow('ROI')
                if key1 == ord('s'):
                    crops_path = 'crops/'
                    # numFiles = len([fname for fname in os.listdir(crops_path) if fname.endswith('.png')])
                    # new_filename = str(numFiles + 1) + '.png'
                    new_filename = image_name + '.png'
                    cv2.imwrite(crops_path + new_filename, roi)
                    print('Cropped Image saved to: ', crops_path + new_filename)
            else:
                print('Draw a rectangle across the cropping region first.')
        elif key == ord('d'):
            cv2.destroyAllWindows()
            break

