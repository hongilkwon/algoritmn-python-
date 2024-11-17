"""
    play_ground


"""

import sys

input = sys.stdin.readline

n = int(input())

if __name__ == '__main__':

    cnt_long = n // 4

    answer = ""
    for _ in range(cnt_long):
        answer += "long "

    answer += "int"
    print(answer)