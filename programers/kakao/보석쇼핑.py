"""
    보석쇼핑

    특정 범위의 물건들을 모두 싹쓸이 구매하는 습관
    진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

    모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수
    시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며,
    만약 가장 짧은 구간이 여러 개라면 "시작 진열대 번호가 가장 작은 구간"을 return 합니다.

     1 <= gems <= 100_000

     사고과정
     배열의 특정한 구간을 정한다???
     투포인터?

     일단, 배열에 들어 있는 보석이 몇 종류인지 확인한다.
     어떻게 포인터를 움직일 것인가??

     1. end - 모든 종류의 보석을 포함할 떄 까지 증가
     2. start - 모든 종류의 보석을 포함를 유지하며 증가하여, 범위를 줄여가면서, 최소범위 구함.

     배울점
     from collections import Counter
     대해서 공부한다.
"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(gems):
#     answer = []
#
#     cnt_gems_type = len(set(gems))
#     cnt_dic = dict()
#     start = 0
#
#     min_range = len(gems)
#     for end in range(len(gems)):
#         gem = gems[end]
#         if gem in cnt_dic:
#             cnt_dic[gem] += 1
#         else:
#             cnt_dic[gem] = 1
#
#         # 모든 보석이 적어도 1개 이상으로 범위에 들어온 다면.
#         while len(cnt_dic) == cnt_gems_type:
#             # 최소 범위 갱신
#             if min_range > end - start:
#                 min_range = end - start
#                 answer = [start + 1, end + 1]
#
#             if cnt_dic[gems[start]] > 0:
#                 cnt_dic[gems[start]] -= 1
#                 # key 제거
#                 if cnt_dic[gems[start]] == 0:
#                     del cnt_dic[gems[start]]
#             start += 1
#     return answer


if __name__ == '__main__':
    solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
