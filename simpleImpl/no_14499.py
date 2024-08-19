"""
    주사위 굴리기(복잡구현, 시뮬레이션)

    가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

    이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

    주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값

    주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

    사고과정.

    1. 주사위의 상태를 어떻게 표현할 것인가?
    2. 조건을 지키면서, 진행
"""


# import sys
#
# input = sys.stdin.readline
#
# # 편의를 위해 x, y 반대로 받음.
# n, m, y, x, k = map(int, input().split())
#
# board = [list(map(int, input().split())) for r in range(n)]
#
# operators = list(map(int, input().split()))
#
# point = (y, x)
#
# dy = [0, 0, -1, 1]
# dx = [1, -1, 0, 0]
#
# # 윗면 idx1 아랫면 idx3,
# # 북으로 구르면 <= 이동후, 세로의 1,3 => 가로 1,3
#
# # 남으로 구르면 => 이동후, 세로의 1,3 => 가로 1,3
# dice_sero = [0 for _ in range(4)]
#
# # 윗면 idx1 아랫면 idx3,
# # 동으로 구르면 => 이동, 가로 1,3 => 세로 1,3
# # 서로 구르면 <= 이동, 가로 1,3 => 세로 1,3
# dice_garo = [0 for _ in range(4)]
#
# answer = []
#
#
# def move_left(arr):
#     temp = arr[-1]
#     for i in range(len(arr)-1, 0, -1):
#         arr[i] = arr[i - 1]
#     arr[0] = temp
#
#
# def move_right(arr):
#     temp = arr[0]
#     for i in range(len(arr) - 1):
#         arr[i] = arr[i + 1]
#     arr[-1] = temp
#
#
# def go(dir):
#     global point
#
#     ny = point[0] + dy[dir - 1]
#     nx = point[1] + dx[dir - 1]
#
#     if (0 > ny or ny >= n) or (0 > nx or nx >= m):
#         return
#
#     if dir == 1:
#         move_left(dice_garo)
#         dice_sero[1] = dice_garo[1]
#         dice_sero[3] = dice_garo[3]
#     elif dir == 2:
#         move_right(dice_garo)
#         dice_sero[1] = dice_garo[1]
#         dice_sero[3] = dice_garo[3]
#     elif dir == 3:
#         move_left(dice_sero)
#         dice_garo[1] = dice_sero[1]
#         dice_garo[3] = dice_sero[3]
#     elif dir == 4:
#         move_right(dice_sero)
#         dice_garo[1] = dice_sero[1]
#         dice_garo[3] = dice_sero[3]
#
#     if board[ny][nx] == 0:
#         # 바닥면이 0이면,
#         board[ny][nx] = dice_garo[3]
#     else:
#         # 바닥면이 0이 아니면,
#         dice_garo[3] = board[ny][nx]
#         dice_sero[3] = board[ny][nx]
#         board[ny][nx] = 0
#
#     answer.append(dice_garo[1])
#     point = (ny, nx)
#
#
# if __name__ == '__main__':
#     for dir in operators:
#         go(dir)
#
#     for num in answer:
#         print(num)