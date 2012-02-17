import sys
import datetime
now = datetime.datetime.now()
from shutil import move
import os

def get_filename_from_input(filepath):
    """ Get the new filename from given filepath """
    filepiece = filepath.split("/")[-1]
# Take filenameafter first "-"
    filename = filepiece[filepiece.find("-"):]
    return filename

def get_title_from_dashed(dashed_title):
    title_list = dashed_title[1:].split("-")
    title = " ".join(title_list)
    return title.title()

def get_tag_string_from_list(tag_list):
    tag_string = ""
    tag_string += ", ".join(tag_list)
    full_tag_string = "[" + tag_string + "]"
    return full_tag_string
    
def get_metadata(dashed_title, tag_list):
    title = get_title_from_dashed(dashed_title)
    tag_string = get_tag_string_from_list(tag_list)

    metadata = """---
layout: post
title: {title}
tags: {tags}
---

""".format(title=title, tags=tag_string)

    return metadata

try:
    filepath = sys.argv[1]
except IndexError:
    print "Please choose a file to publish!"
    sys.exit()
filename = get_filename_from_input(filepath)
post_dir = "_posts/"

filepiece = filepath.split("/")[-1]
# Take filenameafter first "-"
filename = filepiece[filepiece.find("-"):]
print filename

date_string = str(now.year) + "-" + str('%02d' % now.month) + "-" + str('%02d' % now.day)

newfilename = date_string + filename + ".markdown"
new_post_path = post_dir + newfilename
print "Attempting to publish", filepath, "-->", new_post_path 
print "      ...      "

# Perform final operations ----------------------------
tag_list = sys.argv[2:]
metadata = get_metadata(filename, tag_list)
try:
    with open(filepath, "r") as old_file:
        old_file_contents = old_file.read()
except IOError:
    print "Unable to open file. Make sure it is a text file, not a directory."
    sys.exit()

all_new_contents = metadata + old_file_contents

try:
    with open(new_post_path, 'w') as f:
        f.write(all_new_contents)
except IOError:
    print "Ensure the _posts/ directory exists!"
    sys.exit()

# delete the draft
os.remove(filepath)

print "File published!"
