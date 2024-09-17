"""
    다리 만들기(BFS)

    한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다

     1< n <= 100

     사고과정.

     1. 각 섬을 분류한다.
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# new_board = [[0 for _ in range(n)] for _ in range(n)]
# visited = [[0 for _ in range(n)] for _ in range(n)]
#
#
# def make_new_board(start, num):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     new_board[start[0]][start[1]] = num
#
#     while q:
#         node = q.popleft()
#
#         for i in range(4):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
#             if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                 continue
#             if board[ny][nx] == 0:
#                 continue
#             if visited[ny][nx] == 1:
#                 continue
#
#             visited[ny][nx] = 1
#             new_board[ny][nx] = num
#             q.append((ny, nx))
#
#
#
#
# def cal_length(color):
#     q = deque()
#     dist = [[-1 for _ in range(n)] for _ in range(n)]
#     # 시작점 여러개 넣어주기
#     for i in range(n):
#         for j in range(n):
#             if new_board[i][j] == color:
#                 q.append((i, j))
#                 dist[i][j] = 0
#
#     while q:
#         y, x = q.popleft()
#
#         if new_board[y][x] > 0 and new_board[y][x] != color:
#             # for e in dist:
#             #     print(*e)
#             # print()
#             return dist[y][x]
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                 continue
#             if dist[ny][nx] >= 0:
#                 continue
#             dist[ny][nx] = dist[y][x] + 1
#             q.append((ny, nx))
#
#     return sys.maxsize
#
# if __name__ == '__main__':
#
#     color = 1
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1 and visited[i][j] == 0:
#                 make_new_board((i, j), color)
#                 color += 1
#
#     # for e in new_board:
#     #     print(*e)
#     # print()
#
#     min_length = sys.maxsize
#     for c in range(1, color):
#         min_length = min(min_length, cal_length(c))
#     print(min_length-1)