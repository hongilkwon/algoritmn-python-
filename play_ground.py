"""
    play_ground
"""

import sys

input = sys.stdin.readline

s = input().rstrip()
n = int(input())

if __name__ == '__main__':
    print(s[n-1])
