"""
   예산 (이분탐색)

   정해진 총액 이하에서 가능한 한 최대의 총 예산 배정

   모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
   모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
   상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

    3 <= n <= 10_000
    1 <= 예산 <= 100_000
    n <= m <= 1_000_000_000 (10억)

    예시)
    상한액을 잡는 방법.
    1. 완전탐색

    10_000 * 1_000_000_000(10억)
    -> 너무 많은 연산 횟수.

    2. 이진탐색
    상한액 자체는 순차적으로 정렬되어 있다.
    n n+1 n+2 ....  10억 까지..

"""

import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
#
#
# def chk(upper_bound):
#     total = 0
#     for e in arr:
#         total += min(e, upper_bound)
#     return m >= total
#
#
# if __name__ == '__main__':
#
#     left = 0
#     right = max(arr)
#
#     answer = 0
#     while left <= right:
#         mid = int((left + right) / 2)
#         if chk(mid):
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(answer)