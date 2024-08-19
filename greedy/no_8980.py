"""
    택배

     본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
     박스들은 모두 크기가 같다.
     트럭에 최대로 실을 수 있는 박스의 개수, 즉 "트럭의 용량"이 있다.
     이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송

    조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
    조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
    조건 3: 박스들 중 일부만 배송할 수도 있다.

    2 <= n <= 2_000
    1 <= c <= 10_000
    1 <= m <= 10_000

    사고과정.

    그리디인가???

    단순하게 최대한 많이 배송 하려면,
    "가장 앞에서" 받아서 가장 "가까운 도착지"에 내려준다..?
    단, 너무 앞쪽 마을에서 가장 뒤에 있는 마을의 택배를 받는다면? 비 효율적임.

    "도착지가 가까운걸 받아야됨"

    몇개의 택배를 가지고 갈 수 있지???
    C개를 넘어서는 가지고 갈 수가 없다.

    트럭이 지나가는 마을에 상한선중 가장 작은값 보다 작아야 된다.
    box_cnt = min(w, min(truck_state[u:v]))

    택배는 U 마을부터 V-1 마을 까지 해당 택배를 가지고 있어야 한다.
    따라서 box_info 를 탐색할 때, truck_state[u:v]에서 가지고 가야할 택배의 갯수를 제외함.

    매우 어려운 문제..

    배울점.
    - 상한선을 정하는 배열을 만들어서 카운팅을 한다
    - 정렬?, 우선순위큐?
"""


# import sys
#
# input = sys.stdin.readline
#
# n, c = map(int, input().split())
# m = int(input())
#
# box_info = []
# for i in range(m):
#     u, v, w = map(int, input().split())
#     box_info.append((u, v, w))
#
# if __name__ == '__main__':
#
#     box_info.sort(key=lambda x: x[1])
#
#     # 각 마을 마다 트럭이 담을 수 있는 상자의 개수는 최대 c개이다.
#     # [40, 40, 40, 40, 40, 40, 40]
#     truck_upper_bound = [c] * (n + 1)
#
#     # 배달한 택배의 갯수
#     total_cnt = 0
#     for e in box_info:
#         print(e)
#
#     for u, v, w in box_info:
#         # 목적지까지 이동하기 전까지 현재의 몇개의 택배를 트럭에 담고갈 수 있는지 확인한다.
#         reserved_box = min(truck_upper_bound[u:v])
#         box_cnt = min(w, reserved_box)
#
#         # 단 1개라도 담을 수 있다면,
#         if box_cnt > 0:
#             for i in range(u, v):
#                 truck_upper_bound[i] -= box_cnt
#             total_cnt += box_cnt
#
#     print(total_cnt)