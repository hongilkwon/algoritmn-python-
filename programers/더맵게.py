"""
    더 맵게(힙, 우선순위 큐)

    가장 낮은 두 개의 음식
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

    K 이상이 될 때까지 반복

    모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수
    모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

    2 <= scoville의 길이 <= 1_000_000 100만
    0 <= scoville의 원소 <= 1_000_000

    0<= K <= 1_000_000_000 이하입니다.

"""


# import heapq
#
#
# def solution(scoville, K):
#     answer = 0
#
#     q = scoville
#     heapq.heapify(q)
#
#     cnt = 0
#     while len(q) >= 2 and q[0] < K:
#         num1 = heapq.heappop(q)
#         num2 = heapq.heappop(q)
#         ret = num1 + (2 * num2)
#         heapq.heappush(q, ret)
#         cnt += 1
#
#     if q[0] < K:
#         cnt = -1
#
#     answer = cnt
#     return answer
