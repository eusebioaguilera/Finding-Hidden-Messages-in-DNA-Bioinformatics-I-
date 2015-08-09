__author__ = 'eusebio'


#
# This file implements the approximate search method
#

import os
import argparse
import sys



def hamming(text1, text2):

    counter = 0

    for i in range(len(text1)):
        if text1[i] != text2[i]:
            counter += 1

    return  counter

def main(args):
    if os.path.isfile(args.pattern):
        f = open(args.dna1)
        pattern = f.readline().strip()
    else:
        pattern = args.pattern

    if os.path.isfile(args.dna):
        f = open(args.dna)
        text = f.readline().strip()
    else:
        text = args.dna

    distance = args.distance

    idx = []

    for i in range(len(text) - len(pattern) + 1):
        if hamming(text[i:i+len(pattern)], pattern) <= distance:
            idx.append(i)

    return idx


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return the approximate search indexes of pattern in dna with at maximum hamming distance.')
    parser.add_argument('pattern', help='Pattern to compare')
    parser.add_argument('dna', help='DNA text for findind the pattern')
    parser.add_argument('distance', help='Maximum hamming distance', type=int)
    args = parser.parse_args()
    idx = main(args)

    for i in idx:
        sys.stdout.write(str(i) + ' ')

    print