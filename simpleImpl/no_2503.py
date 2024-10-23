"""
    숫자야구

    완전탐색을 떠 올리기 쉽지 않은 문제이다.
    컴퓨터 적인 사고를 해야 풀 수있는 문제.

    123, 123, .... 987
"""


# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# n = int(input())
#
# temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# if __name__ == '__main__':
#     ret = list(permutations(temp, 3))
#     # 전체 경우의 수 509
#     # print(len(ret))
#
#     removed_idx_set = set()
#     for _ in range(n):
#         num, s, b = map(str, input().split(' '))
#
#         for i in range(len(ret)):
#             temp_n = ret[i]
#             temp_s, temp_b = 0, 0
#
#             # 민혁이 말한 숫자가 모든 123, 123, .... 987 마다 s, b 계산
#             for j in range(3):
#                 if num[j] == temp_n[j]:
#                     temp_s += 1
#                 elif num[j] in temp_n:
#                     temp_b += 1
#
#             # s ,b가 동일하지 않다면, 후보가 될수 없다.
#             # print(num, temp_n, temp_s, temp_b)
#             if int(s) != temp_s or int(b) != temp_b:
#                 removed_idx_set.add(i)
#
#     print(len(ret) - len(removed_idx_set))
