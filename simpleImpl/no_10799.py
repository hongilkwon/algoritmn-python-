"""
    쇠막대기

    사고과정.

    쇠막대기가 언제 짤리는지가 중요하다.

    () 여는 괄호와 닫는 괄호과 만날때, 레이져가 생성되고 잘려나간다.
    => stack을 사용한다.
"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# arr = input().rstrip()
#
# if __name__ == '__main__':
#     stack = deque()
#
#     cnt = 0
#     for i in range(len(arr)):
#         c = arr[i]
#         if c == '(':
#             stack.append(c)
#         else:
#             if arr[i - 1] == '(':
#                 # 레이저인 경우
#                 stack.pop()
#                 cnt+= len(stack)
#             else:
#                 # 쇠막대기가 끝나는 지점인 경우
#                 stack.pop()
#                 cnt += 1
#     print(cnt)