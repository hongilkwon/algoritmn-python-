"""
    소문난 칠공주

    1. 이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
    2. 강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
    3. 화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
    4. 그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 "4명 이상은 반드시 포함"되어 있어야 한다.

    ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수

    * dfs 원리상, 나오면 visited 복원하면, 좃됨.

    4명이 이상이 S(이다솜파)다.

    사고과정.
    25개 중에 7개를 뽑아 확인한다.

"""


# import sys
#
# input = sys.stdin.readline
#
# board = [list(input().rstrip()) for _ in range(5)]
#
# group = []
# cnt = 0
#
# visited = [[0 for _ in range(5)] for _ in range(5)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# def go(start, cnt_y):
#     global cnt, visited
#
#     if len(group) == 7:
#         visited = [[0 for _ in range(5)] for _ in range(5)]
#         s = group[0]
#         visited[s[0]][s[1]] = 1
#         if chk(s) == 7:
#             cnt += 1
#         return
#
#     for i in range(start, 25):
#         r = i // 5
#         c = i % 5
#
#         if board[r][c] == 'Y':
#             if cnt_y + 1 >= 4:
#                 continue
#             group.append((r, c))
#             go(i + 1, cnt_y + 1)
#         else:
#             group.append((r, c))
#             go(i + 1, cnt_y)
#
#         group.pop()
#
#
# def chk(node):
#
#     ret = 1
#     for i in range(4):
#         ny = node[0] + dy[i]
#         nx = node[1] + dx[i]
#
#         if (ny, nx) not in group:
#             continue
#         if visited[ny][nx] == 1:
#             continue
#         visited[ny][nx] = 1
#         ret += chk((ny, nx))
#
#     return ret
#
# if __name__ == '__main__':
#     go(0, 0)
#     print(cnt)