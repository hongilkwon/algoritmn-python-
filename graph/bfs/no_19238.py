"""
    스타트 택시(bfs)

    손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.

    특정 위치로 이동할 때 항상 최단경로로만 이동
    M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다
    백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다.


    각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.


    1. 태울 승객을 고를 때는 "현재 위치"에서 "최단거리가 가장 짧은 승객"을 고른다
    행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을

    2. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 "소모한 연료 양의 두 배"가 충전된다
    * 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.


    모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.

    (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000)
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
#
# board = [list(map(int, input().split())) for r in range(n)]
#
# init_start = tuple(map(int, input().split()))
#
# start_set = set()
# end_dict = dict()
#
# for i in range(m):
#     sy, sx, ey, ex = map(int, input().split())
#     start_set.add((sy - 1, sx - 1))
#     end_dict[(sy - 1, sx - 1)] = (ey - 1, ex - 1)
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def bfs_find_customer(start):
#     q = deque()
#     q.append(start)
#
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     visited[start[0]][start[1]] = 1
#     temp = []
#
#     while q:
#         temp_q = deque()
#         for y, x in q:
#             if (y, x) in start_set:
#                 temp.append((y, x))
#
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#
#                 if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                     continue
#                 if board[ny][nx] == 1:
#                     continue
#                 if visited[ny][nx] > 0:
#                     continue
#
#                 visited[ny][nx] = visited[y][x] + 1
#                 temp_q.append((ny, nx))
#
#         if temp:
#             temp.sort(key=lambda e: (e[0], e[1]))
#             ry, rx = temp[0]
#             return ry, rx, visited[ry][rx]-1
#         q= temp_q
#
#     return -1, -1, -1
#
#
# def bfs(start, end):
#     q = deque()
#     q.append(start)
#
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     visited[start[0]][start[1]] = 1
#
#     while q:
#         y, x = q.popleft()
#
#         if (y, x) == end:
#             return visited[y][x] - 1
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
#                 continue
#             if board[ny][nx] == 1:
#                 continue
#             if visited[ny][nx] > 0:
#                 continue
#
#             visited[ny][nx] = visited[y][x] + 1
#             q.append((ny, nx))
#     return -1
#
#
# if __name__ == '__main__':
#
#     current = (init_start[0] - 1, init_start[1] - 1)
#
#     for _ in range(m):
#         # 손님 태우러 가기
#         sy, sx, d = bfs_find_customer(current)
#         if d == -1 or k < d:
#             k = -1
#             break
#         k -= d
#         start_set.remove((sy, sx))
#
#         # 출발지에서 목적지 가기
#         ey, ex = end_dict[(sy, sx)]
#         d = bfs((sy, sx), (ey, ex))
#         if d == -1 or k < d:
#             k = -1
#             break
#         k -= d
#
#         # 목적지가 현재위치로, 연료 채우기
#         current = (ey, ex)
#         k += (d * 2)
#     print(k)