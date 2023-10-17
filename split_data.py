# Creator: Gabriela Vidal
# Objective: This code gets the dataset and split it into train, test and val
# To use it, just change the 'main_path' and 'split_folder', 

import splitfolders
import shutil
import os

main_path = "Guararema_e_Arthur/Forth_test/"   # Path to the folder that will be splited
split_folder = "Geral/"                         # Folder that will be splited

path_image = main_path + split_folder + "class1"
path_label = main_path + split_folder + "class2"

output_image = main_path + split_folder + "output"
output_label = main_path + split_folder + "outputlabels"

# Create folder 'class1' and 'class2'
if not os.path.exists(path_image):
    os.mkdir(path_image)

if not os.path.exists(path_label):
    os.mkdir(path_label)

# Move folder 'image' to 'class1' and 'label' to 'class2'
if os.path.exists(path_image.replace('class1', 'images')):
    shutil.move(path_image.replace('class1', 'images'), path_image)

if os.path.exists(path_label.replace('class2', 'labels')):
    shutil.move(path_label.replace('class2', 'labels'), path_label)

# Train: 70%    Val: 20%    Test: 10%s
splitfolders.ratio(path_image, output=output_image, seed=1337, ratio=(0.7, 0.2, 0.1))
splitfolders.ratio(path_label, output=output_label, seed=1337, ratio=(0.7, 0.2, 0.1))

# Move folders to the correct place
# First: remove folders 'class1' and 'class2'
if os.path.exists(path_image):
    shutil.rmtree(path_image)

if os.path.exists(path_label):
    shutil.rmtree(path_label)

# Second: list all directories in the current folder:
dirlistImg = [item for item in os.listdir(output_image) if os.path.isdir(os.path.join(output_image, item))]
dirlistLabel = [item for item in os.listdir(output_label) if os.path.isdir(os.path.join(output_label, item))]
for folder in dirlistImg:
    print(folder)

print()
for folder in dirlistLabel:
    print(folder)

# Third: create the folder "Dataset" and put train, test and val into it
if not os.path.exists(path_image.replace('class1', 'Dataset')):
    os.mkdir(path_image.replace('class1', 'Dataset'))

# Forth: Move all files listed to correct path
for folder in dirlistImg:
    shutil.move(os.path.join(output_image, folder), path_image.replace('class1', 'Dataset')) # Go to the directorie before class1
    # Moves folder inside the current folder (which name is 'labels') to inside the current folder in path label
    print("Arquivo de origem: "+"{}".format(os.path.join(output_label, folder)+"/labels"))
    print("Arquivo de destino: "+"{}".format(os.path.join(path_label.replace('class2', '/'), folder)))
    shutil.move((os.path.join(output_label, folder)+"/labels"), os.path.join(path_label.replace('class2', '/Dataset'), folder))

# Fifth: remove folders 'output' and 'outputlabels'
if os.path.exists(output_image):
    shutil.rmtree(output_image)

if os.path.exists(output_label):
    shutil.rmtree(output_label)

