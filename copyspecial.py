#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir_list):
  """Given a dirname, returns a list of all its special files."""
  mfull, mname = [], []
  for dir in dir_list:
    for root, dirs, files in os.walk(dir):
      for name in files:
        if re.search("^.*__.+__.*$", name) != None:
          if name in mname: exit("Error: Duplicate file name matches")
          mfull.append(os.path.join(root, name))
          mname.append(name)
  return mfull

def copy_to(paths, dir):
  if not os.path.exists(dir): os.mkdir(dir)
  for file in paths:
    shutil.copy(file, dir)
  
def zip_to(paths, zippath):
  pathstring = " ".join(paths)
  cmd = 'zip -j {} {}'.format(zippath, pathstring)
  print "about to do this:", cmd
  (status, output) = commands.getstatusoutput(cmd)
  print output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  specials = get_special_paths(args)
  
  if todir != '':
    copy_to(specials, todir)
  
  if tozip != '':
    zip_to(specials, tozip)
  
  if todir == '' and tozip == '':
    for file in specials: print file
  
  
if __name__ == "__main__":
  main()
