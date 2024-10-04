"""
    숫자변환하기(dp, bfs+백트레킹)
"""

##bfs + backtracking
# from collections import deque
#
#
# x = 0
# y = 0
# n = 0
#
# visited = [0 for _ in range(1_000_001)]
#
# def bfs(start):
#     global x, y, n, visited
#
#     q = deque()
#     q.append((start, 0))
#     visited[start] = 1
#
#     while q:
#         node, cnt = q.popleft()
#
#         if node == y:
#             return cnt
#
#         for nxt in (node+n, node*2, node*3):
#             if nxt > y:
#                 continue
#             if visited[nxt] == 1:
#                 continue
#
#             q.append((nxt, cnt+1))
#             visited[nxt] = 1
#
#     return -1
#
#
# def solution(i_x, i_y, i_n):
#     answer = 0
#     global x, y, n, visited
#     x = i_x
#     y = i_y
#     n = i_n
#
#     answer = bfs(x)
#     print(answer)
#     return answer
#
# # DP풀이
# x = 0
# y = 0
# n = 0
#
# INF = 1_000_001
#
#
#
# def solution(x, y, n):
#     answer = 0
#
#     table = [INF for _ in range(y+1)]
#     table[x] = 0
#
#     for i in range(x, y+1):
#         if i % 3 == 0:
#             table[i] = min(table[i // 3] + 1, table[i])
#         if i % 2 == 0:
#             table[i] = min(table[i // 2] + 1, table[i])
#         if i - n >= 0:
#             table[i] = min(table[i - n] + 1, table[i])
#
#     if table[y] == INF:
#         answer = -1
#     else:
#         answer = table[y]
#
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     pass
