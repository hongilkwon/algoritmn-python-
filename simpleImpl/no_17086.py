"""
    아기상어2(bfs, 시작점이 여러개인..)

    N과 M(2 ≤ N, M ≤ 50)
"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(' '))
#
# board = [list(map(int, input().split(' '))) for _ in range(n)]
# point_shark = []
#
# visited = [[0 for _ in range(m)] for _ in range(n)]
#
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
#
#
# def bfs():
#     q = deque()
#     for p in point_shark:
#         visited[p[0]][p[1]] = 1
#         q.append(p)
#
#     while q:
#         y, x = q.popleft()
#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if (ny < 0 or ny >= n) or (nx < 0 or nx >= m):
#                 continue
#             if visited[ny][nx] >= 1:
#                 continue
#             visited[ny][nx] = visited[y][x] + 1
#             q.append((ny, nx))
#
#
# if __name__ == '__main__':
#     for r in range(n):
#         for c in range(m):
#             if board[r][c] == 1:
#                 point_shark.append((r, c))
#     bfs()
#     answer = 0
#     for r in range(n):
#         for c in range(m):
#             answer = max(answer, visited[r][c])
#     print(answer - 1)