"""
    double up(정수론, 소인수 분해)

    1 <= n <= 200_000

    가장 많이 등장 하는 수의 가능한 최대 등장 횟수

    사고과정

    수를 하나 골라 2를 곱하는 작업을 수행후 가장 많이 등장한 숫자의 등장 횟수

    배울점
    - 어떤 정수든 소인수 분해후, 2 이외의 동일한 소인수를 보유한다면, 2를 곱하여 만들수 있다
    - 실제로 곱하는것 보단 2로 계속 나눠서 2를 제외한 소인수만 남았을때, 남은 소인수가 동일한 것의 개수를 센다.
"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = list(map(int, input().split()))
#
# if __name__ == '__main__':
#
#     cnt_dict = dict()
#     for i in range(len(arr)):
#         temp = arr[i]
#         while temp % 2 == 0:
#             temp /= 2
#
#         key = int(temp)
#
#         if key in cnt_dict:
#             cnt_dict[key] += 1
#         else:
#             cnt_dict[key] = 1
#
#     max_cnt = 0
#     for _, value in cnt_dict.items():
#         max_cnt = max(max_cnt, value)
#     print(max_cnt)
