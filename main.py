"""
    디펜스 게임(greedy)

    남은 병사의 수보다 현재 라운드의 적의 수가 더 많으면 게임이 종료
    무적권을 사용하면 병사의 소모없이 한 라운드의 공격을 막을 수 있습니다.

    "몇 라운드까지 막을 수 있는지"

    1 ≤ n ≤ 1_000_000_000(10억)
    1 ≤ enemy의 길이 ≤ 1_000_000

    사고과정.

    - 적이 순서대로 나온다는 것.--> enemy에 정렬같은 행위를 해서는 안된다.
    - 최대한 적의 숫자가 많을 때, 사용하는 것이 좋다.

    결론: 순서대로 나오는 적들중에 최대한 적의 숫자가 많을때 무적권을 사용해야 된다!

    로직
    일단, 현재 보유병사로 막는다.
    그러다 보면, 언젠가는 현재 보유병사로 막을 수 없을 경우가 오거나, 모든 병사를 막는다.
    이때, 보유병사로 더 이상 막을 수 없다면,
    -> 과거에 "내가 막은 적중에 가장 큰 적"을 무적권을 사용하여, 대체 하고 병사를 부활 시킨다.

"""

# import sys
# import heapq
#
#
# def solution(n, k, enemy):
#     answer = 0
#
#     pq = []
#     for i in range(len(enemy)):
#         if n >= enemy[i]:
#             n -= enemy[i]
#             heapq.heappush(pq, (-enemy[i], enemy[i]))
#         elif k > 0:
#             if pq and enemy[i] <= pq[0][1]:
#                 n += (heapq.heappop(pq)[1] - enemy[i])
#                 heapq.heappush(pq, (-enemy[i], enemy[i]))
#             k -= 1
#         else:
#             answer = i
#             break
#         answer = i + 1
#     return answer
#
#
# if __name__ == '__main__':
#     ret = solution(10, 2, [8, 6, 5, 3, 2])
#     print(ret)

