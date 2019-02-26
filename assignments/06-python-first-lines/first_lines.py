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
        'directory', type=str, metavar='DIR', nargs='+', help='Directory File Name')

    parser.add_argument(
        '-w',
        '--width',
        help='integer argument for the width',
        metavar='int',
        type=int,
        default=50)


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


    for file in os.listdir(dirs):
     path = os.path.join(dirs,file)
     line = open(path).readline().rstrip()
     dir_dict[line] = file

    for line, file in sorted(dir_dict.items()):
     lines = len(line)
     files = len(file)
     period = '.'*line_width

    print('{} {} {}'.format(line, period, file))


#-----------------------------------------------
if __name__ == '__main__':
    main()
