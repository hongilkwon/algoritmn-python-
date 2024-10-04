"""
    구명보트(Greedy, 탐욕, 투포인터)

    한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
    구명보트를 최대한 적게 사용하여 모든 사람을 구출

    1 <= 무인도에 갇힌 사람 <= 50_000
    40 <= 구명보트 무게, 사람의 무게 <=240

    사고과정.

    정렬 -> 가벼운 애들부터 태움.
    그러면 보트의 공간을 최대한 활용 못함.

    투포인터로 양쪽으로 해결한다.
"""


# def solution(people, limit):
#     answer = 0
#
#     people.sort()
#
#     cnt = 0
#     left = 0
#     right = len(people) - 1
#
#     while left <= right:
#         if people[left] + people[right] <= limit:
#             left +=1
#             right -=1
#         else:
#             right -=1
#         cnt += 1
#
#     answer = cnt
#     return answer
#
#
# def solution(people, limit):
#     answer = 0
#
#     people.sort()
#
#     cnt = 0
#     p_cnt = 0
#     w = 0
#     for i in range(len(people)):
#         if p_cnt >= 2 or w + people[i] > limit:
#             cnt += 1
#             p_cnt = 0
#             w = 0
#
#         p_cnt += 1
#         w += people[i]
#
#     if p_cnt != 0:
#         cnt += 1
#
#     answer = cnt
#     return answer