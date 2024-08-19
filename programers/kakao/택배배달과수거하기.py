"""
    택배배달과 수거하기
"""


# def cal_len(arr):
#     length = 0
#     for i in range(len(arr) - 1, -1, -1):
#         if arr[i] != 0:
#             length = i + 1
#             break
#     return length
#
#
# def update(arr, length, cap):
#     idx = length - 1
#
#     while cap > 0:
#         if idx < 0:
#             break
#
#         if arr[idx] > 0:
#             cap -= 1
#             arr[idx] -= 1
#
#         while idx >= 0 and arr[idx] == 0:
#             idx -= 1
#     return idx + 1
#
#
# def solution1(cap, n, deliveries, pickups):
#     answer = -1
#
#     delivery_len = cal_len(deliveries)
#     pickup_len = cal_len(pickups)
#
#     time = 0
#     while delivery_len > 0 or pickup_len > 0:
#         # 배달/수거 둘 중 하나라도 남아 있으면 해당 위치까지 왕복해야됨.
#         time += 2 * max(delivery_len, pickup_len)
#
#         delivery_len = update(deliveries, delivery_len, cap)
#         pickup_len = update(pickups, pickup_len, cap)
#         # print()
#         # print("delivery_len", delivery_len, "deliveries", *deliveries)
#         # print("pickup_len", pickup_len, "pickups", *pickups)
#
#     answer = time
#     # print(answer)
#     return answer

# def solution2(cap, n, deliveries, pickups):
#     answer = -1
#
#     time = 0
#     delivery_cnt = 0
#     pickup_cnt = 0
#
#     for i in range(n - 1, -1, -1):
#         delivery_cnt += deliveries[i]
#         pickup_cnt += pickups[i]
#
#         while delivery_cnt > 0 or pickup_cnt > 0:
#             delivery_cnt -= cap
#             pickup_cnt -= cap
#             time += (i + 1) * 2
#
#     answer = time
#     return answer