"""
    소수
"""

# import sys
#
# input = sys.stdin.readline
#
# prime_num = []
#
# table = [1 for _ in range(1_000_001)]
# table[0] = 0
# table[1] = 0
#
# for i in range(2, 1_000_001):
#     if table[i] == 0:
#         continue
#     for j in range(i * 2, 1_000_001, i):
#         table[j] = 0
#
# for i, v in enumerate(table):
#     if v == 1:
#         prime_num.append(i)
#
#
# def solution(n):
#     answer = 0
#     cnt = 0
#     for i in range(len(prime_num)):
#         if prime_num[i] <= n:
#             cnt += 1
#         else:
#             break
#     answer = cnt
#     return answer


# if __name__ == '__main__':
#     solution(5)
