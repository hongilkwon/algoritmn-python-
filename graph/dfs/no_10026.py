"""

    적록색약(dfs, connected component)

    1 ≤ N ≤ 100

    사고과정
    기본 그래프 탐색문제
    연결된 컴포넌트를 찾는 문제인데 2개의 영역을 1개로 세어야 한다.
    탐색을 시작한 색깔에 따라서 다음 탐색을 이어갈지 안할지 결정한다.

    배울점
    어려운 문제는 아니나 다음 탐색을 할 기준을 변경하는 문제이다.

"""

# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# input = sys.stdin.readline
#
# n = int(input())
# map = [list(input().strip()) for row in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# visited = [[0 for col in range(n)] for row in range(n)]
#
# colors = []
# def dfs(y, x):
#
#     if visited[y][x]:
#         return
#     visited[y][x] = 1
#
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#
#         if 0 > ny or ny >= n or 0 > nx or nx >= n:
#             continue
#         if map[ny][nx] in colors:
#             dfs(ny, nx)
#
# if __name__ == '__main__':
#
#     cnt1 = 0
#     visited = [[0 for col in range(n)] for row in range(n)]
#     for r in range(n):
#         for c in range(n):
#             if visited[r][c] == 0:
#                 colors = [map[r][c]]
#                 dfs(r, c)
#                 cnt1 += 1
#
#     cnt2 = 0
#     visited = [[0 for col in range(n)] for row in range(n)]
#     for r in range(n):
#         for c in range(n):
#             if visited[r][c] == 0:
#                 colors = ['R', 'G'] if map[r][c] == 'R' or map[r][c] == 'G' else ['B']
#                 dfs(r, c)
#                 cnt2 += 1
#     print(cnt1, cnt2)
