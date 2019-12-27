import glob
import cv2

image_path = '/home/tducnguyen/NguyenTran/Project/12_5G/Data/Crop-Tool-master/crops'
label_path = '/home/tducnguyen/NguyenTran/Project/12_5G/Data/Crop-Tool-master/anotation'

list_images = glob.glob(image_path + '/*.png')
# string = str(input())
# print(string)
key_list = {'48': '0', '49': '1', '50': '2', '51': '3', '52': '4', '53': '5', '54': '6', '55': '7', '56': '8', '57': '9',
            '113': 'q', '119': 'w', '101': 'e', '114': 'r', '116': 't', '121': 'y', '117': 'u', '105': 'i', '111': 'o', '112': 'p',
            '97': 'a', '115': 's', '100': 'd', '102': 'f', '103': 'g', '104': 'h', '106': 'j', '107': 'k', '108': 'l',
            '122': 'z', '120': 'x', '99': 'c', '118': 'v', '98': 'b', '110': 'n', '109': 'm'}

for image_path in list_images:
    image = cv2.imread(image_path)
    image_name = image_path.split('/')[-1].split('.')[0]
    label = []
    while True:
        cv2.imshow('Image', image)
        key = cv2.waitKey(0) & 0xFF
        if key != 255:
            if key != 13:
                if str(key) in list(key_list.keys()):  # Enter key
                    # record any key to text file
                    key_str = key_list[str(key)]
                    print(key_str)
                    label.append(key_str)
            else:
                # if press enter, store the label to path
                with open(label_path + '/' + image_name + '.txt', 'w') as lbf:
                    lbf.writelines(label)
                    lbf.close()

                break

