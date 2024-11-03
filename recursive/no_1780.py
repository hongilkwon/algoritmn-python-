"""
    종이의 개수(재귀)

    27        9        3
    0 9 18 => 0 3 6 => 0 1 2

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# cnt_dict = {-1: 0, 0: 0, 1: 0}
#
#
# def chk(t, p, s):
#     for r in range(p[0], p[0] + s):
#         for c in range(p[1], p[1] + s):
#             if board[r][c] != t:
#                 return False
#     return True
#
#
# def go(point, size):
#     type_paper = board[point[0]][point[1]]
#     if chk(type_paper, point, size):
#         cnt_dict[type_paper] += 1
#         return
#
#     next_size = size // 3
#
#     for i in range(point[0], point[0] + size, next_size):
#         for j in range(point[1], point[1] + size, next_size):
#             go((i, j), next_size)
#
#
# if __name__ == '__main__':
#     go((0, 0), len(board))
#     for k, v in cnt_dict.items():
#         print(v)

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# cnt_dict = {-1: 0, 0: 0, 1: 0}
#
#
# 시간초과
# def chk(p, t):
#     for r in range(len(p)):
#         for c in range(len(p[r])):
#             if p[r][c] != t:
#                 return False
#     return True
#
#
# def go(p):
#     if chk(p, p[0][0]):
#         cnt_dict[p[0][0]] += 1
#         return
#
#     next_size = len(p) // 3
#     for i in range(0, len(p), next_size):
#         for j in range(0, len(p[i]), next_size):
#             new_p = [[0 for _ in range(next_size)] for _ in range(next_size)]
#             # 복사
#             start = (i, j)
#             for r in range(next_size):
#                 for c in range(next_size):
#                     new_p[r][c] = p[start[0] + r][start[1] + c]
#             # print(new_p)
#             go(new_p)
#
#
# if __name__ == '__main__':
#     go(board)
#     for k, v in cnt_dict.items():
#         print(v)
