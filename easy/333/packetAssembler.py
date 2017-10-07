#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    lpackets = []
    for i in lines:
        r = re.search('(\d+)\s+(\d+)\s+(\d+)\s+(.+)', i)
        mid = int(r.group(1))
        pid = int(r.group(2))
        ptotal = int(r.group(3))
        text = r.group(4)
        lpackets.append((mid, pid, ptotal, text))
    lpackets.sort()
    for i in lpackets:
        print('{:<7} {:<3} {:<4} {}'.format(i[0], i[1], i[2], i[3]))

