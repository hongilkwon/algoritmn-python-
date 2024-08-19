"""
    그룹 단어 체커(단순구현)

    그룹단어 -모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# if __name__ == '__main__':
#
#     cnt = 0
#     for _ in range(n):
#         s = str(input().strip())
#
#         flag = True
#         dic = dict()
#         current = ''
#         for i in range(len(s)):
#             c = s[i]
#             if c in dic:
#                 if c == current:
#                     continue
#                 else:
#                     flag = False
#                     break
#             else:
#                 dic[c] = 1
#                 current = c
#
#         if flag:
#             # print(s)
#             cnt += 1
#     print(cnt)
