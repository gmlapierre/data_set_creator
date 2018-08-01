This script will copy Images files from a google drive repository on a filesystem (folder synced with google drive)
to a local filesystem

We assume the following file structure as an input (specified in the config file):

Images/
-Bananas/
--bananes 2018-07-25/
---1.jpg
---2.jpeg
---etc
--bananes plantain 2018-07-26/
---1.jpg
---etc
-Apples/
--pommes 2018-07-27/
---1.jpg
---etc

The files will be copied to a folder specified at a path (specified in the config files):

Images/
-Bananas/
--1.jpg
--2.jpeg
--(1)1.jpg
--(2)2.jpeg
--etc
-Apples/
--1.jpg
--2.jpeg
--(1)1.jpg
--(2)2.jpeg

This script can be used as command line tool or can be used with a config file (app.conf)
located at the root of the project. If no arguments are specified, the app.conf file will be parsed

usage: main.py [-h] [-s SOURCE] [-t TARGET]

Transform 2 level folder directories of images to 1 level

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        path of the source directory
  -t TARGET, --target TARGET
                        path of the target directory



ToDo: Add description feature to count the number of classes, number of images per class etc