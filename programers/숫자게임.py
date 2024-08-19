"""
    숫자게임(Greedy, 탐욕법)

    A팀은 빠르게 출전순서를 정했고 자신들의 출전 순서를 B팀에게 공개해버렸습니다.
    B팀은 그것을 보고 자신들의 "최종 승점"을 가장 높이는 방법

    1 <= A, B length <=100_000
    1 < =A와 B의 각 원소 <= 1_000_000_000(10억)

    사고과정

    최대한 많이 이겨야 한다..

    정렬을 해서 가장 최소한의 차이로 이기면된다?

    A [5,1,3,7]
    B [2,2,6,8]

    A [15,12,8,7,5]
    B [8,6,2,2,2]

    이길수 없거나 비긴다면, B에서 최소값 카드를 버린다.
    이길수 있다면 정렬이 되어 있으니까, B에서 최대값 카드를 사용한다??

    배울점.
    python의 list sort, sorted의 함수를 조금 더 자유롭게 사용할 수 있어야 한다.

"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def solution(A, B):
#     answer = -1
#
#     A.sort(reverse=True)
#     B.sort(reverse=True)
#
#     dq = deque(B)
#     cnt = 0
#     for i in range(len(A)):
#         if A[i] >= dq[0]:
#             dq.pop()
#         else:
#             dq.popleft()
#             cnt += 1
#     print(cnt)
#     answer = cnt
#     return answer

#
# if __name__ == '__main__':
#     solution([5, 1, 3, 7], [2, 2, 6, 8])
#     solution([2, 2, 2, 2], [1, 1, 1, 1])
