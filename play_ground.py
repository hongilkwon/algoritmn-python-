"""
    play_ground

    ord(문자) => 아스키 코드
    chr(아스키코드) => 문자

    *
    A - 65
    a - 97
    0 - 48
"""

import sys

input = sys.stdin.readline

s = str(input().rstrip())

if __name__ == '__main__':
    print(ord(s))
