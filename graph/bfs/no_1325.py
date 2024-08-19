"""
    효율적 해킹

    한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹
    A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다

    A가 B를 신뢰

    B -> A

    1 <= N <= 10_000,
    1 <= M <= 100_000

    탐색할 때, 시작후 가장 많은 노드를 탐색할 수 있는 노드
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# adj_list = [[] for _ in range(n + 1)]
#
# for i in range(m):
#     v, u = map(int, input().split())
#     adj_list[u].append(v)
#
# visited = []
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 1
#
#     ret = 1
#     while q:
#         node = q.popleft()
#         for next in adj_list[node]:
#             if visited[next] == 0:
#                 visited[next] = 1
#                 q.append(next)
#                 ret += 1
#     return ret
#
#
# if __name__ == '__main__':
#     cnt = [0] * (n + 1)
#     for i in range(n + 1):
#         visited = [0] * (n + 1)
#         cnt[i] = bfs(i)
#
#     max_cnt = max(cnt)
#     for i in range(n + 1):
#         if cnt[i] == max_cnt:
#             print(i, end=" ")
