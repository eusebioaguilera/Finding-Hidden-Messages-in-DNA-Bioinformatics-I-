__author__ = 'eusebio'

#
# This file implements the approximate kmer search method
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

def approximate_pattern_count(p, d, dis):
    if os.path.isfile(p):
        f = open(p)
        pattern = f.readline().strip()
    else:
        pattern = p

    if os.path.isfile(d):
        f = open(d)
        text = f.readline().strip()
    else:
        text = d

    distance = dis

    idx = []

    for i in range(len(text) - len(pattern) + 1):
        if hamming(text[i:i+len(pattern)], pattern) <= distance:
            idx.append(i)

    return idx


def main(args):
    tested = []
    kmers = []
    max_count = 0

    if os.path.isfile(args.dna):
        f = open(args.dna)
        text = f.readline().strip()
    else:
        text = args.dna

    k = args.k

    distance = args.distance

    for i in range(len(text)-k):
        pattern_ = text[i:i+k]

        testit = True

        # for item in tested:
        #     if hamming(item, pattern_) <= distance:
        #         testit = False
        #         print item, pattern_, "are similar"
        #         break

        if testit:
            tested.append(pattern_)
            #print tested
            count = len(approximate_pattern_count(pattern_, text, distance))

            if count > max_count:
                max_count = count
                kmers = [pattern_]
            elif count == max_count:
                kmers.append(pattern_)

    return kmers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return the approximate search k-mers  in dna with at maximum hamming distance.')
    parser.add_argument('dna', help='DNA text for findind the pattern')
    parser.add_argument('k', help='k size for the k-mers', type=int)
    parser.add_argument('distance', help='Maximum hamming distance', type=int)
    args = parser.parse_args()
    kmers = main(args)

    for item in kmers:
        sys.stdout.write(str(item) + ' ')

    print

    print len(kmers)