"""
   DFS와 BFS

"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m, s = map(int, input().split())
#
# adj_list = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)
#
# for e in adj_list:
#     e.sort()
#
# visited = [0 for _ in range(n + 1)]
#
# dfs_answer = []
# def dfs(node):
#     if visited[node] == 1:
#         return
#     visited[node] = 1
#
#     dfs_answer.append(node)
#     for next in adj_list[node]:
#         dfs(next)
#
#
# bfs_answer = []
# def bfs(start):
#
#     q = deque()
#     q.append(start)
#     visited[start] = 1
#
#
#     while q:
#         node = q.popleft()
#         bfs_answer.append(node)
#
#         for next in adj_list[node]:
#             if visited[next] == 1:
#                 continue
#
#             visited[next] = 1
#             q.append(next)
#
# if __name__ == '__main__':
#
#     dfs(s)
#     print(*dfs_answer)
#
#     visited = [0 for _ in range(n + 1)]
#     bfs(s)
#     print(*bfs_answer)