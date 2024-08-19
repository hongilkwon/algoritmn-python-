"""
    야근지수

    야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.

    Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다
    Demi가 1시간 동안 작업량 1만큼을 처리

    N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값

    1 <= works의 길이 <= 2000
    1 <= works원소 크기 <= 50_000

    1 <= n <= 1_000_000

    사고과정.
    피로도를 최소화 하려면, 제곱의 크기를 줄여야 하기 때문에
    가장 큰 작업부터 줄여간다.

    우선순위 큐를 사용하여 가장 큰 작업량을 줄이고 0 이상이면 다시 넣어처리한다.
"""

# import sys
# import heapq
# input = sys.stdin.readline
#
#
# def solution(n, works):
#     answer = 0
#
#     q = []
#     for work in works:
#         heapq.heappush(q, (-work, work))
#
#     while n > 0 and q:
#         i, v = heapq.heappop(q)
#         v -= 1
#         if v > 0:
#             heapq.heappush(q, (-v, v))
#         n -= 1
#
#     for i, v in q:
#         answer += v ** 2
#
#     return answer
#
#
# if __name__ == '__main__':
#     solution(4, [4, 3, 3])
