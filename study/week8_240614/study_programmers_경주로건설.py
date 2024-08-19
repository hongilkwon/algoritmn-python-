"""
    경주로 건설(그래프 탐색, dp)

    출발점은 (0, 0) 칸(좌측 상단)이며, 도착점은 (N-1, N-1) 칸(우측 하단)입니다
    끊기지 않도록 경주로를 건설해야 합니다.

    직선 - 100
    코너 - 500

    3 <= 배열크기 <= 25

    사고과정.

    이전 방향과 같다면 직선.
    아니면 코너.

    그래프 탐색을 이용해야 되고,
    재방문을 허용해야 되는가???

    생각이 많아지고 복잡해진다..

    결국 어느 방향에서 왔을때 최소비용을 가지는가!
    이것을 계산하는 문제이다.

    그래프 탐색 + dp
"""

# import sys
# from collections import deque
#
# n = 0
# board = []
#
# # 시계 방향(상, 우, 하, 좌)
# dy = [1, 0, -1, 0,]
# dx = [0, 1, 0, -1,]
#
# visited_direction = []
#
#
# def bfs():
#     queue = deque()
#     queue.append([0, 0, -1])
#     visited_direction[0][0] = [0, 0, 0, 0]
#
#     while queue:
#         y, x, d = queue.popleft()
#
#         for i in range(4):
#             # 반대 방향으로 움직이는 경우 가면 안됨.
#             if (d == 0 and i == 2) or (d == 2 and i == 0):
#                 continue
#             if (d == 1 and i == 3) or (d == 3 and i == 1):
#                 continue
#
#             # 방향에 따른 비용 계산.
#             ny = y + dy[i]
#             nx = x + dx[i]
#             cost = 100
#             # 기존의 반향과 다르면 또는 시작점 아니라면
#             if i != d and d != -1:
#                 cost += 500
#
#             if 0 > ny or ny >= n or 0 > nx or nx >= n:
#                 continue
#
#             if board[nx][ny] == 1:
#                 continue
#
#             if visited_direction[ny][nx][i] > visited_direction[y][x][d] + cost:
#                 visited_direction[ny][nx][i] = visited_direction[y][x][d] + cost
#                 queue.append([ny, nx, i])
#
# def solution(_board):
#     global board, n, visited_direction
#     board = _board
#
#     n = len(board)
#     visited_direction = [[[sys.maxsize for d in range(4)] for col in range(n)] for row in range(n)]
#     bfs()
#
#     print(visited_direction)
#     answer = min(visited_direction[n - 1][n - 1])
#     # print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(
#         [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     )
