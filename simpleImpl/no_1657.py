"""
    누울 자리를 찾아라.

    똑바로 연속해서 2칸 이상의 빈 칸이 존재하면
    가로로 누울 수도 있고 세로로 누울 수도 있다
    누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다

    1 <= N <= 100
"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# board = [list(input().rstrip()) for row in range(n)]
#
# dy = [1, 0]
# dx = [0, 1]
#
# cnt_ver = 0
# cnt_hor = 0
#
#
# def go(point):
#     global cnt_ver, cnt_hor
#
#     if board[point[0]][point[1]] == 'X':
#         return
#
#     # 수직
#     ny, nx = point[0] + dy[0], point[1] + dx[0]
#
#     if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '.':
#         if ny + 1 >= n or board[ny + 1][nx] == 'X':
#             cnt_ver += 1
#     # 수평
#     ny, nx = point[0] + dy[1], point[1] + dx[1]
#     if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '.':
#         if nx + 1 >= n or board[ny][nx + 1] == 'X':
#             cnt_hor += 1
#
#
# if __name__ == '__main__':
#     for r in range(n):
#         for c in range(n):
#             go((r, c))
#     print(cnt_hor, cnt_ver)