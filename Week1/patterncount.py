#
# This file implements the PatternCount method
#

import os
import argparse


def pattern_count(text, pattern):
  count = 0

  for i in range(0, len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
      count += 1

  return count


def main(args):
  text = args.text
  pattern = args.pattern

  print "Pattern is %d times in text" % (pattern_count(text, pattern))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='PatternCount method.')
  parser.add_argument('text', help='The text you are analyzing')
  parser.add_argument('pattern',  help='The pattern you are looking for')

  args = parser.parse_args()
  main(args)
