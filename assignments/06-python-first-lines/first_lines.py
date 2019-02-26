#!/usr/bin/env python3
"""
Author : sbrown10
Date   : 2019-02-19
Purpose: Prints the first line of the contents of each file in a directory along with the source file name
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Prints first line of a given file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'directory',metavar='DIR', nargs='+', help='Directory File Name')

    parser.add_argument(
        '-w',
        '--width',
        help='integer argument for the width',
        metavar='int',
        type=int,
        default=0)


    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
   

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    line_width = args.width
    dirs = args.directory
    
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            die('"{}" is not a directory'.format(dir_name))         

    #file = sys.argv[1]
    for filename in os.listdir(dirs):
     with open(filename,'r') as f:   
      first_line = f.readline()    
      print(first_line)
    
  
#    with open(file) as fh:
 #    lines = fh.readlines()
  #   for line in lines:
   #   print(line, end='')

#-----------------------------------------------
if __name__ == '__main__':
    main()
