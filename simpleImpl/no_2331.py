"""
    반복수열(단순구현)
"""

# import sys
# import math
#
# input = sys.stdin.readline
#
# a, p = map(int, input().split(" "))
#
# temp = set()
# arr = [a]
#
# if __name__ == '__main__':
#
#     while arr[-1] not in temp:
#         temp.add(arr[-1])
#         num = arr[-1]
#         sum = 0
#
#         while num > 0:
#             sum += int(math.pow(num % 10, p))
#             num = num // 10
#
#         arr.append(sum)
#
#     # print(arr)
#     cnt = 0
#     for e in arr:
#         if e != arr[-1]:
#             cnt += 1
#         else:
#             break
#     print(cnt)