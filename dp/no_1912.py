"""
    연속합(dp, idea)

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list()
#
# for i in range(n):
#     arr.append(int(input()))
#
# if __name__ == '__main__':
#     answer = -1000_000_000
#
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#         answer = max(answer, sum)
#         if sum < 0:
#             sum = 0
#     print(answer)


import sys

input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

table = [0 for _ in range(n)]

if __name__ == '__main__':

    table[0] = arr[0]
    for i in range(1, n):
        table[i] = max(table[i - 1] + arr[i], arr[i])

    print(max(table))

