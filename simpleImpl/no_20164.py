"""
    홀릭 홀릭 호석(재귀 및 구현)

    1 ≤ N ≤ 10^9-1, N 은 자연수
    => 999999999 9개


"""

# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n = input().rstrip()
#
# min_cnt = 1000
# max_cnt = 0
#
#
# def count_odd(s):
#     count = 0
#     for c in s:
#         if int(c) % 2 == 1:
#             count += 1
#     return count
#
#
# def go(num, cnt):
#     global min_cnt, max_cnt
#
#     cnt += count_odd(num)
#
#     if len(num) == 1:
#         min_cnt = min(min_cnt, cnt)
#         max_cnt = max(max_cnt, cnt)
#     elif len(num) == 2:
#         tmp = int(num) // 10 + int(num) % 10
#         go(str(tmp), cnt)
#     else:
#         for e in list(combinations([i for i in range(1, len(num))], 2)):
#             first, second = e
#             tmp = int(num[:first]) + int(num[first:second]) + int(num[second:])
#             go(str(tmp), cnt)
#
#
# if __name__ == '__main__':
#     go(n,0)
#     print(min_cnt, max_cnt)
