'''

This script removes all the uneeded files from the cityscape dataset and keeps only the segment masks
Prepares the data for training
Author-Srinjoy Bhuiya
'''
import os
import glob

val_label = glob.glob("val_image/*")
test_label = glob.glob("test_image/*")
train_label = glob.glob("train_image/*")

print(val_label)
print(test_label)
print(train_label)

train_label_instanceIds = glob.glob("train_image/*instanceIds.png")
train_label_color = glob.glob("train_image/*color.png")

for filePath in train_label_instanceIds:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

for filePath in train_label_color:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

val_label_instanceIds = glob.glob("val_image/*instanceIds.png")
val_label_color = glob.glob("val_image/*color.png")

for filePath in val_label_instanceIds:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

for filePath in val_label_color:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

test_label_instanceIds = glob.glob("test_image/*instanceIds.png")
test_label_color = glob.glob("test_image/*color.png")

for filePath in test_label_instanceIds:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

for filePath in test_label_color:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

val_label = glob.glob("val_image/*")
test_label = glob.glob("test_image/*")
train_label = glob.glob("train_image/*")

print(len(val_label))
print(len(test_label))
print(len(train_label))
