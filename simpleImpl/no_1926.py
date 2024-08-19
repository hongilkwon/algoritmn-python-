"""
    그림(bfs, dfs)

    그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력

"""


# import sys
# sys.setrecursionlimit(10**9)
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# board = [list(input().split()) for _ in range(n)]
#
# visited = [[0 for _ in range(m)] for _ in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def dfs(node):
#     ret = 1
#     for i in range(4):
#         ny = node[0] + dy[i]
#         nx = node[1] + dx[i]
#
#         if (ny < 0 or ny >= n) or (nx < 0 or nx >= m):
#             continue
#         if board[ny][nx] == '0':
#             continue
#         if visited[ny][nx] == 0:
#             visited[ny][nx] = 1
#             ret += dfs((ny, nx))
#     return ret
#
#
# if __name__ == '__main__':
#     cnt = 0
#     max_size = 0
#     for r in range(n):
#         for c in range(m):
#             if visited[r][c] == 0 and board[r][c] == '1':
#                 visited[r][c] = 1
#                 max_size = max(max_size, dfs((r, c)))
#                 cnt += 1
#     print(cnt)
#     print(max_size)


# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# board = [list(input().split()) for _ in range(n)]
#
# visited = [[0 for _ in range(m)] for _ in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def dfs(node):
#     if visited[node[0]][node[1]] == 1:
#         return 0
#     visited[node[0]][node[1]] = 1
#
#     ret = 1
#     for i in range(4):
#         ny = node[0] + dy[i]
#         nx = node[1] + dx[i]
#
#         if (ny < 0 or ny >= n) or (nx < 0 or nx >= m):
#             continue
#         if board[ny][nx] == '0':
#             continue
#         ret += dfs((ny, nx))
#     return ret
#
#
# if __name__ == '__main__':
#     cnt = 0
#     max_size = 0
#     for r in range(n):
#         for c in range(m):
#             if visited[r][c] == 0 and board[r][c] == '1':
#                 max_size = max(max_size, dfs((r, c)))
#                 cnt += 1
#     print(cnt)
#     print(max_size)
