#!/usr/bin/env python3
"""
Author : sbrown10
Date   : 2019-02-11
Purpose: Acts like the cat-n command
"""

import os
import sys


# --------------------------------------------------
def main():
 
 args=sys.argv[1:]

 if len(args) != 1:
  print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
  sys.exit(1)

 file=args[0]
 
 if not os.path.isfile(file):
  print('{} is not a file'.format(file))
  sys.exit(1)

#all_lines=open(file).read().strip().splitlines() 
#i=0

#for line in all_lines:
 #print('{}: {}'.format(i+1, all_lines))
 #break

 with open(file, 'r') as total_lines:
  for k, lines in enumerate(total_lines):
   print(' {}: {}'.format(k+1, lines.strip()))
# --------------------------------------------------
main()
