#!/usr/bin/env python3
"""
Author : sbrown10
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
          
 Names=sys.argv[1:] 
        
 if len(Names) == 0:
  print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
  sys.exit(1)

 if len(Names) == 1:
  print('Hello to the 1 of you: ' + Names[0] + '!')
  #print('Hello to the 1 of you: {}!' + format(Names))

 elif len(Names) == 2:
  print('Hello to the 2 of you: {}!' .format(' and '.join(Names)))
    
 elif len(Names) > 2:
  num = len(Names)
  print('Hello to the {} of you: {}, and {}!' .format(num, ', ' .join(Names[0:-1]), Names[-1]))
# --------------------------------------------------
main()
