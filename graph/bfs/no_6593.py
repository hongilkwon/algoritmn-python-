"""
    상범빌딩

    탈출하는 가장 빠른 길

    사고과정.
    3차원 bfs
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# l, r, c = -1, -1, -1
# board = None
# visited = None
#
# dz = [0, 0, 0, 0, 1, -1]
# dy = [-1, 0, 1, 0, 0, 0]
# dx = [0, 1, 0, -1, 0, 0]
#
#
# def go(s):
#     global board, visited
#     q = deque()
#
#     visited[s[0]][s[1]][s[2]] = 1
#     q.append(s)
#
#     while q:
#         node = q.popleft()
#
#         for i in range(6):
#             nz = node[0] + dz[i]
#             ny = node[1] + dy[i]
#             nx = node[2] + dx[i]
#
#             if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
#                 if board[nz][ny][nx] == '#':
#                     continue
#                 if visited[nz][ny][nx] > 0:
#                     continue
#
#                 visited[nz][ny][nx] = visited[node[0]][node[1]][node[2]] + 1
#                 q.append((nz, ny, nx))
#
#
# if __name__ == '__main__':
#
#     while True:
#         l, r, c = map(int, input().split())
#         if l == 0 and r == 0 and c == 0:
#             break
#
#         board = [[['' for _ in range(c)] for _ in range(r)] for _ in range(l)]
#         visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
#
#         for i in range(l):
#             for j in range(r):
#                 board[i][j] = list(input().rstrip())
#             input()
#
#         start = None
#         end = None
#         for i in range(l):
#             for j in range(r):
#                 for k in range(c):
#                     if board[i][j][k] == 'S':
#                         start = (i, j, k)
#                     if board[i][j][k] == 'E':
#                         end = (i, j, k)
#         go(start)
#
#         if visited[end[0]][end[1]][end[2]] == 0:
#             print("Trapped!")
#         else:
#             print("Escaped in", visited[end[0]][end[1]][end[2]]-1, "minute(s).")
