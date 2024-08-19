"""
    점프(상향식 dp)

    게임의 목표는 "가장 왼쪽 위" 칸에서 가장 "오른쪽 아래" 칸으로 규칙에 맞게 점프를 해서 가는 것
    각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동
    즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

    규칙에 맞게 갈 수 있는 경로의 개수를 출력
    N (4 ≤ N ≤ 100)

    사고과정.
    N=100 이고 모든 원소가 1이면..
    2^100... 너무 많음.

    1 1 1 .....1 1
    1
    1
    1
    .
    .
    1

    상향식 dp로 해결 경로 갯수 저장후 계산한다.


"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# table = [[0 for _ in range(n)] for _ in range(n)]
# table[0][0] = 1
#
# if __name__ == '__main__':
#     for r in range(n):
#         for c in range(n):
#             if r == 0 and c == 0:
#                 continue
#             cnt = 0
#             # 현재 위치로 위에서 내려올 수 있는 경로.
#             for i in range(c - 1, c - 10, -1):
#                 if i < 0:
#                     break
#                 if board[r][i] + i == c:
#                     cnt += table[r][i]
#             for i in range(r - 1, r - 10, -1):
#                 if i < 0:
#                     break
#                 if board[i][c] + i == r:
#                     cnt += table[i][c]
#
#             table[r][c] = cnt
#
#     # for e in table:
#     #     print(*e)
#     print(table[n - 1][n - 1])
