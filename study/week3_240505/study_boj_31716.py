"""
    현대모비스 자율주행 테스트 1

    1 <= n <= 100_000
    1 <= k <= 1_000_000_000

    사고과정

    1. bfs -> 트렉의 최단거리
    2. 트랙의 연결부분 처리 --> 4*4 = 16개? 처리해야할 경우가 너무 많다.
    3. 왜 트랙을 이어붙히면 최단거리가 달라질까??


    시작 - 끝 시작 - 끝 시작 - 끝.....

    예시)

    . . . # .
    . # . . .

    . . . # . . . . # .
    . # . . . . # . . .

    트랙을 1개의 최단거리
    트랙을 2개만 연결하여 최단거리를 구하면, 트랙 + 연결부위 + 트랙의 최단거리가 나온다

    그럼 트랙을 2개 연결한 최단거리 - 트랙 1개의 최단거리 = 트랙 1개 + 연결부위 까지의 최단거리가 나온다.

    (k-1)개를 연결하고 나머지 트랙 1개의 최단거리를 더해주면 최종 최단거리가 나온다.

    배운점
    가중치가 동일한 그래프의 최단거리 문제라 bfs를 사용하겠다는 건 쉽게 생각할 수있다.
    하지만, 연결할 트랙이 K(10억개)라 트랙이 1번 연결될때 어떤 특징을 잡아서 반복되는지 확인해야된다.
    또한 출발점과 도착점이 여러개라 이것 또한 고려해야된다.

"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
#
# track = [['' for col in range(n)] for row in range(2)]
# for i in range(2):
#     track[i] = list(input().strip())
#
# double_track = [['' for col in range(2 * n)] for row in range(2)]
# for i in range(2):
#     double_track[i] = track[i] + track[i]
#
# INF = 1_000_000_000
#
# visited = [[[0 for col in range(n)] for row in range(2)] for s in range(2)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def bfs(start, node, track):
#     # 시작할 없는 지점('#')이면, 리턴.
#     if track[node[0]][node[1]] == '#':
#         return
#
#     queue = deque()
#     queue.append(node)
#     visited[start][node[0]][node[1]] = 1
#
#     while queue:
#
#         current = queue.pop()
#         y = current[0]
#         x = current[1]
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or ny >= 2 or nx < 0 or nx >= len(track[0]):
#                 continue
#             if track[ny][nx] == '#':
#                 continue
#             if visited[start][ny][nx] > 0:
#                 continue
#
#             visited[start][ny][nx] = visited[start][y][x] + 1
#             queue.append([ny, nx])
#
#
# if __name__ == '__main__':
#
#     # 기본 track 최단거리
#     visited = [[[0 for col in range(n)] for row in range(2)] for s in range(2)]
#     bfs(start=0, node=[0, 0], track=track)
#     bfs(start=1, node=[1, 0], track=track)
#
#     # visited를 순회하면서 2개의 시작점에 따른 도착점들
#     track_dist = INF
#     for sp in range(2):
#         for row in range(2):
#             if visited[sp][row][n - 1] != 0:
#                 track_dist = min(track_dist, visited[sp][row][n - 1] - 1)
#
#     if track_dist == INF:
#         print(-1)
#         exit(0)
#
#     # 2개의 연결된 track 최단거리
#     visited = [[[0 for col in range(n * 2)] for row in range(2)] for s in range(2)]
#     bfs(start=0, node=[0, 0], track=double_track)
#     bfs(start=1, node=[1, 0], track=double_track)
#
#     double_track_dist = INF
#     for sp in range(2):
#         for row in range(2):
#             if visited[sp][row][(2 * n) - 1] != 0:
#                 double_track_dist = min(double_track_dist, visited[sp][row][(2 * n) - 1] - 1)
#
#     if k != 1 and double_track_dist == INF:
#         print(-1)
#         exit(0)
#
#     answer = (double_track_dist - track_dist) * (k - 1) + track_dist
#     print(answer)
