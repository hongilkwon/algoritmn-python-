"""
    달팽이(단순구현)

    1 => 1 = 1
    3 => 9 = 1+8
    5 => 25 = 1+8+16
    7 => 49 = 1+8+16+24
    9 => 81 = 1+8+16+24+32
   11 => 121 = 1+8+16+24+32+40

    N(3 ≤ N ≤ 999)

    생각보다 구현하려면 쉽지 않음....
"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# target = int(input())
#
# board = [[0 for _ in range(n)] for _ in range(n)]
#
# if __name__ == '__main__':
#
#     num = 1
#
#     # 시작점 >= 1
#     board[(n // 2)][(n // 2)] = 1
#     num += 1
#
#     # 이후 테두리
#     rotate_cnt = n // 2
#     for i in range(rotate_cnt):
#         r = (n // 2) - (i + 1)
#         c = (n // 2) - i
#
#         # 시작점 디버깅
#         # print(r, c)
#         # 왼쪽
#         for j in range(2 * (i + 1) - 1):
#             board[r][c] = num
#             num += 1
#             c += 1
#         # 아래
#         for j in range(2 * (i + 1)):
#             board[r][c] = num
#             num += 1
#             r += 1
#         # 오른쪽
#         for j in range(2 * (i + 1)):
#             board[r][c] = num
#             num += 1
#             c -= 1
#         # 위로
#         for j in range(2 * (i + 1) + 1):
#             board[r][c] = num
#             num += 1
#             r -= 1
#
#     for e in board:
#         print(*e)
#
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == target:
#               print(i+1, j+1)