"""
    면접보는 승범이네.

    N개 도시 중 K개의 도시에 면접장을 배치했다. 도시끼리는 단방향 도로로 연결되며,
    거리는 서로 다를 수 있다. 어떤 두 도시 사이에는 도로가 없을 수도, 여러 개가 있을 수도 있다.

    @ 또한 어떤 도시에서든 적어도 하나의 면접장까지 갈 수 있는 경로가 항상 존재한다.

    본인의 도시에서 출발하여 가장 가까운 면접장으로 찾아갈 예정

    가장 먼 도시에서 오는 면접자에게 교통비를 주려고 한다.
    승범이를 위해 면접장까지의 거리가 가장 먼 도시와 그 거리를 구해보도록 하자.


    N(2 ≤ N ≤ 100,000),
    도로의 수 M(1 ≤ M ≤ 500,000),
    면접장의 수 K(1 ≤ K ≤ N)
"""


# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
#
# adjList = [[] for i in range(n + 1)]
#
# # 도착지 --> 출발지
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     adjList[v].append((u, w))
#
# test_spot = list(map(int, input().split()))
#
# INF = 100_000_000_000
# dist = [INF] * (n + 1)
#
#
# def dijkstra():
#     # 시험장 여러 곳을 우선순위큐에 한번에 넣어줌.
#     q = []
#     for s in test_spot:
#         heapq.heappush(q, (0, s))
#         dist[s] = 0
#
#     while q:
#         d, u = heapq.heappop(q)
#
#         if dist[u] < d:
#             continue
#
#         for next in adjList[u]:
#             v, w = next
#             if dist[v] > dist[u] + w:
#                 dist[v] = dist[u] + w
#                 heapq.heappush(q, (dist[v], v))
#
#
# if __name__ == '__main__':
#
#     # 다익스트라 실행
#     dijkstra()
#
#     max_start, max_cost = 0, 0
#
#     for idx, cost in enumerate(dist):
#         if cost > max_cost and cost != int(1e11):
#             max_start, max_cost = idx, cost
#
#     print(max_start)
#     print(max_cost)