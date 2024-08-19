"""
    가장 큰 정사각형 찾기.

    1 <= row, col <= 1_000

    사고과정.

    가장 큰 정사각형?
    1_000*1_000 = 1_000_000 (100만)

    완전탐색??
    각 점마다 다시 1인지 확인하면서 2차원탐색을 하면 최대 100만*100만...

    dp 문제라는데.... 전혀 감을 잡을 수가 없었다.
    도형에 관한 지식이 필요한 문제라 생각한다...

    1. (i, j) 칸을 포함하는 정사각형이 존재하려면,
    (위, 오른쪽, 대각선)이 모두 정사각형에 포함되어 있다면 (i, j)가 포함된 정사각형을 만들수가 있다.

    2. 그 정사각형의 크기는?
    (위, 오른쪽, 대각선)중 가장 작은 정사각형보다 1칸 큰 정사각형이 생성된다.
"""


# n = 0
# m = 0
# table = []
#
#
# def solution(board):
#     answer = 0
#     global n, m, table
#
#     n = len(board)
#     m = len(board[0])
#     table = [[0 for col in range(m)] for row in range(n)]
#
#     table[0] = board[0]
#     for row in range(n):
#         table[row][0] = board[row][0]
#
#     for row in range(n):
#         for col in range(m):
#             if row == 0 or col == 0 or board[row][col] == 0:
#                 continue
#             # (위, 오른쪽, 대각선)중 가장 작은것보다 사이즈가 1이 큰 정사각형을 만들수 있다.
#             table[row][col] = min(table[row][col - 1], table[row - 1][col], table[row - 1][col - 1]) + 1
#
#     # for i in range(n):
#     #     print(*table[i])
#
#     max_size = 0
#     for row in range(n):
#         for col in range(m):
#             max_size = max(table[row][col], max_size)
#
#     answer = max_size ** 2
#     return answer
