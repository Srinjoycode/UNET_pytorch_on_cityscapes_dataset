"""


Paste this file (prepare_train_mask.py) in "gtFine_trainvaltest/gtFine". 
There are 3 folder in this directory - test, train, val. 
Paste the file inside the folder containing the 3 folders.

In Command Prompt or Terminal : 

            python prepare_train_mask.py


Link for the label: 
            https://www.cityscapes-dataset.com/file-handling/?packageID=1

"""

import os 
import cv2 
import numpy as np 
import glob 

try:
    os.makedirs("train_mask")
except:
    pass

print("It might take a few time. Be patient! Let this program run in background.")


images = glob.glob("train_image/*")
print(len(images))


for image in images:
    if "labelIds" in image:
        img_name = image.split('\\')[-1]
        img = cv2.imread(image)
        img[img==7] = 255
        ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
        sub_name = img_name[:-19]
        print(img_name, "--- DONE")
        cv2.imwrite(f"train_mask/{sub_name}mask.png", thresh)

print(len(glob.glob("train_mask/*")))
print("You masked Images is stored in './train_mask' successfully! \n You may proceed. \n Thank you")
