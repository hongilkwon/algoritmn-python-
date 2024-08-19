"""
    행운을 빌어요(아이디어, 수학, 정수론)

   줄기와 잎을 "남김없이 모두 써서" 클로버를 만들기 위해,
   포닉스가 더 가져와야 하는 클로버 줄기와 잎 개수의 합의 최솟값을 구해주자.

   사고과정

   완전탐색 -> 시간초과

   1. 줄기가 부족한 경우
   2. 잎이 부족한 경우

   * 줄기가 부족한 경우를 먼저 고려해야 된다.
   그 이유는 전체 추가되는 것을 최소값을 구하는 것인데,
   줄기를 통해 모든 잎을 소모할 만큼 확보한 뒤, 부족한 잎의 개수를 추가해 준다.
"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#
#     for _ in range(tc):
#
#         julgi, leaf = map(int, input().split())
#
#         cnt = 0
#
#         while True:
#             if julgi * 3 <= leaf <= julgi * 4:
#                 break
#
#             if julgi * 3 > leaf:
#                 leaf += 1
#                 cnt += 1
#             if julgi * 4 < leaf:
#                 julgi += 1
#                 cnt += 1
#         print(cnt)
