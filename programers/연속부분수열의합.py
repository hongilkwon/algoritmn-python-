"""
    연속 부분 수열 합의 개수

    원형 수열의 "연속하는 부분 수열의 합"으로 만들 수 있는 수가 모두 몇 가지

    3 ≤ elements의 길이 ≤ 1,000
    1 ≤ elements의 원소 ≤ 1,000

    사고과정 원소의 길이를 보면,
    완전탐색으로 충분히 해결가능해 보인다???

    하지만 1_000 * 1_000 * 1_000 =10억..

    누적합 사용
"""


# def solution(elements):
#     answer = 0
#
#     elements_x2 = elements * 2
#
#     prefix_sum = [0 for _ in range(len(elements_x2))]
#     prefix_sum[0] = elements_x2[0]
#
#     for i in range(1, len(elements_x2)):
#         prefix_sum[i] = prefix_sum[i - 1] + elements_x2[i]
#         # print(*prefix_sum)
#
#     nums = set()
#     for length in range(1, len(elements) + 1):
#         for i in range(len(elements)):
#             sum = prefix_sum[i + length] - prefix_sum[i]
#             nums.add(sum)
#
#     answer = len(nums)
#     return answer

# #시간초과남.
# def solution(elements):
#     answer = 0
#
#     temp = elements * 2
#     nums = set()
#
#     for length in range(1, len(elements)+1):
#         window_size = length
#         for i in range(len(elements)):
#             sum = 0
#             for j in range(i, i + window_size):
#                 sum += temp[j]
#             nums.add(sum)
#     # print(nums)
#     answer = len(nums)
#     return answer