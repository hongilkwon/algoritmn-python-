"""
    선수과목(위상정렬)

    과목의 수 N(1 ≤ N ≤ 1_000)
    선수 조건의 수 M(0 ≤ M ≤ 500_000)

    노드를 위상정렬할 때,
    각 노드들이 어떤 그룹에 속하는지 까지 구하는 문제.
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# adj_list = [[] for i in range(n + 1)]
# in_degree = [0 for _ in range(n + 1)]
#
# for i in range(m):
#     u, v = map(int, input().split())
#     adj_list[u].append(v)
#     in_degree[v] += 1
#
# is_cycle = False
# order = []
#
#
# def topology_sort():
#     q = deque()
#
#     for i in range(1, n + 1):
#         if in_degree[i] == 0:
#             q.append((i, 1))
#
#     for _ in range(1, n + 1):
#         if not q:
#             global is_cycle
#             is_cycle = True
#             return
#
#         node = q.popleft()
#         order.append(node)
#
#         idx = node[0]
#         term = node[1]
#
#         for next in adj_list[idx]:
#             in_degree[next] -= 1
#
#             if in_degree[next] == 0:
#                 q.append((next, term + 1))
#
#
# if __name__ == '__main__':
#
#     topology_sort()
#     # print(is_cycle)
#     # print(order)
#
#     answer = [0] * n
#     for e in order:
#         idx = e[0]-1
#         term = e[1]
#         answer[idx] = term
#
#     print(*answer)



