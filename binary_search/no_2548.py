"""
    대표 자연수

    1 <= N <= 20,000
    대표 자연수가 두 개 이상일 경우 그 중 제일 작은 것을 출력

    완전탐색
    N이 2만개 => O(n^2) 불가함.

    이진 탐색
    1. 정렬
    2.

    o(n)
    https://magentino.tistory.com/107

"""


# 2분탐색 풀이
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = list(map(int, input().split(' ')))
#
# min_sum = 1_000_000_000
#
# if __name__ == '__main__':
#
#     arr.sort()
#     answer = max(arr)
#
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # 중간값의 차이의 합계산
#         num = arr[mid]
#         temp_sum = 0
#         for e in arr:
#             temp_sum += abs(num - e)
#
#         # 차이의 합이 현재 최소 차이의 합보다 작거나 같다면
#         if temp_sum <= min_sum:
#             # 정답이 될수 있는것 중 작은것
#             answer = min(answer, arr[mid])
#             min_sum = temp_sum
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     print(answer)
