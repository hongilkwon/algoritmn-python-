"""
    모음사전

    사고과정

    1 A
    2 AA
    3 AAA
    4 AAAA
    5 AAAAA
    6 AAAAE
    7 AAAAI
    8 AAAAO
    9 AAAAU
   10 AAAE
   11 AAAEA

   깊이 우선탐색.
"""

# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# answer = 0
# cnt = -1
# mo = ['A', 'E', 'I', 'O', 'U']
#
#
# def go(target, word):
#     global answer, cnt
#     cnt += 1
#
#     # print('word', word, 'cnt:', cnt)
#
#     if target == word:
#         answer = cnt
#         return
#
#     if len(word) >= 5:
#         return
#
#     for c in mo:
#         go(target, word + c)
#
#
# def solution(word):
#     global answer, cnt
#
#     go(word, '')
#     return answer
#
#
# if __name__ == '__main__':
#     solution("AAAAE")
