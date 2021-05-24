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

# Author: Swabha Swayamdipta, Lingpeng Kong
#
# (2021-05-24: Modified by Jenny Chim for Python 3)
# /usr/bin/python

import viterbi, sys

def print_line_withmodification(cline, tag):
    s = ""
    for i in range(0,13):
        s += (cline[i] + "\t")
    s += tag
    print(s)


def main(testfile, featsfile):
    labelset = ['0', '1', '*']

    feats = set([])
    sents = []
    tagseqs = []
    postagseqs = []
    vecs1 = []
    vecs2 = []
    
    contents = []

    sent = []
    tags = []
    postags = []
    vec1 = []
    vec2 = []

    content = []

    with open(testfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                if sent:
                    sents.append(sent)
                    tagseqs.append(tags)
                    postagseqs.append(postags)
                    vecs1.append(vec1)
                    vecs2.append(vec2)
                    contents.append(content)

                    sent = []
                    tags = []
                    postags = []
                    vec1 = []
                    vec2 = []
                    content = []
            else:
                cline = line.split("\t")
                word = cline[1].strip()
                tag = '1'
                pos = cline[3].strip()
                v1 = cline[10].strip()
                v2 = cline[11].strip()
                sent.append(word.strip())
                tags.append(tag.strip())
                postags.append(pos.strip())
                vec1.append(v1.strip())
                vec2.append(v2.strip())
                content.append(cline)

    weights = {}
    feats = open(featsfile, 'r')


    while True:
        line = feats.readline()
        if not line:
            break
        line = line.strip()
        f, wt = line.split(' ')
        weights[f] = float(wt)
    feats.close()

    acc = 0.0
    tot = 0
        
    for i in range(len(sents)):
        sent = sents[i]
        postags = postagseqs[i]
        vec1 = vecs1[i]
        vec2 = vecs2[i]
        
        tags, f = viterbi.execute(sent, labelset, postags, vec1, vec2, weights) 

        for j in range(len(tags)):
            print_line_withmodification(contents[i][j],tags[j])
            if tags[j] == tagseqs[i][j]:
                acc += 1
        print()
        tot += len(tags)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

