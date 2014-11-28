#!/usr/bin/env python
# -*- coding:utf-8 -*-

def ispalindrome(seq):
    """Print out result whether the given string is a palindrome"""
    if not seq:
        print "Empty string is also a palindrome."
        return

    # reversed order string should equal to the original
    if seq == seq[::-1]:
        print "{0} is a palindrome".format(seq)
    else:
        print "{0} is not a palindrome".format(seq)

    # traverse the string using two indexes one from head and other from
    # the end
    palindrome = ' is '
    lo, hi = 0, len(seq)-1
    while lo < hi:
        if seq[lo] != seq[hi]:
            palindrome = False
        else:
            lo, hi = lo+1, hi-1
    if palindrome:
        print "{0} is palindrome"


if __name__ == '__main__':
    ispalindrome("godog")
