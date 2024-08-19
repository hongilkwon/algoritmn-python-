"""
    광고삽입

    광고효과를 높이기 위해 시청자들이 "가장 많이 보는 구간"에 공익광고를 넣으려고 합니다.

    "죠르디"는 시청자들이 해당 동영상의 어떤 구간을 재생했는 지 알 수 있는 재생구간 기록을 구했고,
    해당 기록을 바탕으로 공익광고가 삽입될 최적의 위치를 고를 수 있었습니다.

    "누적 재생시간"이 가장 많이 나오는 곳에 공익광고를 삽입

    동영상 재생시간 =>
    재생이 종료된 시각 - 재생이 시작된 시각(예를 들어, 00시 00분 01초부터 00시 00분 10초까지 동영상이 재생되었다면, 동영상 재생시간은 9초)

    사고과정.

    최대한 겹치도록...???

    https://driip.me/65d9b58c-bf02-44bf-8fba-54d394ed21e0

    1. 시간의 단위 통일
    2. imos
    3. 윈도우 슬라이싱.
    4. 파이썬 출력 '%02d:%02d:%02d' % (hh:mm:ss)

"""


# import sys
#
# input = sys.stdin.readline
#
#
# def convert_to_second(time):
#     temp = time.split(':')
#     return int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])
#
#
# def convert_to_time(second):
#     h = second // 3600
#     second = second % 3600
#
#     m = second // 60
#     s = second % 60
#     return h, m, s
#
#
# def solution(play_time, adv_time, logs):
#     answer = ''
#     play_second = convert_to_second(play_time)
#
#     # 마킹을 위해 재생시간 +1초
#     play_arr = [0 for _ in range(play_second + 1)]
#
#     # 마킹 (시작 포함, 끝은 포함하지 않음)
#     for log in logs:
#         log_range = log.split('-')
#         start = convert_to_second(log_range[0])
#         end = convert_to_second(log_range[1])
#         play_arr[start] += 1
#         play_arr[end] -= 1
#
#     # 누적 구간합
#     for i in range(1, len(play_arr)):
#         play_arr[i] += play_arr[i - 1]
#
#     window_size = convert_to_second(adv_time)
#     max_idx = 0
#     cur_sum = sum(play_arr[:window_size])
#     max_sum = cur_sum
#
#     # idx   0  1  2  3  4  5
#     #       1  0  0  0  0 -1
#     #       0  1  0 -1  0  0
#     #       0  0  0  0  1 -1
#     #       1  2  2  1  2  0
#
#     for i in range(1, len(play_arr) - window_size):
#         cur_sum -= play_arr[i - 1]
#         cur_sum += play_arr[i + window_size - 1]
#         if cur_sum > max_sum:
#             max_sum = cur_sum
#             max_idx = i
#
#     ret = convert_to_time(max_idx)
#     answer = '%02d:%02d:%02d' % ret
#     # print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution("99:59:59", "00:14:15",
#              ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
