"""
    0을 만들기(재귀, 문자열).

    기본적인 재귀 + 문자열 지식 물어보는 문자
    *문자열 수식 평가 함수 eval()


    1. 1에서 n까지 사이에 연산자 3종류를 채운다.
    2. n-1개를 중복해서 뽑아 채울수 있다.
    3. 재귀로 구혆

    1 2 3
     + -
    1+2-3


    00:00
"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
# n = 0
# arr = []
#
# answer = []
#
# ret = []
# def go(cnt):
#     if cnt == 0:
#
#         s = arr[0]
#         for i in range(0, n-1):
#             s += ret[i]
#             s += arr[i+1]
#
#         if eval(s.replace(' ','')) == 0:
#             answer.append(s)
#         return
#
#     for item in ['+', '-', ' ',]:
#         ret.append(item)
#         go(cnt - 1)
#         ret.pop()
#
#
# if __name__ == '__main__':
#     for _ in range(tc):
#         n = int(input())
#         arr = [str(i) for i in range(1, n + 1)]
#         answer = []
#
#         go(n - 1)
#         answer.sort()
#         for e in answer:
#             print(e)
#         print()

