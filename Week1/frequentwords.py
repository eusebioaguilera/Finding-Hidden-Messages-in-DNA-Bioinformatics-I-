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


#
# This funtionc computes the frequent k-mers that are in the text
#


def frequent_words(text, k):
  # Python set that contains the frequent words
  frequent_patterns = set()

  # count contains the counter of the Pattern
  count = [0] * (len(text))

  # This variable contains the maximum value which a pattern is in text
  max_count = -1

  for i in range(len(text) - k + 1):
    pattern = text[i:i + k]
    count[i] = pattern_count(text, pattern)

    if count[i] > max_count:
      max_count = count[i]

  for i in range(len(text) - k + 1):
    if count[i] == max_count:
      frequent_patterns.add(text[i:i + k])

  return frequent_patterns, max_count


def main(args):
  text = args.text
  k = args.k

  k_mers, max_count = frequent_words(text, k)
  print "Frequent %d-mers in text are" % (k), k_mers, "and max_count =", max_count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='PatternCount method.')
  parser.add_argument('text', help='The text you are analyzing')
  parser.add_argument('k', type=int, help='Size for the k-mer')

  args = parser.parse_args()
  main(args)
