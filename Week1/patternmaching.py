#
# This file implements the PatternCount method
#

import os
import argparse
import sys


def main(args):
  f = open(args.text)
  line = f.readline()
  text = line
  pattern = args.pattern

  my_idx = []

  idx = text.find(pattern)

  while idx != -1:
    my_idx.append(idx)

    idx = text.find(pattern, idx + 1)

  return my_idx

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Complementary method.')
  parser.add_argument(
      'text', help='The text you are obtaining the Complementary')
  parser.add_argument('pattern', help='The pattern you are looking for')
  args = parser.parse_args()
  idxs = main(args)

  for idx in idxs:
    sys.stdout.write(str(idx) + ' ')

  print
