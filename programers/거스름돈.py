"""
    거스름돈

    n 원을 줄 때 방법의 경우의 수

    1 <= n <= 100_000
    1 <= 화폐 단위 <= 100

    모든 화폐는 무한하게 있다고 가정
    1_000_000_007 나눈 나머지 리턴

    사고과정.
    화폐의 종류가 여러개다.

    종류가 너무 많다 -> DP

    예시) n = 5

    1 2 3 4 5
    ---------
"""


# MOD = 1_000_000_007
#
# n = 0
# # table[n] => n원을 거슬러주는 방법의 수 저장
# table = []
#
# def solution(_n, money):
#     answer = 0
#     global n, table
#
#     n = _n
#     table = [0 for _ in range(n+1)]
#     table[0] = 1
#
#     for amount in money:
#         for i in range(amount, n+1):
#             table[i] += table[i - amount]
#
#     answer = table[n] % MOD
#     return answer