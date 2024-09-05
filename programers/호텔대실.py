"""
    호텔대실(greedy)

"""

# import sys
#
# input = sys.stdin.readline
#
# import heapq
#
#
# def convert(s):
#     temp = s.split(':')
#     return int(temp[0]) * 60 + int(temp[1])
#
#
# def solution(book_time):
#     answer = 0
#
#     converted_book_time = []
#     for time in book_time:
#         s = convert(time[0])
#         e = convert(time[1])
#         converted_book_time.append((s, e))
#
#     converted_book_time.sort(key=lambda x: x[0])
#
#     room_cnt = 0
#     q = []
#
#     for i in range(len(converted_book_time)):
#         # heap이 비어있거나, 방의 사용종료 시간 가장 짧은 방 보다 앞서는 새로운 예약이 있다면, 방을 1개 추가
#         if not q or q[0] > converted_book_time[i][0]:
#             room_cnt += 1
#             heapq.heappush(q, converted_book_time[i][1] + 10)
#             continue
#
#         # 방의 사용종료 시간이 가장 짧은 방 보다 새로운 예약의 사용시작 시간이 이후라면,
#         heapq.heappop(q)
#         heapq.heappush(q, converted_book_time[i][1] + 10)
#
#     return room_cnt
#
#
# if __name__ == '__main__':
#     solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
