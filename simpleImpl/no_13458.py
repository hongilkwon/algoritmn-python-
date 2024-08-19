"""
    시험감독(단순구현)
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# b, c = map(int, input().split())
#
# if __name__ == '__main__':
#
#     totalCnt = 0
#     for i in range(len(arr)):
#         cnt = 0
#         if arr[i] - b <= 0:
#             cnt += 1
#         else:
#             temp = arr[i] - b
#             cnt += 1
#             if (temp % c) == 0:
#                 cnt += int((temp / c))
#             else:
#                 cnt += int((temp / c)) + 1
#
#         totalCnt += cnt
#
#     print(totalCnt)
