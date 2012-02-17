import sys
import datetime
now = datetime.datetime.now()
from shutil import move

filepath = sys.argv[1]
post_dir = "_posts/"

fileparts = filepath.split("/")[-1]
filename_list  = fileparts .split("-")
filename = ""
# Ignore first part of filename, eg. 03-[filename]
for file_segment in filename_list[1:]:
    filename += file_segment

datestring = str(now.year) + "-" + str('%02d' % now.month) + "-" + str('%02d' % now.day) + "-"

newfilename = datestring + filename
new_post_path = post_dir + newfilename
print "Publishing", filepath, "-->", new_post_path 

move(filepath, new_post_path)
print "File published!"
