"""

    프렌트4 블록(시뮬레이션)


    여러 개 있다면 한꺼번에 지워진다.
    같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
    블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

    2 ≦ n, m ≦ 30
    (30 * 30) 900
"""


# import sys
#
# input = sys.stdin.readline
#
# m = 0
# n = 0
# board = None
#
#
# def solution(_m, _n, _board):
#     answer = 0
#     global m, n, board
#     m, n = _m, _n
#
#     board = [list(_board[i]) for i in range(m)]
#
#     points = set()
#     while True:
#         # 2*2 블록 지우기
#         for i in range(m - 1):
#             for j in range(n - 1):
#                 c = board[i][j]
#                 if c == ' ':
#                     continue
#                 if c == board[i][j + 1] and c == board[i + 1][j] and c == board[i + 1][j + 1]:
#                     points.update([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
#
#         if not points:
#             break
#
#         for p in points:
#             r, c = p
#             board[r][c] = ' '
#
#         # 블록 내리기
#         for c in range(n):
#             temp = ''
#             for r in range(m):
#                 if board[r][c] != ' ':
#                     temp += board[r][c]
#
#             for r in range(m):
#                 if r < m - len(temp):
#                     board[r][c] = ' '
#                 else:
#                     board[r][c] = temp[r - (m - len(temp))]
#         # for e in board:
#         #     print(e)
#         # print()
#         points.clear()
#
#     cnt = 0
#     for r in range(m):
#         for c in range(n):
#             if board[r][c] == ' ':
#                 cnt += 1
#
#     answer = cnt
#     print(cnt)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(4,	5,	["CCBDE", "AAADE", "AAABF", "CCBBF"])
