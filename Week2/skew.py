#
# This file implements the skew method
#

import os
import argparse
import sys



def main(args):

    if os.path.isfile(args.dna):
        f = open(args.dna)
        text = f.readline().strip()
    else:
        text = args.dna

    mytext = ''
    myids = []

    counter = 0
    min_counter = counter

    for i in range(len(text)):
        if text[i] == 'C':
            counter -= 1
        elif text[i] == 'G':
            counter += 1

        if counter == min_counter:
            myids.append(i+1)
        elif counter < min_counter:
            myids = [i+1]
            min_counter = counter


    return myids




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return the all the integers that minimize the skew.')
    parser.add_argument('dna', help='The DNA text you are using to skew')
    args = parser.parse_args()
    myids = main(args)

    for i in myids:
        sys.stdout.write(str(i) + ' ')

    print