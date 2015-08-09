__author__ = 'eusebio'

#
# This file implements the Hamming method
#

import os
import argparse
import sys



def main(args):

    if os.path.isfile(args.dna1):
        f = open(args.dna1)
        text1 = f.readline().strip()
    else:
        text1 = args.dna1

    if os.path.isfile(args.dna2):
        f = open(args.dna2)
        text2 = f.readline().strip()
    else:
        text2 = args.dna2

    counter = 0

    for i in range(len(text1)):
        if text1[i] != text2[i]:
            counter += 1

    return  counter




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return the hamming distance between two dna strings.')
    parser.add_argument('dna1', help='First DNA text to compare')
    parser.add_argument('dna2', help='Second DNA text to compare')
    args = parser.parse_args()
    counter = main(args)

    print counter