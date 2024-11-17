"""
    n번쨰 큰수
"""

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
#
# # board = [list(map(int, input().split(' '))) for _ in range(n)]
#
# if __name__ == '__main__':
#     q = []
#
#     for _ in range(n):
#         line = map(int, input().split())
#         for num in line:
#             if len(q) < n:
#                 heapq.heappush(q, num)
#             else:
#                 if q[0] < num:
#                     heapq.heappop(q)
#                     heapq.heappush(q, num)
#     print(q[0])