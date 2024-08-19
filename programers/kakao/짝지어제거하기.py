"""
    짝지어제거하기(스택)

    문자열에서 같은 알파벳이 2개 붙어 있는 짝

    모두 제거한다면 짝지어 제거하기가 종료
    문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환

     1 <= 문자열의 길이 <= 1_000_000
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def solution(s):
#     answer = -1
#
#     if len(s) % 2 == 1:
#         return 0
#
#     stack = deque()
#
#     for c in s:
#         if stack and stack[-1] == c:
#             stack.pop()
#         else:
#             stack.append(c)
#
#     if stack:
#         answer = 0
#     else:
#         answer = 1
#
#     return answer
