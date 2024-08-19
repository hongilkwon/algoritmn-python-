"""
    방문길이

     우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
     단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

     사고과정.

     단순구현
     1. 좌표 평면을 2차원 배열로 표현,
     2. 지나간 길을 edge의 확인을 집합으로 처리
     3. 길은 역방향도 지나간것으로 처리한다.

"""

# board = [[0 for col in range(11)] for row in range(11)]
#
# # U R D L
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def solution(dirs):
#     answer = 0
#
#     cnt = 0
#
#     y = 5
#     x = 5
#     visited = set()
#     for d in dirs:
#         if d == 'U':
#             ny = y + dy[0]
#             nx = x + dx[0]
#         elif d == 'R':
#             ny = y + dy[1]
#             nx = x + dx[1]
#         elif d == 'D':
#             ny = y + dy[2]
#             nx = x + dx[2]
#         elif d == 'L':
#             ny = y + dy[3]
#             nx = x + dx[3]
#
#         if 0<= ny < 11 and 0<= nx < 11:
#             if (y, x, ny, nx) not in visited:
#                 visited.add((y,x, ny, nx))
#                 visited.add((ny, nx, y,x))
#                 cnt += 1
#             y = ny
#             x = nx
#
#     # for e in board:
#     #     print(*e)
#
#     answer = cnt
#     # print(answer)
#     return answer
