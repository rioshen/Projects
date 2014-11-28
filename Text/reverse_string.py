#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(seq):
    """Reverse a string and print it out."""

    # string slicing
    print "{0} reverse version 1 is {1}".format(seq, seq[::-1])

    # also create a new string backward
    rev = [seq[i] for i in xrange(len(seq)-1, -1, -1)]
    print "{0} reverse version 2 is {1}".format(seq, ''.join(rev))

if __name__ == '__main__':
    content = raw_input("Input the string here.")
    reverse(content)
