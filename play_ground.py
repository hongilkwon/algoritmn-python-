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


"""
    일부 숫자의 이진수 표현에 수정된 한 자리 숫자
    진법! 나눈 몫이 != 0
"""


def convert(num, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, k):
    b_list = list(convert(n, 2))

    if len(b_list) > k:
        b_list[-k] = '0'

    temp = b_list[::-1]
    ret = 0
    for i in range(len(temp)):
        ret += (2 ** i) * int(temp[i])

    return ...


if __name__ == '__main__':
    # solution(0, 4)
    temp = ['1', '2', '3', '4']
    a = ''.join(temp)

    print(a)
