"""
    ZOAC(완전탐색, 재귀, 문자열)

   문자열의 길이는 최대 100자

    사고과정.

    1. 재귀함수
    - 사전순으로 빠르다 --> 아스키값( A-65, a-97 )이 가장 작다.
    - 규칙이 분명 재귀적인 성격을 띄고 있다는 것은 파악했지만, 구현력이 부족했음.


    예시) ST A RTLINK

       * -->
     __A______

     정해진 구간에서 "가장 작은 문자를 찾는다".
       *
     __A___I__

     가장 작은 문자를 기준으로, 사전순서로 가장 앞서기 위해서 왼쪽부터 추가해준다.
           *
     __A___I__
             *
     __A___I_K
             *
     __A___INK

           *
     __A__TINK

     더 이상 왼쪽을 추가할 수 없다면, 오른쪽 구간에 추가해 준다.
"""

# import sys
#
# input = sys.stdin.readline
#
# s = list(str(input()).strip())
# isSelected = [False] * len(s)
#
#
# def go(left, right):
#     # 가장 아스키 값이 작은 문자를 찾는다.
#     c = ord('Z') + 1
#     idx = -1
#
#     for i in range(left, right + 1):
#         if isSelected[i]:
#             continue
#         if ord(s[i]) < c:
#             c = ord(s[i])
#             idx = i
#
#     if idx == -1:
#         return
#
#     isSelected[idx] = True
#
#     temp = ""
#     for i in range(len(s)):
#         if isSelected[i]:
#             temp += s[i]
#     print(temp)
#     # 오른쪽
#     go(idx + 1, right)
#     # 왼쪽
#     go(left, idx - 1)
#
#
# if __name__ == '__main__':
#     go(0, len(s) - 1)
