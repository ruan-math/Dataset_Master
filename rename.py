# Creator: Gabriela Vidal
# Objective: This code gets the dataset and change the names of the images and labels to avoid name problems
# It is used to get the correct dataset to train YOLO v7

import os
import shutil

images = [f for f in os.listdir("Dataset/028/images") if '.jpg' in f.lower()]
labels = [f for f in os.listdir("Dataset/028/labels") if '.txt' in f.lower()]

if not os.path.exists('Dataset/images'):
    os.mkdir('Dataset/images')
if not os.path.exists('Dataset/labels'):
    os.mkdir('Dataset/labels')

for image in images:
    prev_path = 'Dataset/028/images/' + image
    new_path = 'Dataset/images/' + '028_' + image

    shutil.move(prev_path, new_path)

for label in labels:
    prev_path = 'Dataset/028/labels/' + label
    new_path = 'Dataset/labels/' + '028_' + label

    shutil.move(prev_path, new_path)


images = [f for f in os.listdir("Dataset/029/images") if '.jpg' in f.lower()]
labels = [f for f in os.listdir("Dataset/029/label") if '.txt' in f.lower()]

for image in images:
    prev_path = 'Dataset/029/images/' + image
    new_path = 'Dataset/images/' + '029_' + image

    shutil.move(prev_path, new_path)

for label in labels:
    prev_path = 'Dataset/029/label/' + label
    new_path = 'Dataset/labels/' + '029_' + label

    shutil.move(prev_path, new_path)