"""
    옥상정원(모노톤 스택, monotone stack, 구현)

    빌딩의 개수 N이(1 ≤ N ≤ 80_000)
    각 빌딩의 높이가 hi 입력된다. (1 ≤ hi ≤ 1_000_000_000)

    사고과정

    각 빌딩(원소) 마다 자신의 시야를 가로막는 즉, 다신 보다 오른쪽에서 처음 나오는 큰수와 몇칸 떨어져 있는지 구한다.

    1. 완전탐색
    80_000 * 80_000 = 1600_000_000 (16억) >>> 불가능함.

    2. 모노톤 스택
    - 스택의 원소를 중복이 없이, 오름/내림차순 상태를 유지
    - 자신보다 최초로 나오는 큰 수/작은 수

    참고
    https://www.youtube.com/watch?v=o0j0mlo0j0mlLGXdoLGXdo
    https://fisher10001.tistory.com/123

    내림차순 모노톤 스택을 사용한다.

   높이  10  3  7  4  12 2
   idx  1   2  3  4  5  6

   10 -> stack size = 0, 이후 stack 에 넣음.
   10 3 -> 높이3 2번 빌딩을 바라볼 수 있는 빌딩은 높이10인 1번 벌딩(stack size = 1) 이후 stack 에 넣음.
   10 7 -> 높이3 2번 빌딩이 나가고 높이7 3번 빌딩을 바라볼 수 있는 빌딩은 높이10인 1번 벌딩(stack size = 1), 이후 stack 에 넣음.
   10 7 4 -> 높이4 4번 빌딩을 바라볼 수 있는 빌딩은 높이10인 1번 벌딩, 높이7인 3번 빌딩(stack size = 2), 이후 stack 에 넣음.
   .
   .
   .
   새로운 빌딩의 높이가 내림차순으로 모노톤 스택을 이룬다면 남아있는 스택들은 전부 새로운 높이의 빌딩의 옥상을 볼수 있기 떄문에 stack size를 더해줌.

   배울점.
   1. 모노톤 스택
   2. 정답이 int 범위를 넘어 long type을 사용.
   - (79999 * 80000) / 2
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = [0] * n
# for i in range(n):
#     arr[i] = int(input())
#
# if __name__ == '__main__':
#
#     s = deque()
#
#     answer = 0
#     for i in range(len(arr)):
#
#         while s and s[-1] <= arr[i]:
#             s.pop()
#
#         answer += len(s)
#         s.append(arr[i])
#
#     print(answer)
