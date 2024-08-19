"""
   최솟값 만들기

   배열 A, B에서 각 각 한 개의 숫자를 뽑아 두 수를 곱
   곱한 값을 누적하여 더합니다.
   k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.

   사고과정.

   곱의 최소값을 구해야됨.
   -> 작은것 * 큰것

   [1, 2, 4]
   [5, 4, 4]

   [4, 2, 1]
   [4, 4, 5]

"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(A, B):
#     answer = 0
#
#     A.sort()
#     B.sort(reverse=True)
#
#     sum = 0
#     for i in range(len(A)):
#         sum += (A[i] * B[i])
#
#     answer = sum
#     return answer
#
