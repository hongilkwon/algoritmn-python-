"""
    1. 10초 전 이동
    - prev

    2. 10초 후 이동
    - next

    3. 오프닝 건너뛰기.
    - "자동"으로 오프닝이 끝나는 위치로 이동합니다.

    사고과정. 단순구현

    마지막으로 하번더 오프닝 체크
    시간 변환 주의


    answer = '%02d:%02d' %  (time // 60, time % 60)
"""


# import sys
#
# input = sys.stdin.readline
#
# c_video_len = 0
# c_pos = 0
# c_op_start = 0
# c_op_end = 0
#
#
# def convert(s):
#     temp = s.split(':')
#     return int(temp[0]) * 60 + int(temp[1])
#
#
# def is_op_range(time):
#     if c_op_start <= time <= c_op_end:
#         return True
#     else:
#         return False
#
#
# def solution(video_len, pos, op_start, op_end, commands):
#     answer = ''
#     global c_video_len, c_pos, c_op_start, c_op_end
#
#     c_video_len = convert(video_len)
#     c_pos = convert(pos)
#     c_op_start = convert(op_start)
#     c_op_end = convert(op_end)
#
#     for c in commands:
#         if is_op_range(c_pos):
#             c_pos = c_op_end
#
#         if c == 'prev':
#             c_pos = max(0, c_pos - 10)
#
#         if c == 'next':
#             c_pos = min(c_video_len, c_pos + 10)
#
#     if is_op_range(c_pos):
#         c_pos = c_op_end
#
#     ret = (c_pos // 60, c_pos % 60)
#     answer = '%02d:%02d' % ret
#     # print(answer)
#     return answer
#
# if __name__ == '__main__':
#     pass
