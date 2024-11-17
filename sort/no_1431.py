"""
    정렬

    모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)

    A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
    만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
    만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = list()
# for _ in range(n):
#     arr.append(str(input()).rstrip())
#
# def cal_sum(s):
#     ret = 0
#     for c in s:
#         if c.isdecimal():
#             ret += int(c)
#     return ret
#
# if __name__ == '__main__':
#     # print(arr)
#     arr.sort(key= lambda x: (len(x), cal_sum(x), x))
#     for e in arr:
#         print(e)
#

