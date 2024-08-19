"""
    제로

    K가 주어진다. (1 ≤ K ≤ 100,000)

    재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
    정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
"""

# import sys
#
# input = sys.stdin.readline
#
# k = int(input())
#
# if __name__ == '__main__':
#     stack = list()
#
#     for i in range(k):
#         num = int(input())
#         if num != 0:
#             stack.append(num)
#         if num == 0 and stack:
#             stack.pop()
#     print(sum(stack))
