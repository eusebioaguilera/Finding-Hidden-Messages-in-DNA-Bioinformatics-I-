#
# This file implements the PatternCount method
#

import os
import argparse


def main(args):
  text = args.text

  mytext = ''

  for char in text:
    if char == 'A':
      mytext = 'T' + mytext
    elif char == 'C':
      mytext = 'G' + mytext
    elif char == 'G':
      mytext = 'C' + mytext
    else:
      mytext = 'A' + mytext

  return mytext

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Complementary method.')
  parser.add_argument(
      'text', help='The text you are obtaining the Complementary')
  args = parser.parse_args()
  print main(args)
