"""
    올바른 괄호
    짝맞추기...

    일반적으로 stack을 이용한다
    모든 괄호가 올바르게 맞춰진다면, 문자열을 모두 순회하였을때 스택은 비어있다.
"""

# import sys
#
# input = sys.stdin.readline
#
# from collections import deque
#
#
# def solution(s):
#     answer = True
#
#     stack = deque()
#
#     for c in s:
#         if stack and c == ')':
#             stack.popleft()
#         else:
#             stack.appendleft(c)
#
#     if stack:
#         answer = False
#
#     return answer
#
#
# if __name__ == '__main__':
#     solution("(())()")
