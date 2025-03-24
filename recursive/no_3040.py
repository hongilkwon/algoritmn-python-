"""
    백설 공주와 일곱 난쟁이(재귀, 조합)

    1. 내장함수,

    2. 재귀로 구현,
"""

import sys
from itertools import combinations
from math import radians

input = sys.stdin.readline

num_list = list()
for _ in range(9):
    num = int(input())
    num_list.append(num)

# 내장함수 이용
# ret_list = list(combinations(range(0, len(num_list)), 2))
#
# if __name__ == '__main__':
#
#     for ret in ret_list:
#         if sum(num_list) - (num_list[ret[0]] + num_list[ret[1]]) == 100:
#             for idx in range(len(num_list)):
#                 if idx not in [ret[0], ret[1]]:
#                     print(num_list[idx])
#             break

# 재귀함수 이용.
# ret = list()
#
# def combi(n, r, s):
#     if r == len(ret):
#         s = 0
#         for idx in ret:
#             s += num_list[idx]
#         if s == 100:
#             for idx in ret:
#                 print(num_list[idx])
#         return
#
#     for i in range(s, n):
#         ret.append(i)
#         combi(n, r, i+1)
#         ret.pop()
#
# if __name__ == '__main__':
#     combi(9, 7, 0)