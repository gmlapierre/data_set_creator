import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from configparser import ConfigParser
import json

config = ConfigParser()
config.read(r'./app.conf')


def get_immediate_subdirectories(path_directory, excludes=False, names_only=False):
    if excludes:
        tmp = [name for name in os.listdir(path_directory)
               if os.path.isdir(os.path.join(path_directory, name)) and name not in excludes]
        if names_only:
            return tmp
        else:
            return [path_directory + '\\' + e for e in tmp]
    else:
        tmp = [name for name in os.listdir(path_directory)
               if os.path.isdir(os.path.join(path_directory, name))]
        if names_only:
            return tmp
        else:
            return [path_directory + '\\' + e for e in tmp]


def get_images_path(path_directory_images, extensions, names_only=False):
    tmp = [f for f in listdir(path_directory_images)
           if isfile(join(path_directory_images, f)) and f.endswith(extensions)]
    if len(tmp) == 0:
        print('no files found')
    if names_only:
        return tmp
    else:
        return [path_directory_images + '\\' + e for e in tmp]


def create_directories(path_list):
    for path in path_list:
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print('Folder already exists', path)


def copy_images(dict_images_paths, path_target, config):
    # Give a target path
    # Create an Image folder
    try:
        os.mkdir(path_target)  # will create the Images directory
    except:
        print('Folder already exists')
    # Create the folders

    list_class_path = []
    # Copy the images to the respective folder
    # Assumes the folders were already created
    for key in dict_images_paths:
        list_class_path.append(path_target + '\\' + key)
    create_directories(list_class_path)

    # extract filename from image paths (list)
    # build folder path (class_list)
    x_ = 0
    i = 0
    for key in dict_images_paths:
        for y in dict_images_paths[key]:
            if os.path.exists(list_class_path[x_] + '\\' + os.path.basename(y)):
                i += 1
                copyfile(y, list_class_path[x_] + '\\' + '(' + str(i) + ')' + os.path.basename(y))
            else:
                copyfile(y, list_class_path[x_] + '\\' + os.path.basename(y))
        x_ += 1


PATH_BASE_IMAGES = config['PATHS']['PATH_BASE_IMAGES']

gpath_parent_image_directories = get_immediate_subdirectories(PATH_BASE_IMAGES, config['IGNORE']['FOLDERS'])

gpath_parent_image_directories_names = get_immediate_subdirectories(PATH_BASE_IMAGES, config['IGNORE']['FOLDERS'])

class_names = get_immediate_subdirectories(PATH_BASE_IMAGES, excludes=config['IGNORE']['FOLDERS'], names_only=True)

# build list of sub directories
subdirectories = get_immediate_subdirectories(PATH_BASE_IMAGES, excludes=config['IGNORE']['FOLDERS'])


# for each sub directory
x = 0

classes_and_paths = {}
for subdirectory in subdirectories:
    classes_and_paths[class_names[x]] = []
    for sub in get_immediate_subdirectories(subdirectory, excludes=config['IGNORE']['FOLDERS']):
        paths = get_images_path(sub, tuple(json.loads(config['IMAGE_TYPES']['EXTENSIONS'])))
        for path in paths:
            classes_and_paths[class_names[x]].append(path)
    x += 1

copy_images(classes_and_paths, config['PATHS']['PATH_TARGET_FOLDER'], config)
