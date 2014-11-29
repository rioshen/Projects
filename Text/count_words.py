#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_words(content):
    """Count number of words in raw data."""
    if not content or not isinstance(content, basestring):
        print "0 words in the content"
        return
    print len([word for line in content.split()
                    for word in line.split(' ')])
    words = 0
    for line in content.split():
        words += len(line.split(' '))
    print words

if __name__ == '__main__':
    count_words("Counts the number of individual words in a string. For added \
                 complexity read these strings in from a text file and\
                 generate a summary.")

