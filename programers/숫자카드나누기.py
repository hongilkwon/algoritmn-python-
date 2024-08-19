"""
    숫자카드 나누기
"""

# import math
#
#
# def gcd(num1, num2):
#     a, b = (num1, num2) if num1 > num2 else (num2, num1)
#
#     while a % b != 0:
#         r = a % b
#         a = b
#         b = r
#     return b
#
#
# def solution(arrayA, arrayB):
#     answer = 0
#
#     gcdA = arrayA[0]
#     gcdB = arrayB[0]
#
#     for i in range(1, len(arrayA)):
#         gcdA = gcd(gcdA, arrayA[i])
#         gcdB = gcd(gcdB, arrayB[i])
#     # print('gcdA:', gcdA, 'gcdB:', gcdB)
#
#     flagA = True
#     flagB = True
#     for i in range(len(arrayA)):
#         if arrayA[i] % gcdB == 0:
#             flagA = False
#         if arrayB[i] % gcdA == 0:
#             flagB = False
#
#     if (flagA == False) and (flagB == False):
#         answer = 0
#     elif (flagA == True) and (flagB == False):
#         answer = gcdA
#     elif (flagA == False) and (flagB == False):
#         answer = gcdB
#     else:
#         answer = max(gcdA, gcdB)
#
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution([14, 35, 119], [18, 30, 102])
