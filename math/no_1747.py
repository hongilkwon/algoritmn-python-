"""
    소수 & 팰린드롭

    어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때,
    N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수

    사고과정 100만 이하의 소수를 모두 다 구한다.

"""


# import sys
# import math
#
# input = sys.stdin.readline
#
# n = int(input())
#
# # 시간초과
# # def is_prime(num):
# #     if num == 1:
# #         return False
# #
# #     flag = True
# #     for i in range(2, int(math.sqrt(num) + 1)):
# #         if (num % i) == 0:
# #             flag = False
# #     return flag
#
# primes = []
#
#
# def eratos():
#     table = [1 for _ in range(1_100_000)]
#     table[0] = 0
#     table[1] = 0
#
#     for i in range(2, len(table)):
#         if table[i] == 0:
#             continue
#         for j in range(i * 2, len(table), i):
#             table[j] = 0
#
#     for num, chk in enumerate(table):
#         if chk == 1:
#             primes.append(num)
#
#
# def is_palindrome(num):
#     str1 = str(num)
#     str2 = str1[::-1]
#     if str1 == str2:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     eratos()
#     # print(primes)
#     for num in primes:
#         if num >= n and is_palindrome(num):
#             print(num)
#             break