"""
     충돌위험 찾기(시뮬레이션)

    - 생각보다 복잡함....
    - 충돌위치를 구하는데 있어 시간복잡도 걸리는 테스트케이스가 존재함...
"""


# import sys
#
# input = sys.stdin.readline
#
# board = [[0 for c in range(101)] for r in range(101)]
#
# max_time = 0
# routes_points = []
#
# points = []
# routes = []
#
#
# def make_routes_points():
#     global points, routes, max_time
#
#     for i in range(len(routes)):
#
#         # print('로봇', n)
#         temp = list()
#
#         current_route = routes[i]
#         init_point = points[current_route[0] - 1]
#         temp.append(init_point)
#
#         for j in range(len(current_route) - 1):
#             start_point = points[current_route[j] - 1]
#             end_point = points[current_route[j + 1] - 1]
#             # print(start_point, end_point)
#
#             # row
#             diff_r = end_point[0] - start_point[0]
#             if diff_r > 0:
#                 for _ in range(abs(diff_r)):
#                     prev = temp[-1]
#                     nxt = [prev[0] + 1, prev[1]]
#                     temp.append(nxt)
#             elif diff_r < 0:
#                 for _ in range(abs(diff_r)):
#                     prev = temp[-1]
#                     np = [prev[0] - 1, prev[1]]
#                     temp.append(np)
#
#             # col
#             diff_c = end_point[1] - start_point[1]
#             if diff_c > 0:
#                 for _ in range(abs(diff_c)):
#                     prev = temp[-1]
#                     nxt = [prev[0], prev[1] + 1]
#                     temp.append(nxt)
#             elif diff_c < 0:
#                 for _ in range(abs(diff_c)):
#                     prev = temp[-1]
#                     nxt = [prev[0], prev[1] - 1]
#                     temp.append(nxt)
#
#         max_time = max(max_time, len(temp))
#         routes_points.append(temp)
#
# if __name__ == '__main__':
#     # solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])
#     # solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])
#     # solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])

# def solution(p, r):
#     global points, routes, board
#     points, routes = p, r
#
#     make_routes_points()
#
#     cnt = 0
#     for time in range(max_time):
#         # clear_board
#         # board = [[0 for c in range(101)] for r in range(101)]
#         temp_dict = dict()
#
#         # move
#         for routes in routes_points:
#             if len(routes) - 1 < time:
#                 continue
#             r, c = routes[time]
#             if (r, c) in temp_dict:
#                 temp_dict[(r,c)] += 1
#             else:
#                 temp_dict[(r, c)] = 1
#
#         for v in temp_dict.values():
#             if v >= 2:
#                 cnt += 1
#
#     print(cnt)
#     return cnt
#
#     import sys
#
#     input = sys.stdin.readline
#
#     board = [[0 for c in range(102)] for r in range(102)]
#
#     max_time = 0
#     routes_points = []
#
#     points = []
#     routes = []
#
#
#     def make_routes_points():
#         global points, routes, max_time
#
#         for i in range(len(routes)):
#
#             # print('로봇', n)
#             temp = list()
#
#             current_route = routes[i]
#             init_point = points[current_route[0] - 1]
#             temp.append(init_point)
#
#             for j in range(len(current_route) - 1):
#                 start_point = points[current_route[j] - 1]
#                 end_point = points[current_route[j + 1] - 1]
#                 # print(start_point, end_point)
#
#                 # row
#                 diff_r = end_point[0] - start_point[0]
#                 if diff_r > 0:
#                     for _ in range(abs(diff_r)):
#                         prev = temp[-1]
#                         nxt = [prev[0] + 1, prev[1]]
#                         temp.append(nxt)
#                 elif diff_r < 0:
#                     for _ in range(abs(diff_r)):
#                         prev = temp[-1]
#                         np = [prev[0] - 1, prev[1]]
#                         temp.append(np)
#
#                 # col
#                 diff_c = end_point[1] - start_point[1]
#                 if diff_c > 0:
#                     for _ in range(abs(diff_c)):
#                         prev = temp[-1]
#                         nxt = [prev[0], prev[1] + 1]
#                         temp.append(nxt)
#                 elif diff_c < 0:
#                     for _ in range(abs(diff_c)):
#                         prev = temp[-1]
#                         nxt = [prev[0], prev[1] - 1]
#                         temp.append(nxt)
#
#             max_time = max(max_time, len(temp))
#             routes_points.append(temp)
#
#
#     def solution(p, r):
#         global points, routes, board
#         points, routes = p, r
#
#         make_routes_points()
#
#         cnt = 0
#         for time in range(max_time):
#             # clear_board
#             board = [[0 for c in range(102)] for r in range(102)]
#
#             # move
#             for routes in routes_points:
#                 if len(routes) - 1 < time:
#                     continue
#                 r, c = routes[time]
#                 board[r][c] += 1
#
#             for r in range(101):
#                 for c in range(101):
#                     if board[r][c] >= 2:
#                         cnt += 1
#         # print(cnt)
#         return cnt
#




