"""
    석유시추(dfs)

    1 <= n,m <= 500

    사고과정

    1. 완전탐색

    - connected component 응용문제로 그렇게 어렵지는 않다.
    - 컴포넌트의 사이즈를 구별하여 최대값을 구하는것.

"""

# import sys
# sys.setrecursionlimit(10**8)
#
# n = 0
# m = 0
# land = []
# resourceSize = []
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# visited = []
#
#
# def dfs(node, result):
#     ret = 1
#
#     for i in range(4):
#         ny = node[0] + dy[i]
#         nx = node[1] + dx[i]
#         if ny < 0 or ny >= n or nx < 0 or nx >= m:
#             continue
#         if visited[ny][nx] == 1:
#             continue
#         if land[ny][nx] == 0:
#             continue
#
#         visited[ny][nx] = 1
#         result.append((ny, nx))
#         ret += dfs((ny, nx), result)
#
#     return ret
#
#
# def solution(l):
#     global n
#     global m
#     global land
#     global resourceSize
#     global visited
#
#     n = len(l)
#     m = len(l[0])
#     for i in range(n):
#         land.append(l[i])
#
#     resourceSize = [[0 for col in range(m)] for row in range(n)]
#     visited = [[0 for col in range(m)] for row in range(n)]
#
#     label = 1
#     label_dic = dict()
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j] == 0 and land[i][j] == 1:
#                 visited[i][j] = 1
#                 result = [(i, j)]
#                 size = dfs((i, j), result)
#                 for e in result:
#                     resourceSize[e[0]][e[1]] = label
#                 label_dic[label] = size
#                 label += 1
#
#     # for e in resourceSize:
#     #     print(e)
#
#     max_res = 0
#     s = set()
#     for col in range(m):
#         for row in range(n):
#             if resourceSize[row][col] == 0:
#                 continue
#             s.add(resourceSize[row][col])
#         sum = 0
#         for key in s:
#             sum += label_dic[key]
#         max_res = max(max_res, sum)
#         s.clear()
#
#     # print(max_res)
#     answer = max_res
#     return answer


# if __name__ == '__main__':
#     solution(
#         [[0, 0, 0, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 1, 1, 0, 0],
#          [1, 1, 0, 0, 0, 1, 1, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0],
#          [1, 1, 1, 0, 0, 0, 1, 1]]
#     )
#     solution(
#         [[1, 0, 1, 0, 1, 1],
#          [1, 0, 1, 0, 0, 0],
#          [1, 0, 1, 0, 0, 1],
#          [1, 0, 0, 1, 0, 0],
#          [1, 0, 0, 1, 0, 1],
#          [1, 0, 0, 0, 0, 0],
#          [1, 1, 1, 1, 1, 1]]
#     )
