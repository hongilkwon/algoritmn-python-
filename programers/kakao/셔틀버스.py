"""
    셔틀버스

"""

import sys

input = sys.stdin.readline

# from collections import deque
#
#
# def convert_to_minute(time):
#     temp = time.split(':')
#     return int(temp[0]) * 60 + int(temp[1])
#
#
# def convert_to_time(minute):
#     h = minute // 60
#     m = minute % 60
#     return h, m
#
#
# def solution(n, t, m, timetable):
#     answer = ''
#
#     bus_times = []
#     start_time = convert_to_minute('09:00')
#     for i in range(n):
#         bus_times.append(start_time + t * i)
#
#     q = []
#     for time in timetable:
#         q.append(convert_to_minute(time))
#     q.sort()
#     q = deque(q)
#
#     last_time = 0
#     for i in range(len(bus_times)):
#         bus_time = bus_times[i]
#
#         if len(bus_times) - 1 == i:
#             # 마지막 버스라면, 마지막 버스에 탈 인원들을 구한다.
#             temp = []
#             for _ in range(m):
#                 if q and q[0] <= bus_time:
#                     temp.append(q.popleft())
#
#             if len(temp) >= m:
#                 # 마지막에 버스에 탈사람들이 정원보다 많다면, index = m-1 번째 사람보다 1분 빨리 오면됨.
#                 last_time = temp[m - 1] - 1
#             else:
#                 # 마지막에 버스에 탈사람들이 정원보다 적다면, 버스 출발시간까지 존버
#                 last_time = bus_time
#         else:
#             # 마지막 버스가 아니라면, 사람들 태워서 보내버림.
#             for _ in range(m):
#                 if q and q[0] <= bus_time:
#                     q.popleft()
#
#     ret = convert_to_time(last_time)
#     answer = '%02d:%02d' % ret
#     print(answer)
#     return answer


if __name__ == '__main__':
    solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
