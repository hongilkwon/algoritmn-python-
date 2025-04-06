"""
    트럭

    n = 트럭의 개수,
    w 대의 트럭만 동시에 올라갈 수 있다
    트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

    모든 트럭들이 다리를 건너는 최단시간을 출력

    1번 풀이
    모든 트럭이 다리를 건너면 종료됨!
    => 다리의 무게가 0
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, w, l = map(int, input().split(' '))
#
# truck = deque(map(int, input().split(' ')))
#
# bridge = deque([0 for _ in range(w)])
#
# if __name__ == '__main__':
#     flag = True
#     time = 0
#
#     while flag:
#         # 1초 증가.
#         time += 1
#         # 다리 가장 앞에 있는 트럭 건너기
#         bridge.popleft()
#
#         if truck:
#         # 대기 트럭이 남아 있다면,
#             if sum(bridge) + truck[0] <= l:
#                 bridge.append(truck.popleft())
#             else:
#                 bridge.append(0)
#         else:
#         # 대기 트럭이 없다면,
#             bridge.append(0)
#
#         if sum(bridge) == 0:
#             flag = False
#
#     print(time)