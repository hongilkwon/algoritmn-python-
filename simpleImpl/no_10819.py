"""
    차이를 최대로(완전탐색)

    배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성

    |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
    => 차이의 절대값의 최대

    3 <= n <= 8

"""


# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# def cal(arr):
#     sum = 0
#     for i in range(len(arr)-1):
#         sum += abs(arr[i] - arr[i+1])
#     return sum
#
# if __name__ == '__main__':
#     ret = list(permutations(arr))
#     max_value = 0
#     for e in ret:
#         max_value = max(cal(list(e)), max_value)
#     print(max_value)