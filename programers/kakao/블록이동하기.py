"""
    블록 이동하기

    "0"은 빈칸을 "1"은 벽
    로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다.
    로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작

    로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만,
    회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다.

    로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간

    사고과정.

    로봇은 2칸을 차지 한다는 점. --> visited를 set으로 처리한다.
    회전이동할 수 있다는 점.

    회전 처리를 할때, 로봇의 상태 / 회전 방향/ 회전 축/
    너무 처리가 복잡하다..

    * 로봇이 어떤 상태로 해당 좌표를 방문하는가를 구별하여, 해결한 풀이.
    실전에서 생각하기 매우 어렵다.
    https://www.youtube.com/watch?v=XLa2JL_UCko

"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = 0
# board = []
# visited = set()
#
# # 시계방향(상, 우, 하, 좌)
# dir = [(-1, 0), (0, 1), (1, 0), (0, -1),]
#
# rotate = []
#
#
# def go(start):
#     q = deque()
#     q.append((start, 0))
#     visited.add(start)
#
#     while q:
#         (p1, p2), time = q.popleft()
#         if p1 == (n - 1, n - 1) or p2 == (n - 1, n - 1):
#             return time
#
#         # 직선이동.
#         for dy, dx in dir:
#             np1 = (p1[0] + dy, p1[1] + dx)
#             np2 = (p2[0] + dy, p2[1] + dx)
#
#             # 보드의 범위 확인
#             if np1[0] < 0 or np1[0] >= n or np1[1] < 0 or np1[1] >= n:
#                 continue
#             if np2[0] < 0 or np2[0] >= n or np2[1] < 0 or np2[1] >= n:
#                 continue
#             # 이동 후 벽인지 확인
#             # print("np1:", np1, "np2:", np2)
#             if board[np1[0]][np1[1]] == 1 or board[np2[0]][np2[1]] == 1:
#                 continue
#             # 방문 여부 확인
#             if (np1, np2) in visited:
#                 continue
#
#             visited.add((np1, np2))
#             q.append(((np1, np2), time + 1))
#
#         # 회전이동.
#         # @--@ 로봇이 가로일 경우
#         if p1[0] == p2[0]:
#             # 행을 기준으로 아래로 회전, 위로 회전 (x+1 또는 x-1)
#             for d in [-1, 1]:
#                 # 이동할 공간이 비어있고, 대각선의 장애물이 아닌 경우
#                 if ((0 <= p1[0] + d < n) and (board[p1[0] + d][p1[1]] == 0)
#                         and (0 <= p2[0] + d < n) and (board[p2[0] + d][p2[1]] == 0)):
#                     # 왼쪽 축
#                     next1 = (p1, (p1[0] + d, p1[1]))
#                     # 오른쪽 축
#                     next2 = ((p2[0] + d, p2[1]), p2)
#                     if next1 not in visited:
#                         visited.add(next1)
#                         q.append((next1, time + 1))
#                     if next2 not in visited:
#                         visited.add(next2)
#                         q.append((next2, time + 1))
#         # @ 로봇이 세로
#         # |
#         # @
#         if p1[1] == p2[1]:
#             for d in [-1, 1]:
#                 if ((0 <= p1[1] + d < n) and (board[p1[0]][p1[1] + d] == 0)
#                         and (0 <= p2[1] + d < n) and (board[p2[0]][p2[1] + d] == 0)):
#                     # 위 축
#                     next1 = (p1, (p1[0], p1[1] + d))
#                     # 아래 축
#                     next2 = ((p2[0], p2[1] + d), p2)
#                     if next1 not in visited:
#                         visited.add(next1)
#                         q.append((next1, time + 1))
#                     if next2 not in visited:
#                         visited.add(next2)
#                         q.append((next2, time + 1))
#
#
# def solution(_board):
#     answer = 0
#     global board, n
#     board = _board
#     n = len(board)
#     answer = go(((0, 0), (0, 1)))
#     # print(answer)
#     return answer

# if __name__ == '__main__':
#     solution(
#              [[0, 0, 0, 1, 1],
#               [0, 0, 0, 1, 0],
#               [0, 1, 0, 1, 1],
#               [1, 1, 0, 0, 1],
#               [0, 0, 0, 0, 0]]
#              )
