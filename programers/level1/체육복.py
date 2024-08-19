"""
    체육복

    학생들의 번호는 체격 순으로 매겨져 있어,
    바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.

    최대한 많은 학생이 체육수업을 들어야 합니다.

    사고과정.

    체육복을 빌려줄 수 있는 학생 기준으로 최대한 자신보다 앞번호에게 빌려줘야,
    이후에 다른 체육복을 가진 친구가 더 빌려 줄 수 있음.

    여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에     다른 학생에게는 체육복을 빌려줄 수 없습니다.
"""


# def solution(n, lost, reserve):
#     answer = 0
#
#     reserve_set = set(reserve) -set(lost)
#     lost_set = set(lost) - set(reserve)
#
#     cnt = n - len(lost_set)
#
#     for i in reserve_set:
#         if i - 1 in lost_set:
#             lost_set.remove(i - 1)
#             cnt += 1
#             continue
#
#         if i + 1 in lost_set:
#             lost_set.remove(i + 1)
#             cnt += 1
#             continue
#
#     answer = cnt
#     return answer
#
#
# if __name__ == '__main__':
#     solution(5, [2, 4], [1, 3, 5])
#