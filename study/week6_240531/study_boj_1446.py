"""
    지름길(dp, dijkstra)

   모든 지름길은 일방통행이고, 고속도로를 "역주행할 수는 없다".

   0 <= N <= 12,
   1 <= D <= 10_000

   운전해야 하는 거리의 최솟값

   사고과정.

    예시)
    5 150
    0 50 10 *
    0 50 20
    50 100 10 *
    100 151 10
    110 140 90

    0 --> 50 --> 100 --> 150
    10 + 10 + 50 = 70

    이전 거리까지의 최소값을 통해서 다음 거리의 최소값을 계산할 수 있어 보인다.
    -> dp(tabulation, 상향식)

    2. dijkstra

    u -> v  w
    0 -> 1, 1
    1 -> 2, 1
    2 -> 3, 1
    .
    .
    0 -> 50, 10

"""

## dp 풀이법
# import sys
#
# input = sys.stdin.readline
#
# n, d = map(int, input().split())
#
# short_cut = [tuple(map(int, input().split())) for i in range(n)]
#
# dic = dict()
#
# INF = 1_000_000_000
# table = [INF for _ in range(10_001)]
#
# if __name__ == '__main__':
#
#     for e in short_cut:
#         u, v, w = e
#         if v in dic:
#             dic[v].append((u, w))
#         else:
#             dic[v] = [(u, w)]
#     # print(dic)
#
#     table[0] = 0
#     for i in range(1, len(table)):
#         if i in dic:
#             for e in dic[i]:
#                 u, w = e
#                 table[i] = min(table[i], table[i - 1] + 1, table[u] + w)
#         else:
#             table[i] = min(table[i], table[i - 1] + 1)
#     # print(table)
#     print(table[d])

## dijkstra 풀이법
# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n, d = map(int, input().split())
#
# short_cut = [tuple(map(int, input().split())) for i in range(n)]
#
# adj_list = [[] for _ in range(10_001)]
# for i in range(len(adj_list)-1):
#     adj_list[i].append((i + 1, 1))
# for e in short_cut:
#     u, v, w = e
#     adj_list[u].append((v, w))
#
# INF = 1_000_000_000
# dist = [INF] * 10_001
#
#
# def dijkstra(start):
#     dist[start] = 0
#
#     pq = []
#     heapq.heappush(pq, (0, start))
#
#     while pq:
#         d, u = heapq.heappop(pq)
#         if dist[u] < d:
#             continue
#
#         for next in adj_list[u]:
#             v, w = next
#             if dist[v] > dist[u] + w:
#
#                 dist[v] = dist[u] + w
#                 heapq.heappush(pq, (dist[v], v))
#
#
# if __name__ == '__main__':
#     dijkstra(0)
#     print(dist[d])
