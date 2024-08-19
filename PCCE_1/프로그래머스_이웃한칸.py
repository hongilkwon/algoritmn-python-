"""
    [PCCE 기출문제] 9번 이웃한 칸

"""

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def solution(board, h, w):
#     answer = 0
#     color = board[h][w]
#     for i in range(4):
#         nh = h + dy[i]
#         nw = w + dx[i]
#
#         if nh < 0 or nh >= len(board) or nw < 0 or nw >= len(board[0]):
#             continue
#
#         if board[nh][nw] == color:
#             answer += 1
#     return answer
