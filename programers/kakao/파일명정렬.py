"""
    파일명 정렬(문자열, 정렬).

    1. head/number/tail 로 분할.
    2. 커스텀 comparator.
    stable sort

    isalpha() - 알파벳으로만 이루어져있는지
    isdigit() - 오직 0을 포함한 양수형 정수로만 이루어진 문자열"
    isdecimal() - 0~9 사이의 숫자로만 이루어져있는 경우
    isnumberic() -
    배운점.
    생각보다 head, number, tail 나누는게 까다로움.
    파이썬 문자열 기본정렬 - 사전순 오름차순.
    여러 가지 정렬기준으로 정렬하기.
"""

from functools import cmp_to_key


# def separate(s):
#     head, number, tail = '', '', ''
#
#     for i, c in enumerate(s):
#         if c.isdecimal():
#             s = s[i:]
#             break
#         head += c
#
#     for i, c in enumerate(s):
#         if not c.isdecimal():
#             s = s[i:]
#             break
#         number += c
#
#         if i == len(s) - 1:
#             s = ''
#
#     tail = s
#
#     return head, number, tail
#
#
# def solution(files):
#     answer = []
#
#     separate_file = []
#     for s in files:
#         separate_file.append(separate(s))
#
#     separate_file.sort(key=lambda x: (x[0].lower(), int(x[1])))
#
#     for e in separate_file:
#         s = ''.join(e)
#         answer.append(s)
#
#     return answer
