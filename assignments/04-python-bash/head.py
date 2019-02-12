#!/usr/bin/env python3
"""
Author : sbrown10
Date   : 2019-02-11
Purpose: Works as the head command
"""

import os
import sys


# --------------------------------------------------
def main():

 args = sys.argv[1:]

 if len(args) == 0 :
  print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
  sys.exit(1)

 file = args[0]
  
 if not os.path.isfile(file):
  print('{} is not a file'.format(file))
  sys.exit(1)
 
 if len(args) < 2:
  num_lines = 3
 
 elif len(args) < 3:
  if int(args[1]) < 1:
   print('lines ({}) must be a postive number'.format(args[1]))
   sys.exit(1)
 num_lines =int(args[1])
 
 with open(file, 'r') as all_lines:
  for i, line in enumerate(all_lines,1):
   print(line, end='')
   if i == num_lines:
    break
#-----------------------------------------------
main()
