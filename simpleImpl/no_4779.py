"""
    칸토어 집합()
"""

import sys

input = sys.stdin.readline

ret = ''

def go(n):
    if n == 0:
        return '-'

    return go(n - 1) + ' ' * (3 ** (n - 1)) + go(n - 1)

while True:
    try:
        n = int(input())
        print(go(n))
    except:
        break


