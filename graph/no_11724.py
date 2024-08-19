"""
    연결 요소의 개수

"""

# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# adj_list = [[] for r in range(n + 1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)
#
# visited = [0] * (n + 1)
#
#
# def dfs(node):
#     visited[node] = 1
#
#     for next_node in adj_list[node]:
#         if visited[next_node] == 1:
#             continue
#         dfs(next_node)
#
#
# if __name__ == '__main__':
#     cnt = 0
#     for node in range(1, n + 1):
#         if visited[node] == 0:
#             dfs(node)
#             cnt += 1
#     print(cnt)
