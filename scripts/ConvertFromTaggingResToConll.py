# Copyright (c) 2013-2014 Lingpeng Kong
# All Rights Reserved.
#
# This file is part of TweeboParser 1.0.
#
# TweeboParser 1.0 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TweeboParser 1.0 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with TweeboParser 1.0.  If not, see <http://www.gnu.org/licenses/>.
#
# (2021-05-24: Modified by Jenny Chim for Python 3)
# /usr/bin/python

import argparse
import sys
import io

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')

A = parser.parse_args()


def read_corpus(filename):
    corpus = []
    sentence = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            corpus.append(sentence)
            sentence = []
            continue
        else:
            line = line.strip()
            cline = line.split(u"\t")
            sentence.append(cline)
    return corpus

def print_sentence(sentence, outputf):
    for line in sentence:
        s = ""                  
        for field in line:
            s += field + "\t"
        s = s.strip() + "\n"
        outputf.write(s)
    outputf.write("\n")
    return

def convert_sentence(sen):
    new_sen = []
    ind = 1
    for line in sen:
        word = line[0]
        tag = line[1]
        new_line = [str(ind), word, '_', tag, tag, '_', '0', '_',  '_',   '_']
        new_sen.append(new_line)
        ind += 1
    return new_sen 

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='UTF-8', line_buffering=True)   #Ref: https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef#codecs
    corpus = read_corpus(A.inputf)

    conll_format_corpus = []
    for sen in corpus:
        conll_format_corpus.append(convert_sentence(sen))

    for sen in conll_format_corpus:
        print_sentence(sen, sys.stdout)

