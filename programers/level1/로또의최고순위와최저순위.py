"""
    로또의 최고순위와 최저순위 (단순구현)
"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(lottos, win_nums):
#     answer = []
#
#     cnt = 0
#     zero_cnt = 0
#     for num in lottos:
#         if num in win_nums:
#             cnt += 1
#         if num == 0:
#             zero_cnt += 1
#
#     rank_dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
#
#     max_rank = rank_dict[cnt + zero_cnt]
#     min_rank = rank_dict[cnt]
#
#     answer = [max_rank, min_rank]
#     print(answer)
#     return answer
#
# if __name__ == '__main__':
#     pass
