# photo_organiser
##Problem to solve: 
It often happened that we have many photos which are scattered everywhere, can be duplicated and consume a huge disk space. A random number is given to a photo file name and we may forget where and when the photo is made. It will be desiable to organise these photos.

##Solutions
1. For each photo, get the metadata, in form of EXIF
2. From the metadata, extract address where the phot is made, and the date/time
3. Rename the photo use the combination of address and date/time
4. There are folders named by year. The renamed photo will be put into the corresponnding folder based on the year it is made.

##Benefits:
The photos will not be duplicated, since the renamed photos are identical using photo name as address + time. 

##Libraries used:
*piexif
*geopy
*shutil
