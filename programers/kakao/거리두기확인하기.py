"""
    거리두기 확인하기(카카오 인턴 문제)

    맨해튼 거리1가 2 이하로 앉지 말아 주세요.
    파티션으로 막혀 있을 경우에는 허용

    대기실별로 거리두기를 지키고 있으면 1을,
    한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

    사고과정.

    사람마다 맨해튼 거리인 2만큼을 전부 탐색해서, 그중에 사람이 있으면?

        0
      0 0 0
    0 0 P 0 0
      0 0 0
        0

    거리가 2이기 때문에 P를 중심으로 12의 점을 직접 구해서 완전탐색으로 검사할 수도 있지만,
    dfs/bfs 탐색 횟수를 제한하여 검색을 할 수 도있다.

    2가지 탐색법 모두다 구현해 보자!
    또한 두가지 탐색의 구현에 있어 각 구현부의 의미를 잘 파악하고 있어야 한다.

"""

# from collections import deque
#
# place = []
#
# visited = []
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# # bfs 풀이
# def go(start):
#     global visited
#     visited = [[0 for c in range(5)] for r in range(5)]
#     q = deque()
#
#     visited[start[0]][start[1]] = 1
#     q.append(start)
#
#     while q:
#         node = q.popleft()
#
#         y = node[0]
#         x = node[1]
#         d = node[2]
#
#         if d != 0 and place[y][x] == 'P':
#             return False
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
#                 continue
#             if place[ny][nx] == 'X':
#                 continue
#             if d + 1 > 2:
#                 continue
#             if visited[ny][nx] == 1:
#                 continue
#             visited[ny][nx] = 1
#             q.append((ny, nx, d + 1))
#     return True
#
#
# def solution(places):
#     answer = []
#     global place
#
#     for e in places:
#         place = e
#         points_p = []
#         for i in range(len(place)):
#             for j in range(len(place[i])):
#                 if place[i][j] == 'P':
#                     points_p.append((i, j, 0))
#
#         flag = True
#         for point in points_p:
#             ret = go(point)
#             if not ret:
#                 flag = False
#                 break
#
#         if flag:
#             answer.append(1)
#         else:
#             answer.append(0)
#     # print(answer)
#     return answer


# if __name__ == '__main__':
#     solution(
#         [
#             ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#             ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#             ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#             ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#             ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
#         ]
#     )
