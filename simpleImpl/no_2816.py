"""
    디지털 티비

    1. 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
    2. 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
    3. 현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
    4. 현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

    채널의 수 N이 주어진다. (2 ≤ N ≤ 100)
    방법의 길이는 500보다 작아야 한다. 두 채널을 제외한 나머지 채널의 순서는 상관없다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# channels = [input().rstrip() for _ in range(n)]
#
# if __name__ == '__main__':
#     order = ''
#
#     idx_1 = channels.index("KBS1")
#     idx_2 = channels.index("KBS2")
#
#     # kbs1 이동.
#     for i in range(idx_1):
#         order += '1'
#     for i in range(idx_1):
#         order += '4'
#
#     if idx_1 > idx_2:
#         for i in range(idx_2 + 1):
#             order += '1'
#         for i in range(idx_2):
#             order += '4'
#     else:
#         for i in range(idx_2):
#             order += '1'
#         for i in range(idx_2 - 1):
#             order += '4'
#     print(order)
