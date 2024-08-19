"""
    줄서는 방법(수학)

"""

# import sys
# import math
#
# input = sys.stdin.readline


# def solution(n, k):
#     answer = []
#
#     ret = []
#     # [1, 2, 3, 4, 5....n]
#     nums = [i for i in range(1, n + 1)]
#
#     # nums의 idx를 맞추기 위해서 0번 ... k-1번째
#     k = k-1
#     while n != 0:
#         case = math.factorial(n - 1)
#         idx = k // case
#         print('k=', k, 'idx=', idx, 'nums=', nums)
#         ret.append(nums.pop(idx))
#         k %= case
#         n -= 1
#     print(ret)
#     return answer


# 시간초과
# def solution(n, k):
#     answer = []
#
#     temp = [i for i in range(1, n+1)]
#     ret = list(permutations(temp, len(temp)))
#
#     answer = ret[k-1]
#     # print(answer)
#     return answer


# if __name__ == '__main__':
#     solution(4, 24)
