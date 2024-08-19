"""
    게임맵 최단거리(bfs).
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = 0
# m = 0
# maps = []
#
# visited = []
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start[0]][start[1]] = 1
#
#     while queue:
#         node = queue.popleft()
#
#         for i in range(4):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
#
#             if ny < 0 or ny >= n or nx < 0 or nx >= m:
#                 continue
#             if maps[ny][nx] == 0:
#                 continue
#             if visited[ny][nx] > 0:
#                 continue
#             visited[ny][nx] = visited[node[0]][node[1]] + 1
#             queue.append((ny, nx))
#
#
# def solution(_maps):
#     global n, m, maps, visited
#
#     maps = _maps
#     n = len(_maps)
#     m = len(_maps[0])
#
#     visited = [[0 for col in range(m)] for row in range(n)]
#     bfs((0, 0))
#
#     answer = 0
#     if visited[n - 1][m - 1] == 0:
#         answer = -1
#     else:
#         answer = visited[n - 1][m - 1]
#
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
