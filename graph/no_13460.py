"""
    구슬탈출2

    빨간 구슬을 구멍을 통해서 빼내는 것이다.
    이때, "파란 구슬이 구멍에 들어가면 안 된다".

    왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능

    빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다
    빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.

    빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
    기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.


    최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력

    사고과정.

    최단거리- bfs, 시작점이 2개인 것에 초점을 맞춰서 해결을 하려다보니,
    문제의 핵심을 잘못 짚었음.

    구슬이 2개!
    최단거리가 아니라 이동횟수에 제한을 둔것.

    재귀 + 백트레킹

"""

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# board = [list(input().rstrip()) for _ in range(n)]
#
# point_red, point_blue, goal = None, None, None
# for r in range(n):
#     for c in range(m):
#         if board[r][c] == 'R':
#             point_red = (r, c)
#         if board[r][c] == 'B':
#             point_blue = (r, c)
#         if board[r][c] == 'O':
#             goal = (r, c)
#
# visited = set()
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# min_cnt = 11
#
#
# def move(dir, point):
#     y, x = point
#     back = -1
#
#     # board의 최대 크기가 10
#     cnt = 0
#     while True:
#         cnt += 1
#         y = y + dy[dir]
#         x = x + dx[dir]
#
#         if board[y][x] == "#":
#             cnt += back
#             break
#         if board[y][x] == "O":
#             break
#         # 다른 공을 지나간 한 칸더 뒤에 멈춘다.
#         if board[y][x] == "R" or board[y][x] == "B":
#             back -= 1
#     return cnt
#
#
# def go(cnt, red, blue):
#     global min_cnt
#
#     if (red, blue) in visited:
#         return
#     visited.add((red, blue))
#
#     # if min_cnt <= cnt:
#     #     return
#
#     if cnt > 10:
#         return
#
#     if red == goal:
#         min_cnt = min(min_cnt, cnt)
#         print('cnt:', cnt)
#         for e in board:
#             print(*e)
#         print()
#         return
#
#     for i in range(4):
#         r_go = move(i, red)
#         b_go = move(i, blue)
#
#         if r_go == 0 and b_go == 0:
#             continue
#
#         n_red = (red[0] + dy[i] * r_go, red[1] + dx[i] * r_go)
#         n_blue = (blue[0] + dy[i] * b_go, blue[1] + dx[i] * b_go)
#
#         if n_blue == goal:
#             continue
#         if n_red == goal:
#             min_cnt = min(min_cnt, cnt)
#             return
#
#         board[red[0]][red[1]] = '.'
#         board[blue[0]][blue[1]] = '.'
#         board[n_red[0]][n_red[1]] = 'R'
#         board[n_blue[0]][n_blue[1]] = 'B'
#
#         go(cnt + 1, n_red, n_blue)
#
#         # 원복
#         # 주의점, 만약 R B 둘 중에 하나만 움직였을 경우, 아래와 같이 코드를 작성하면,
#         # 움직이지 않은 점은 '.'으로 할당 된다
#         # board[red[0]][red[1]] = 'R'
#         # board[blue[0]][blue[1]] = 'B'
#         # board[n_red[0]][n_red[1]] = '.'
#         # board[n_blue[0]][n_blue[1]] = '.'
#
#         board[n_red[0]][n_red[1]] = '.'
#         board[n_blue[0]][n_blue[1]] = '.'
#         board[red[0]][red[1]] = 'R'
#         board[blue[0]][blue[1]] = 'B'
#
#
# if __name__ == '__main__':
#
#     go(1, point_red, point_blue)
#
#     if min_cnt == 11:
#         print(-1)
#     else:
#         print(min_cnt)
