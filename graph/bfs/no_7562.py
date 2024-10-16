"""
    나이트의 이동(BFS, 최단거리)

    체스판의 한 변의 길이 l(4 ≤ l ≤ 300)

    최소 몇 번만에 이동할 수 있는지,,,
"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# l = 0
# start = None
# end = None
#
# visited = None
#
# dy = [-2, -1, 1, 2, 2, 1, -1, -2]
# dx = [1, 2, 2, 1, -1, -2, -2, -1]
#
#
# def go(s):
#     q = deque()
#     q.append((s, 0))
#     visited[s[0]][s[1]] = 1
#
#     while q:
#         node, cnt = q.popleft()
#
#         if node == end:
#             return cnt
#
#         for i in range(8):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
#
#             if (ny < 0 or ny >= l) or (nx < 0 or nx >= l):
#                 continue
#             if visited[ny][nx] == 1:
#                 continue
#             visited[ny][nx] = 1
#             q.append(((ny, nx), cnt + 1))
#
#     return -1
#
#
# if __name__ == '__main__':
#     for _ in range(tc):
#         l = int(input())
#         start = tuple(map(int, input().split()))
#         end = tuple(map(int, input().split()))
#
#         visited = [[0 for _ in range(l)] for _ in range(l)]
#         ret = go(start)
#         print(ret)