"""
    회문(단순 구현.)

    시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지,
    아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다.

    만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력

    사고과정.

    유사 회문?
    - "한 문자"를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열

    1회차
    *     *
    abxxbxa

    2회차
     *   *
    abxxbxa
     bxxb
    
       **
    abxxbxa

        *
    abxxbxa
"""


# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#     for _ in range(tc):
#         word = input().rstrip()
#
#         left = 0
#         right = len(word) - 1
#
#         miss_cnt = 0
#         while left < right:
#             if word[left] == word[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 if word[left:right] == word[left:right][::-1] or word[left+1:right+1] == word[left+1:right+1][::-1]:
#                     miss_cnt = 1
#                 else:
#                     miss_cnt = 2
#                 break
#
#         if miss_cnt == 0:
#             print(0)
#         elif miss_cnt == 1:
#             print(1)
#         else:
#             print(2)
