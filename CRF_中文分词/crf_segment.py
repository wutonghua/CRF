#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys

import CRFPP

def crf_segmenter(line, tagger):
    tagger.clear()
    seg_result = ""
    for word in line.strip():
        word = word.strip()
        #print(word)
        if word:
            tagger.add((word))
    tagger.parse()
    size = tagger.size()
    xsize = tagger.xsize()
    for i in range(0, size):
        for j in range(0, xsize):
            char = tagger.x(i, j)
            tag = tagger.y2(i)
            if tag == 'B':
                seg_result = seg_result  +' ' + char
            elif tag == 'M':
                seg_result = seg_result + char
            elif tag == 'E':
                seg_result = seg_result + char + ' '
            else:
                seg_result = seg_result + '  ' + char + ' '
    return seg_result.strip()

