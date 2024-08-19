"""
    어른상어(시뮬레이션)

    상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다.
    상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, "1의 번호를 가진 어른 상어"는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.


    맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
    그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다.
    냄새는 상어가 k번 이동하고 나면 사라진다

    이동 방향을 결정할 때는,
    먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.

    모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

    사고과정.

    보드 - 상어가 있는지, 어떤 상어의 냄새가, 얼마나 남았는지,
    상어 - 번호, 쫒겨났는지 아닌지, 현재 이동방향, 우선순위.

    1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
"""


# import sys
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# # 상어정보(상어번호, y, x, dir, is_valid(0, 1))
# shark_list = [[0] * 4 for _ in range(m)]
# # board 정보(상어, 냄새)
# board = [[[-1, 0] for _ in range(n)] for _ in range(n)]
# for r in range(n):
#     for c in range(n):
#         if arr[r][c] != 0:
#             shark_num = arr[r][c] - 1
#             shark_list[shark_num] = [shark_num, r, c, 0]
#             board[r][c][0], board[r][c][1] = shark_num, k
# # 초기방향
# init_dir = list(map(int, input().split()))
# for i in range(m):
#     shark_list[i][3] = init_dir[i]
#
# # 우선순위 dir_priority[상어번호][현재방향]
# dir_priority = [[[0] * 4 for _ in range(5)] for _ in range(m)]
# for i in range(m):
#     for j in range(1, 5):
#         dir_priority[i][j] = list(map(int, input().split()))
# # 방향 백터
# dy = [0, -1, 1, 0, 0]
# dx = [0, 0, 0, -1, 1]
#
# if __name__ == '__main__':
#     time = 0
#     while time <= 1000:
#         if time == 1000:
#             time = -1
#             break
#         time += 1
#         # 이동(빈칸, 자기냄새)
#         for i in range(m):
#             shark_num, y, x, dir = shark_list[i]
#             if shark_num == -1:
#                 continue
#
#             new_dir = -1
#             new_point = (-1, -1)
#             # 빈 공간 찾기
#             for d in dir_priority[shark_num][dir]:
#                 ny, nx = y + dy[d], x + dx[d]
#                 if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                     continue
#                 if board[ny][nx][0] == -1:
#                     new_dir = d
#                     new_point = (ny, nx)
#                     break
#             # 빈 공간을 못 찾은 경우
#             if new_point == (-1, -1):
#                 for d in dir_priority[shark_num][dir]:
#                     ny, nx = y + dy[d], x + dx[d]
#                     if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                         continue
#                     if board[ny][nx][0] == shark_num:
#                         new_dir = d
#                         new_point = (ny, nx)
#                         break
#             shark_list[i] = [shark_num, new_point[0], new_point[1], new_dir]
#
#         # 각 칸마다 냄새 -1
#         for r in range(n):
#             for c in range(n):
#                 info = board[r][c]
#                 if info[0] != -1:
#                     info[1] -= 1
#                 if info[1] == 0:
#                     info[0] = -1
#
#         # 새로운 냄새 남기고, 상어 쫒아내기(작은 번호로 업데이트 되어 있다면, )
#         for i in range(m):
#             shark_num, y, x, dir = shark_list[i]
#             if board[y][x][0] != -1 and board[y][x][0] != shark_num:
#                 # 상어 번호를 -1로 하여 쫒겨난것으로 표기
#                 shark_list[i] = [-1, y, x, dir]
#             else:
#                 board[y][x] = [shark_num, k]
#
#         chk = True
#         for i in range(1, len(shark_list)):
#             if shark_list[i][0] != -1:
#                 chk = False
#                 break
#         if chk:
#             break
#
#     print(time)

# 실패한 코드.
# import sys
#
# input = sys.stdin.readline
#
#
# class Shark:
#     def __init__(self, num, point, direction, priority):
#         self.num = num
#         self.is_valid = True
#         self.point = point
#         self.direction = direction
#         self.priority = priority
#
#     def __repr__(self):
#         return (f"Shark(num={self.num}, is_valid={self.is_valid}, point={self.point}, direction={self.direction}, "
#                 f"priority={self.priority})")
#
#
# n, m, k = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
# init_point = [(-1, -1) for _ in range(m + 1)]
# for r in range(n):
#     for c in range(n):
#         if board[r][c] != 0:
#             init_point[board[r][c]] = (r, c)
#             board[r][c] = [True, board[r][c], k]
#         else:
#             board[r][c] = [False, 0, 0]
#
# # 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
# init_dir = [-1] + list(map(int, input().split()))
# shark_list = [Shark(num=-1, point=(-1, -1), direction=-1, priority=[]) for _ in range(m + 1)]
#
# for i in range(1, m + 1):
#     p = [[0, 0, 0, 0]] + [list(map(int, input().split())) for _ in range(4)]
#     shark_list[i] = Shark(num=i, point=init_point[i], direction=init_dir[i], priority=p)
#
# dy = [0, -1, 1, 0, 0]
# dx = [0, 0, 0, -1, 1]
#
#
# def down_small():
#     for r in range(n):
#         for c in range(n):
#             info = board[r][c]
#             if info[1] != 0:
#                 info[2] -= 1
#
#
# def remove_small():
#     for r in range(n):
#         for c in range(n):
#             info = board[r][c]
#             if info[2] == 0:
#                 info[1] = 0
#
#
# # 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향
# def move(num):
#     shark = shark_list[num]
#
#     if not shark.is_valid:
#         return
#
#     # 다음 이동할 칸 구하기.
#     point = shark.point
#     new_dir = -1
#     new_point = (-1, -1)
#
#     # 빈 공간중에 이동할 곳 찾기
#     for next in shark.priority[shark.direction]:
#         ny = point[0] + dy[next]
#         nx = point[1] + dx[next]
#
#         if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#             continue
#         if board[ny][nx][0] and board[ny][nx][2] == k:
#             shark.is_valid = False
#             return
#         if board[ny][nx][1] == 0:
#             new_dir = next
#             new_point = (ny, nx)
#             break
#
#     # 빈 공간이 없을 때
#     if new_point[0] == -1 and new_point[1] == -1:
#         for next in shark.priority[shark.direction]:
#             ny = point[0] + dy[next]
#             nx = point[1] + dx[next]
#             if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                 continue
#             if board[ny][nx][1] == shark.num:
#                 new_dir = next
#                 new_point = (ny, nx)
#                 break
#
#     # 이동
#     shark.direction = new_dir
#     shark.point = new_point
#
#     board[point[0]][point[1]][0] = False
#     board[new_point[0]][new_point[1]] = [True, num, k]
#
#
# if __name__ == '__main__':
#     # print(shark_list)
#     time = 0
#     cnt = 0
#
#     while time <= 1001:
#         if time == 1001:
#             time = -1
#             break
#         time += 1
#
#         down_small()
#         for num in range(1, m + 1):
#             move(num)
#         remove_small()
#
#         print(f"time:{time + 1}")
#         for e in board:
#             print(*e)
#         print()
#
#         chk = True
#         for i in range(2, len(shark_list)):
#             if shark_list[i].is_valid:
#                 chk = False
#                 break
#         if chk:
#             break
#     print(time)
