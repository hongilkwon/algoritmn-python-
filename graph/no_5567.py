"""
    결혼식(bfs, dfs)

    친구의 친구 거리가 2인 노드의 갯수
    bfs가 더 적합하다.

"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# adj_list = [list() for _ in range(n + 1)]
#
# for _ in range(m):
#     u, v = map(int, input().split(' '))
#     adj_list[u].append(v)
#     adj_list[v].append(u)
#
# visited = [False for _ in range(n + 1)]
#
# cnt = 0
#
# def bfs(start):
#     global cnt
#     q = deque()
#     q.append((start, 0))
#     visited[start] = True
#
#     while q:
#         node, level = q.popleft()
#         # 친구 또는 친구의 친구
#         if level == 1 or level == 2:
#             cnt += 1
#
#         for nxt in adj_list[node]:
#             if visited[nxt]:
#                 continue
#             visited[nxt] = True
#             q.append((nxt, level+1))
#
#
# def dfs(node, level):
#     global cnt
#
#     visited[node] = True
#
#     if level >= 2:
#         return
#
#     for nxt in adj_list[node]:
#
#         dfs(nxt, level + 1)
#
#
# if __name__ == '__main__':
#     dfs(1, 0)
#     print(visited.count(True)-1)
