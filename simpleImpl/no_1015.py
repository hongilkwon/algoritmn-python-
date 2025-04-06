"""
    수열정렬


    수열 P

    배열 A ==> 수열p 적용 ==> 배열 B(비 내림차순)

    B[P[i]] = A[i]

    N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수

    배열 A가 주어졌을떄,
    비내림차순이 되는 수열을 찾는 프로그램을 작성

    예시)
    A= [2, 3, 1]  out 수열P 1 2 0

    A[0] = B[P[0]]

    2  = B[P[0]] = B[1]
    3  = B[P[1]] = B[2]
    1  = B[P[2]] = B[0]

     A= [2, 3, 1]  >>>> B = [1, 2, 3]
    B 배열은 A 배열의 비내림차순 배열

    예시)
    A= [2, 1, 3, 1] out 2 0 3 1

    2  = B[P[0]] = B[2]
    1  = B[P[1]] = B[0]
    3  = B[P[2]] = B[3]
    1  = B[P[3]] = B[1]

    B = [1, 1, 2, 3]

    * P 수열은 A 수열의 각 숫자가 몇번째로 작은지를 0부터 정리한 수열
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# A = list(map(int, input().split(' ')))
#
#
# if __name__ == '__main__':
#
#     temp = sorted(A)
#
#     p = list()
#     for e in A:
#         p.append(str(temp.index(e)))
#         temp[temp.index(e)] = -1
#
#     print(' '.join(p))
