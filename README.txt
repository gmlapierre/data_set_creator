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
