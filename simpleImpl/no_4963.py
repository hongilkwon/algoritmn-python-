"""
    섬의 개수(BFS, DFS)

    한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로
    대각 방향연결
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# visited = []
#
# # 대각선 포함
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
#
#
# def bfs(start):
#     q = deque()
#     visited[start[0]][start[1]] = 1
#     q.append(start)
#     while q:
#         node = q.popleft()
#
#         for i in range(8):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
#
#             if (ny < 0 or ny >= h) or (nx < 0 or nx >= w):
#                 continue
#             if board[ny][nx] == 0:
#                 continue
#             if visited[ny][nx] == 1:
#                 continue
#
#             visited[ny][nx] = 1
#             q.append((ny, nx))
#
# if __name__ == '__main__':
#     while True:
#         w, h = map(int, input().split())
#         if w == 0 and h == 0:
#             break
#
#         board = [list(map(int, input().split())) for _ in range(h)]
#
#         visited = [[0 for _ in range(w)] for _ in range(h)]
#
#         cnt = 0
#         for r in range(h):
#             for c in range(w):
#                 if visited[r][c] == 0 and board[r][c] == 1:
#                     bfs((r, c))
#                     cnt += 1
#         print(cnt)
#         # for e in visited:
#         #     print(*e)
#         # print()

