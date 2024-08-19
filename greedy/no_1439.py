"""
    뒤집기.

    S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
    최소 횟수

    S의 길이는 100만보다 작다.

"""


# import sys
#
# input = sys.stdin.readline
#
# s = input().rstrip()
#
# if __name__ == '__main__':
#
#     zero_list = []
#     one_list = []
#
#     temp = ''
#     for i in range(len(s)):
#         c = s[i]
#         if len(temp) == 0:
#             temp += c
#             continue
#
#         if temp[-1] == c:
#             temp += c
#         else:
#             if c == '0':
#                 one_list.append(temp)
#                 temp = '0'
#             else:
#                 zero_list.append(temp)
#                 temp = '1'
#
#     if len(temp) != 0:
#         if temp[-1] == '0':
#             zero_list.append(temp)
#         else:
#             one_list.append(temp)
#
#     # print(zero_list)
#     # print(one_list)
#     print(min(len(zero_list), len(one_list)))
