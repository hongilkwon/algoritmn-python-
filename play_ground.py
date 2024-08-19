"""
 play_ground
"""

import sys
from collections import deque
from functools import cmp_to_key
import heapq


def create_str_set(str):
    list = []
    str = str.lower()

    for i in range(len(str) - 1):
        c1 = str[i]
        c2 = str[i + 1]
        if 97 <= ord(c1) <= 122 and 97 <= ord(c2) <= 122:
            list.append(c1 + c2)
    return list


def separate(s):
    head, number, tail = '', '', ''

    for i, c in enumerate(s):
        if c.isdecimal():
            s = s[i:]
            break
        head += c

    for i, c in enumerate(s):
        if not c.isdecimal():
            s = s[i:]
            break
        number += c

    if s != number:
        tail = s
    else:
        tail = ''
    return head, number, tail


def return_two_result():
    return True, 10


class Shark:
    def __init__(self, num, direction, priority):
        self.num = num
        self.direction = direction
        self.priority = priority


if __name__ == '__main__':
    a = 'a'
    print(a[-1])


