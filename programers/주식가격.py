"""
    주식가격

    1 <= prices <= 10_000
    2 <= prices길이 <= 100_000

    사고과정.

    그냥 이중반복문 돌리면됨.
    문제가 이상하게 해석될수도 있음....
    별로 좋지 않은 문제임...
"""


# def solution(prices):
#     answer = []
#
#     time = []
#     for i in range(len(prices)):
#         sec = 0
#         price = prices[i]
#         for j in range(i + 1, len(prices)):
#             sec += 1
#             if price > prices[j]:
#                 break
#
#         time.append(sec)
#
#     answer = time
#     return answer