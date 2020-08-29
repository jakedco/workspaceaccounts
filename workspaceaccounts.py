import os, shutil
from os.path import expanduser

workspaces_folder = expanduser("~") + "/Library/Application Support/Amazon Web Services/Amazon WorkSpaces/"

print("Which workspace would you like to open?")

i = 1

# printing all the folders to the screen for decision making
for folder in os.scandir("./"):
    if folder.is_dir():
        print(" (" + str(i) + ") " + folder.name)
        i = i + 1

user_choice = input("You may enter in the number option you would like to open.\n")

i = 1

for folder in os.scandir("./"):
    if folder.is_dir():
        if str(user_choice) == str(i):
            folder_to_use = folder.name
            break;
        i = i + 1

# moving the configuration files over.
for file in os.scandir(folder_to_use):
    shutil.copyfile(folder_to_use + "/" + file.name, workspaces_folder + file.name)

os.system("open -a /Applications/WorkSpaces.app")
