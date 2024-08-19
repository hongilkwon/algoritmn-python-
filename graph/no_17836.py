"""
    공주님을 구해라


    (N, M) 위치에 있는 공주님을 구출
    T시간 이내로 용사를 만나지 못한다면 영원히 돌로 변하게 된다

    "그람"은 성의 어딘가에 반드시 한 개 존재하고, 용사는 그람이 있는 곳에 도착하면 바로 사용할 수 있다

    그람을 갖고 있는 상태 와 그렇지 못한 상태
    그람 2
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m, t = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
#
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]][start[2]] = 1
#
#     while q:
#         s, y, x = q.popleft()
#
#         if board[y][x] == 2:
#             s = 1
#             visited[s][y][x] = visited[0][y][x]
#
#         for i in range(4):
#
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if ny < 0 or ny >= n or nx < 0 or nx >= m:
#                 continue
#
#             if s == 0 and board[ny][nx] == 1:
#                 continue
#             if visited[s][ny][nx] > 0:
#                 continue
#
#             visited[s][ny][nx] = visited[s][y][x] + 1
#             q.append((s, ny, nx))
#
#
# if __name__ == '__main__':
#     bfs((0, 0, 0))
#
#     # temp1 = visited[0]
#     # for e in temp1:
#     #     print(*e)
#     # print()
#     # temp2 = visited[1]
#     # for e in temp2:
#     #     print(*e)
#
#     d1 = visited[0][n - 1][m - 1]
#     d2 = visited[1][n - 1][m - 1]
#
#     if d1 == 0 and d2 == 0:
#         print("Fail")
#     else:
#         min_dist = 0
#         if d1 != 0 and d2 == 0:
#             min_dist = d1 - 1
#         elif d1 == 0 and d2 != 0:
#             min_dist = d2 - 1
#         else:
#             min_dist = min(d1 - 1, d2 - 1)
#
#         if min_dist <= t:
#             print(min_dist)
#         else:
#             print("Fail")
