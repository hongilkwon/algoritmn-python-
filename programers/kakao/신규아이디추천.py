"""
    신규아이디추천

    단순구현 문제.
"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(new_id):
#     answer = ''
#
#     # 1단계
#     step_1 = ''
#     for c in new_id:
#         step_1 += c.lower()
#     # print('step_1', step_1)
#
#     # 2단계
#     step_2 = ''
#     for c in step_1:
#         if c.islower() or c.isdecimal() or c in ['-', '_', '.']:
#             step_2 += c
#     # print('step_2', step_2)
#
#     # *3단계
#     step_3 = step_2[0]
#     prev = step_2[0]
#     for i in range(1, len(step_2)):
#         c = step_2[i]
#         if c != '.':
#             step_3 += c
#
#         if c == '.':
#             if prev != '.':
#                 step_3 += c
#         prev = c
#     # print('step_3', step_3)
#
#     # 4단계
#     step_4 = step_3
#     if len(step_4) >= 2:
#         if step_4[0] == '.':
#             step_4 = step_4[1:]
#         if step_4[-1] == '.':
#             step_4 = step_4[:-1]
#     elif len(step_4) == 1 and step_4 == '.':
#         step_4 = ''
#     # print('step_4', step_4)
#
#     # 5단계
#     step_5 = step_4
#     if step_5 == '':
#         step_5 = 'a'
#     # print('step_5', step_5)
#
#     # 6단계
#     step_6 = step_5
#     if len(step_6) >= 16:
#         step_6 = step_6[:15]
#         if step_6[-1] == '.':
#             step_6 = step_6[:-1]
#     # print('step_6', step_6)
#
#     # 7단계
#     step_7 = step_6
#     last_c = step_7[-1]
#     while len(step_7) <= 2:
#         step_7 += last_c
#     print('step_7', step_7)
#
#     answer = step_7
#     return answer
#
#
# if __name__ == '__main__':
#     # solution("...!@BaT#*..y.abcdefghijklm")
#     # solution("z-+.^.")
#     # solution("=.=")
#     # solution("123_.def")
#     # solution("abcdefghijklmn.p")
#     solution("...")
