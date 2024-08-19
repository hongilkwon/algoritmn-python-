"""
    2016년(단순구현)
    1월 1일은 금요일
"""


# def solution(a, b):
#     answer = ''
#
#     month_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#
#     cnt_days = b
#     for m in range(1, a):
#         cnt_days += month_dict[m]
#
#     weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
#     answer = weeks[cnt_days % 7]
#     return answer
ㅇ