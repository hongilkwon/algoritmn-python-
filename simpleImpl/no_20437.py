"""
    문자열 게임2 (hash)



"""

import sys
#
# input = sys.stdin.readline
#
# t = int(input())
#
# for _ in range(t):
#     w = input()
#     k = int(input())
#
#     # 문자열의 각 문자 갯수 세기
#     cnt_dict = {}
#     for c in w:
#         cnt_dict[c] = cnt_dict.get(c, 0) + 1
#
#     idx_dict = {}
#     for i, c in enumerate(w):
#         if cnt_dict[c] < k:
#             continue
#         idx_dict[c] = idx_dict.get(c, []) + [i]
#
#     max_len = 0
#     min_len = len(w)
#
#     for key, v in idx_dict.items():
#         # print(key, v)
#         for i in range(len(v) - (k-1)):
#             length = v[i + k - 1] - v[i] + 1
#             max_len= max(max_len, length)
#             min_len = min(min_len, length)
#
#     if idx_dict:
#         print(min_len, max_len)
#     else:
#         print(-1)
