"""
    인사고과
"""

"""
    인사고과(정렬, stable sort)

    근무태도 점수 / 동료평가 점수 임의 사원보다 "모두" 낮은 경우 인센티브가 없다.

    1. 두 점수의 합이 높은 순,
    2. 점수가 같은면 동석차 

    완호의 "석차"를 출력하자.
    완호가 인센티브를 받지 못하는 경우 -1

    1 ≤ scores의 길이 ≤ 100_000

    사고과정.

    엣지 케이스
    완호 보다 점수는 높은데, 인센티브를 받을 수 없는 사람이 있다.

    예 - [[2,3], [1,10], [2,11]]
    answer = 2

    예 - [[3,5], [1,10], [2,9], [1,9], [3,11]]
    answer = 3

    근무태도를 내림차순으로 정렬한다. 같은 근무태도 점수에서는 동료 평가 점수를 오름차순으로 정렬
    [3,5]

    [[3,11], [2,9], [1,9], [1,10]]
"""


# def solution(scores):
#     answer = 0
#
#     rank = 1
#     ho = scores[0]
#     ho_sum = sum(ho)
#
#     scores = scores[1:]
#     scores.sort(key=lambda x: (-x[0], x[1]))
#
#     max_peer_point = 0
#     for i in range(0, len(scores)):
#         work_point, peer_point = scores[i]
#
#         # 2개의 점수가 모두 완호보다 높으면 완호는 인센티브 받지 못함.
#         if ho[0] < work_point and ho[1] < peer_point:
#             rank = -1
#             break
#
#             # 근무점수로 내림정렬되어 있고, 동료점수로 오름 차순이라면,
#         # 반복문이 진행되면 근무점수는 같거나 작아지고, 동료점수가 최대값을 기준을 갱신하여 그것보다 커야만 인센티브를 받는 직원임.
#         if max_peer_point <= peer_point:
#             if ho_sum < work_point + peer_point:
#                 rank += 1
#             max_peer_point = peer_point
#
#     answer = rank
#     return answer
