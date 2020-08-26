#import os module
import os

#Creates new folder in specified directory
def new_folder(): 
    folder_name = input('Enter a folder name: ')
    directory = input ('Enter a file location: ')
    path = os.path.join(directory, folder_name)

    os.mkdir(path)
    print("Folder '%s' created: " % folder_name)


new_folder()