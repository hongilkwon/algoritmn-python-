"""
    선입 선출 스케쥴링

    CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 "시간이 다릅"니다.
    한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행
    2개 이상의 코어가 남을 경우 "앞의 코어"부터 작업을 처리 합니다.

    "마지막 작업"을 처리하는 코어의 번호를 return

    2 <= 코어의 수 <= 10_000
    1 <= 코어당 작업을 처리하는 시간 <= 10_000
    1 <= n(일의 개수) <= 50_000

    사고과정.

    예시)
    시작       1, 2, 3,    3개
    1시간 후    1,         1개
    2시간 후    1, 2       2개


    시간 단위로 반복?

    10_000 * 10_000 = 100_000_000 (1억)
    아슬아슬하게 가능할지도 모른다.
    -> 정확성만 통과 / 효율성 전부 실패

    이분탐색

    n개 이상의 작업을 하는 최소 시간은 이분탐색을 이용한다.
    최소 시간을 찾았다면 최소 시간 m때 작업을 시작하는 코어를 찾고,
    그 때 몇 번째 코어가 n번째 작업을 시작하는지 찾아 return 한다.
"""


# n = 0
# cores = []
#
#
# # 해당 시간으로 모든 일을 작업량을 처리 할수 있는지 확인한다.
# def check(time):
#     global n, cores
#
#     # 0초에 동시에 코어에 진입한다고 가정한다.
#     amount = len(cores)
#
#     for core in cores:
#         amount += (time // core)
#
#     flag = amount >= n if True else False
#     return flag, amount
#
#
# def solution(_n, _cores):
#     answer = 0
#     global n, cores
#     n, cores = _n, _cores
#
#     # 코어가 작업의 갯수 보다 충분한 경우.
#     if n <= len(cores):
#         return n
#
#     # 시간을 기준으로 이분탐색을 실시한다! (시간은 언제나 정렬되어 있다)
#     time, throughput = 0, 0
#     left = 1
#     right = max(cores) * n
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         is_possible, amount = check(mid)
#         if is_possible:
#             time = mid
#             throughput = amount
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     print(time, throughput)
#
#     # 최소시간 동안 처리량 - 전체 처리 해야될 일(n)
#     throughput -= n
#
#     # cores 처리량을 뒤에서 부터 순회 (core를 순차로 사용하기 때문에)
#     for i in range(len(cores) - 1, -1, -1):
#         # time % cores[i] 해당 코어의 처리량으로 나누어 떨어진다? -> 해당 코어로 작업을 처리헀다.
#         if time % cores[i] == 0:
#             if throughput == 0:
#                 answer = i + 1
#                 break
#             throughput -= 1
#
#     print(answer)
#     return answer


# 시간초과
# def solution(n, cores):
#     answer = 0
#
#     throughput = n
#     flag = False
#
#     for time in range(10_001):
#         for idx, core_time in enumerate(cores):
#             if time % core_time == 0:
#                 # print(idx, core_time)
#                 n -= 1
#             if n == 0:
#                 flag = True
#                 answer = idx+1
#                 break
#         if flag:
#             break
#     return answer
#
# if __name__ == '__main__':
#     solution(6, [1, 2, 3])
