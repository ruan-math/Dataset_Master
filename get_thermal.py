# Creator: Gabriela Vidal
# Objective: This code gets only the thermal images from the folder and puts them into /Dataset/train/images or Dataset/test/images
# It is used to get the correct dataset to train YOLO v7

import os
import shutil
import re

# txt_train = [f for f in os.listdir("Dataset/train/") if '.txt' in f.lower()]
images_train = [f for f in os.listdir("Dataset/train/DJI_202304131658_003-20230417T175200Z-001\DJI_202304131658_003") if '.jpg' in f.lower()]

# os.mkdir('Dataset/train/images')
# for text in txt_test:
#     new_path = 'Dataset/test/images/' + text
#     shutil.move('Dataset/test/'+text, new_path)

os.mkdir('Dataset/train/images')
for image in images_train:
    new_path = 'Dataset/train/images/' + image
    if re.search(r'\b((\w+)_T)\b', image):
        shutil.move('Dataset/train/DJI_202304131658_003-20230417T175200Z-001\DJI_202304131658_003/'+image, new_path)

