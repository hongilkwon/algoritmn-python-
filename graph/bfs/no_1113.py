"""
       수영장 만들기(bfs, 탐색 활용).

    물은 항상 높이가 더 낮은 곳으로만 흐르고,
    직육면체 위의 표면에는 물이 없다. 그리고,
    땅의 높이는 0이고, 땅은 물을 무한대로 흡수 할 수 있다.

    1 <= N,M <= 50
    1 <= 높이 <= 9

    사고과정.

    어떻게 하면 수영장이 만들어지지? 상대적으로 높을곳으로 4방향이 둘러 쌓여 있다.

    물의 높이는 어떻게 정해지는가? 둘러쌓인 4개의 면중 가장 높이가 작은것으로 물이 채워진다.

    서로 단차가 생기는 물의 높이는 어떻게 할것인가???
    -> 탐색을 시작점을 기준으로 높이가 낮은 곳으로 하며,
    탐색을 끝내면, 물을 채워야됨.

    * 직육면체의 땅의 테두리 지역과 단 1개의 블록이라도 붙어 있다면? 물이 빠져서 물이 고일 수 없다.

    DFS ? BFS ?
    -> 어떤 탐색방법을 사용해도 문제를 푸는데 지장은 없어 보인다.
    하지만, 재귀적 방법인 DFS를 사용하면, 범위를 넘어서는 경우 함수의 종료가 쉽지 않음.
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# pool = [list(map(int, list(input().strip()))) for r in range(n)]
#
# water_height = 9
# points = []
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def bfs(start):
#     global water_height
#     global points
#
#     limit_height = pool[start[0]][start[1]]
#     q = deque()
#     visited = [[False for c in range(m)] for r in range(n)]
#
#     visited[start[0]][start[1]] = True
#     points.append(start)
#     q.append(start)
#
#     while q:
#         node = q.popleft()
#         for i in range(4):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
#
#             if ny < 0 or ny >= n or nx < 0 or nx >= m:
#                 return False
#
#             if limit_height < pool[ny][nx]:
#                 water_height = min(water_height, pool[ny][nx])
#                 continue
#
#             if visited[ny][nx]:
#                 continue
#
#             visited[ny][nx] = True
#             points.append((ny, nx))
#             q.append((ny, nx))
#
#     return True
#
#
# if __name__ == '__main__':
#
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             water_height = 9
#             points.clear()
#             ret = bfs((i, j))
#             if ret:
#                 for p in points:
#                     cnt += water_height - pool[p[0]][p[1]]
#                     pool[p[0]][p[1]] = water_height
#     print(cnt)
