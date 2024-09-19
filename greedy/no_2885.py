"""
    초콜릿 식사(greedy)


    적어도 K개 정사각형을 먹어야 남은 수업을 졸지 않고 버틸 수 있다.
    선영이는 초콜릿은 돈을 주고 사기 아깝다고 생각하기 때문에, 상근이가 주는 초콜릿만 먹는다.

    막대 초콜릿은 나누기 조금 어렵게 되어 있어서, 항상 가운데로만 쪼개진다

    K개 정사각형을 만들기 위해서, 최소 몇 번 초콜릿을 쪼개야 하는지와 사야하는 가장 작은 초콜릿의 크기를 구하는 프로그램을 작성

    사고과정.

    6개

    2^8

    2^7                           2^7
    2^6
    2^5
    2^4
    2^3
    2^2
    2^1

    문제를 이해하는데 생각 보다 어렵다.

"""


# import sys
#
# input = sys.stdin.readline
#
# k = int(input())
#
#
# if __name__ == '__main__':
#
#     choco_size = 1
#     while choco_size < k:
#         choco_size = choco_size * 2
#     ret1= choco_size
#
#     cut_cnt = 0
#     while k > 0:
#         if k >= choco_size:
#             k -= choco_size
#         else:
#             choco_size //= 2
#             cut_cnt += 1
#     ret2 = cut_cnt
#     print(ret1, ret2)