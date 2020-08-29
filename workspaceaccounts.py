import os, shutil
from os.path import expanduser

workspaces_folder = expanduser("~") + "/Library/Application Support/Amazon Web Services/Amazon WorkSpaces/"

print("Which workspace would you like to open?")

i = 1

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

for file in os.scandir(folder_to_use):
    #os.remove(home + "/Library/Application Support/Amazon Web Services/Amazon WorkSpaces/" + file.name)
    shutil.copyfile(folder_to_use + "/" + file.name, workspaces_folder + file.name)

os.system("open -a /Applications/WorkSpaces.app")
