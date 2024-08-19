"""
    톱니바퀴(시뮬레이션)

    4개의 톱니바퀴
    k번 회전.

    톱니바퀴의 회전은 한 칸을 기준
    시계 방향 / 반시계 방향

    서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다.

    톱니바퀴를 회전전시
    옆 맞닿은 극 다르 => 반대방향으로 회전
    같으면 => 회전하지 않음.

    최종 톱니바퀴의 상태

    N극은 0,
    S극은 1

    시계방향 => 1
    반시계방향 => -1


    1. 몇번쨰 톱니가 회전할 것 인가
    2. 기준으로 어떤 톱니바퀴가 같이 회전할 것인가

"""

# import sys
#
# input = sys.stdin.readline
#
# circle_list = [list(input().rstrip()) for _ in range(4)]
#
# k = int(input())
#
# operators = []
# for _ in range(k):
#     n, d = map(int, input().split())
#     operators.append((n, d))
#
#
# def rotate(num, dir):
#     circle = circle_list[num]
#     if dir == 1:
#         # 시계 방향.
#         temp = circle[-1]
#         for i in range(len(circle)-1, 0, -1):
#             circle[i] = circle[i - 1]
#         circle[0] = temp
#     else:
#         # 반시계 방향
#         temp = circle[0]
#         for i in range(len(circle) - 1):
#             circle[i] = circle[i + 1]
#         circle[-1] = temp
#
#
# if __name__ == '__main__':
#
#     temp_list = []
#     for oper in operators:
#         n, d = oper[0] - 1, oper[1]
#         temp_list.append((n, d))
#
#         # n기준 왼쪽톱니.
#         dir = d
#         connected = circle_list[n][-2]
#         for r in range(n - 1, -1, -1):
#             if circle_list[r][2] == connected:
#                 break
#             dir = -1 if dir == 1 else 1
#             connected = circle_list[r][-2]
#             temp_list.append((r, dir))
#
#         # n기준 오른쪽톱니.
#         dir = d
#         connected = circle_list[n][2]
#         for r in range(n + 1, len(circle_list)):
#             if circle_list[r][-2] == connected:
#                 break
#             dir = -1 if dir == 1 else 1
#             connected = circle_list[r][2]
#             temp_list.append((r, dir))
#
#         for e in temp_list:
#             num, dir = e
#             rotate(num, dir)
#         temp_list.clear()
#
#     # for e in circle_list:
#     #     print(*e)
#     point = 0
#     for i in range(4):
#         point += int(circle_list[i][0]) * (2 ** i)
#     print(point)