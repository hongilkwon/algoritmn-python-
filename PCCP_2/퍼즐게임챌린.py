"""
    퍼즐 게임 챌린지(이진탐색).

    1. diff ≤ level이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결
    2. diff > level이면, 퍼즐을 틀릴 때마다, time_cur만큼의 시간을 사용하며,

    - 추가로 time_prev만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야 합니다.
    - 이전 퍼즐을 다시 풀 때는 이전 퍼즐의 난이도에 상관없이 틀리지 않습니다.
    - diff - level번 틀린 이후에 다시 퍼즐을 풀면 time_cur만큼의 시간을 사용하여 퍼즐을 해결합니다.


    "1번 틀릴 때마다 (현재 소요 시간 + 이전 문제 소요시간)" + 현재 소요시간.

    제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 "최솟값"

    사고과정
    10^15???
    이진탐색???

    diffs[0] = 1
"""


# import sys
#
# input = sys.stdin.readline
#
# diffs = None
# times = None
# limit = 0
#
# # 현재 level로 limit를 넘지 않고, 모든 퍼즐을 풀 수 있어?
# def chk(level):
#     global diffs, times, limit
#
#     total_time = times[0]
#
#     for i in range(1, len(times)):
#         count = level - diffs[i]
#         if count >= 0:
#             total_time += times[i]
#         else:
#             total_time += (times[i] + times[i - 1]) * (diffs[i] - level) + times[i]
#
#     return total_time <= limit
#
#
# def solution(d, t, l):
#     global diffs, times, limit
#
#     diffs = d
#     times = t
#     limit = l
#
#     answer = 0
#
#     min_level = 1
#
#     left = 1
#     right = max(diffs)
#
#     while left <= right:
#         mid = (left + right) // 2
#         if chk(mid):
#             min_level = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     # print(min_level)
#     answer = min_level
#     return answer
#
#
# if __name__ == '__main__':
#     pass
