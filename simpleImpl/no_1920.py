"""
    수 찾기(이진탐색)

    N개의 자연수들에서
    M번 있는지 없는지 확읺해야됨.

    자연수 N(1 ≤ N ≤ 100,000)
    M(1 ≤ M ≤ 100,000)

    10만 => 정렬가능,

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# num_list = list(map(int, input().split(' ')))
# num_list.sort()
#
# m = int(input())
# x_list = list(map(int, input().split(' ')))
#
#
# def binary_search(target):
#     left = 0
#     right = len(num_list)-1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if num_list[mid] == target:
#             return True
#         elif num_list[mid] > target:
#             right = mid - 1
#         elif num_list[mid] < target:
#             left = mid + 1
#     return False
#
#
# if __name__ == '__main__':
#     for x in x_list:
#         if binary_search(x):
#             print(1)
#         else:
#             print(0)
