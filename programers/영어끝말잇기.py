"""
    영어 끝말잇기

    조건을 통한 단순구현 문제.

"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(n, words):
#     answer = []
#
#     rotation_cnt = 1
#     current_person = 1
#     temp = set()
#     temp.add(words[0])
#
#     for i in range(1, len(words)):
#         rotation_cnt = (i // n) + 1
#         if (i + 1) % n == 0:
#             current_person = n
#         else:
#             current_person = (i + 1) % n
#
#         prev = words[i - 1]
#         word = words[i]
#         if word in temp or len(word) == 1 or prev[-1] != word[0]:
#             answer = [current_person, rotation_cnt]
#             break
#
#         temp.add(word)
#         if i == len(words) - 1:
#             answer = [0, 0]
#
#     return answer
#
#
# if __name__ == '__main__':
#     pass
