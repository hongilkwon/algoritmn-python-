"""
    아이템 줍기

    다각형의 둘레(굵은 선)를 따라서 이동
    중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로

    * x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.
    * 같이 지형이 2개 이상으로 분리된 경우 없음
    * 다른 직사각형 안에 완전히 포함되는 경우 또한 없음.

    캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리

    사고과정.

    어떻게? 주어진 사각형들을 통해 경로를 만들까???
    [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태

    처음에는 그냥 사각형의 모든 점을 포함해서 돌아도 최단거리가 구해질 줄 알았다. 하지만 아니였다.
    사고에 실수가 있었다.

    분명 테두리만 남겨야 하는데..문제는 테두리만 남겨도 쉽지 않다.

    해설링크.
    https://velog.io/@leeeeeyeon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0

    프로그래머스문제라 많이 조잡한 문제이다.
"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# board = [[0 for c in range(102)] for r in range(102)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# visited = [[0 for c in range(102)] for r in range(102)]
#
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#
#     while q:
#         node = q.popleft()
#         y = node[0]
#         x = node[1]
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if board[ny][nx] == 0 or board[ny][nx] == 2:
#                 continue
#             if visited[ny][nx] > 0:
#                 continue
#             visited[ny][nx] = visited[y][x] + 1
#             q.append((ny, nx))
#
#
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
#
#     for e in rectangle:
#         # x1, y1, x2, y2 = e
#         x1, y1, x2, y2 = map(lambda x: x * 2, e)
#         for r in range(y1, y2 + 1):
#             for c in range(x1, x2 + 1):
#                 # 사각형의 내부면 2로 채움.
#                 if y1 < r < y2 and x1 < c < x2:
#                     board[r][c] = 2
#                 # 다른 직사각형의 내부가 아니고, 테두리면 1로 채움
#                 elif board[r][c] != 2:
#                     board[r][c] = 1
#
#     # for line in board:
#     #     print(*line)
#
#     bfs((characterY * 2, characterX * 2))
#     answer = (visited[itemY * 2][itemX * 2] - 1) // 2
#     print(answer)
#     return answer


# if __name__ == '__main__':
#     solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8, )
