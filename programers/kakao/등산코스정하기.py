"""
    등산코스 정하기

    양방향 통행이 가능한 등산로로 연결, 등산로별로 이동하는데 일정 시간이 소요

    쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있으며, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity
    출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 "다시 원래의 출입구"로 돌아오는 등산코스를 정하려고 합니다.

    intensity가 최소가 되도록 등산코스

    출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.

    *intensity가 최소가 되는 등산코스가 여러 개라면 그중 산봉우리의 "번호가 가장 낮은 등산코스"를 선택합니다.
    intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호, intensity의 최솟값


    2 ≤ n ≤ 50_000
    1 ≤ w ≤ 10_000_000

    서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개

    사고과정.

    출입구 <---> 봉우리
    거쳐가는 간선 중 가장 긴것...중 최소값?

    dijkstra
    - 한 정점까지의 최단거리를 확정하고, 다음 간선중 가장 비용을 가진 간선을 이용하여 다음 최단거리를 정한다.

    여러개의 출발점을 가진다.
    산봉우리를 넘어서 탐색하면 안된다.

"""


# import heapq
#
# n, paths, gates, summits = 0, None, None, None
#
# adj_list = []
#
# max_intensity = 10_000_001
# intensity = []
#
#
# def go():
#     global n, paths, gates, summits, adj_list, intensity
#
#     heap = []
#     # 여러 출발점에서 동시에 시작 시킨다.
#     for gate in gates:
#         intensity[gate] = 0
#         heapq.heappush(heap, (0, gate))
#
#     while heap:
#         i, u = heapq.heappop(heap)
#
#         if intensity[u] != i:
#             continue
#
#         for nxt in adj_list[u]:
#             v, w = nxt
#             # 지금 까지 지나온 간선중 intensity의 최대값이 더 작다면,
#             if intensity[v] > max(intensity[u], w):
#                 intensity[v] = max(intensity[u], w)
#                 if v not in summits:
#                     heapq.heappush(heap, (intensity[v], v))
#
#
# def solution(_n, _paths, _gates, _summits):
#     global n, paths, gates, summits, adj_list, intensity
#     n, paths, gates, summits = _n, _paths, _gates, _summits
#
#     adj_list = [[] for _ in range(n + 1)]
#     for path in paths:
#         u, v, w = path
#         adj_list[u].append((v, w))
#         adj_list[v].append((u, w))
#
#     summits = set(_summits)
#     intensity = [max_intensity for _ in range(n + 1)]
#
#     go()
#
#     temp = []
#     for summit in summits:
#         temp.append([summit, intensity[summit]])
#     temp.sort(key=lambda x: (x[1], x[0]))
#     answer = temp[0]
#
#     return answer


if __name__ == '__main__':
    # solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
    solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
