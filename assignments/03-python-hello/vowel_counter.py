#!/usr/bin/env python3
"""
Author : sbrown10
Date   : 2019-01-31
Purpose: Counts the vowel in a given phrase
"""

import sys
import os

def main():


 args = sys.argv[1:]

 if len(args) != 1:
  print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
  sys.exit(1)

 phrase = args[0]
 vowels = 'aeiouAEIOU'
 count = 0

 for letter in phrase:
  if letter in vowels:
   count += 1

 if count == 0:
  print('There are 0 vowels in "{}."'.format(phrase))
 elif count == 1:
  print('There is 1 vowel in "{}."' .format(phrase))
 elif count > 1:
  print('There are {} vowels in "{}."' .format(count, phrase))

main()
