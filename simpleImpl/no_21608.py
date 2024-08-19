"""
    상어 초등학교(시뮬레이션)

    교실은 N×N 크기의 격자로 나타낼 수 있다.
    학교에 다니는 학생의 수는 N^2명이다.


    1  좋아하는 학생이 가장 많이 인접한 칸
    2. 비어있는 칸이 가장 많이 인접 칸
    3. 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸

    학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다

    첫째 줄에 학생의 만족도의 총 합을 출력한다.

    3 ≤ N ≤ 20

    사고과정.

    n의 크기가 크지않다.
    단순구현, 천천히 1명씩 자리에 앉혀본다.

    단순구현인데 생각보다 너무 까다롭다...

    * max(list, key=)

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# students = []
# for i in range(n ** 2):
#     students.append(tuple(map(int, input().split())))
#
# board = [[0 for c in range(n)] for r in range(n)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# if __name__ == '__main__':
#
#     for student in students:
#         temp = [[(0, 0, n, n) for c in range(n)] for r in range(n)]
#
#         s, f1, f2, f3, f4 = student
#         friends = {f1, f2, f3, f4}
#
#         max_friend_cnt = 0
#
#         for r in range(n):
#             for c in range(n):
#                 # 빈자리 라면,
#                 if board[r][c] == 0:
#                     friends_cnt = 0
#                     empty_cnt = 0
#                     for d in range(4):
#                         ny = r + dy[d]
#                         nx = c + dx[d]
#                         if ny < 0 or n <= ny or nx < 0 or n <= nx:
#                             continue
#                         if board[ny][nx] in friends:
#                             friends_cnt += 1
#                         if board[ny][nx] == 0:
#                             empty_cnt += 1
#                     temp[r][c] = (friends_cnt, empty_cnt, r, c)
#                     max_friend_cnt = max(max_friend_cnt, friends_cnt)
#
#         friends_equal = []
#         for r in range(n):
#             for c in range(n):
#                 if temp[r][c][0] == max_friend_cnt:
#                     friends_equal.append(temp[r][c])
#         # 친구숫자로 확정 된다면
#         if len(friends_equal) == 1:
#             fc, ec, r, c = friends_equal[0]
#             board[r][c] = s
#             continue
#
#         max_empty_cnt = max(friends_equal, key=lambda x: x[1])[1]
#         empty_equal = []
#         for e in friends_equal:
#             if e[1] == max_empty_cnt:
#                 empty_equal.append(e)
#         # 빈칸으로 확정 된다면
#         if len(empty_equal) == 1:
#             fc, ec, r, c = empty_equal[0]
#             board[r][c] = s
#             continue
#
#         empty_equal.sort(key=lambda x: (x[2], x[3]))
#         fc, ec, r, c = empty_equal[0]
#         board[r][c] = s
#
#     # for e in board:
#     #     print(*e)
#     # print()
#
#     total_point = 0
#     for r in range(n):
#         for c in range(n):
#             adj = []
#
#             for d in range(4):
#                 ny = r + dy[d]
#                 nx = c + dx[d]
#                 if ny < 0 or n <= ny or nx < 0 or n <= nx:
#                     continue
#                 adj.append(board[ny][nx])
#
#             cnt = 0
#             for student in students:
#                 s, f1, f2, f3, f4 = student
#                 if s == board[r][c]:
#                     friends = {f1, f2, f3, f4}
#                     for f in adj:
#                         if f in friends:
#                             cnt += 1
#             # print(board[r][c], adj, cnt)
#             point = 0
#             if cnt == 1:
#                 point += 1
#             elif cnt == 2:
#                 point += 10
#             elif cnt == 3:
#                 point += 100
#             elif cnt == 4:
#                 point += 1000
#             total_point += point
#     print(total_point)
