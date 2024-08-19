"""
    플로이드

    시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

    map(function, iterable)

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# INF = 1000_000_000
#
# dist = [[INF for j in range(n + 1)] for i in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             dist[i][j] = 0
#
# for i in range(m):
#     u, v, w = map(int, input().split())
#     #  시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
#     dist[u][v] = min(dist[u][v], w)
#
#
# def floyd():
#     for k in range(1, n + 1):
#         for a in range(1, n + 1):
#             for b in range(1, n + 1):
#                 dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
#
#
# if __name__ == '__main__':
#     floyd()
#
#     for i in range(1, n + 1):
#         line = []
#         for j in range(1, n + 1):
#             if dist[i][j] == INF:
#                 line.append(0)
#             else:
#                 line.append(dist[i][j])
#         print(' '.join(map(str, line)))
