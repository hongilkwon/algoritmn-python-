"""
    용액 합성하기.

    두 용액을 섞을 때는 10ml씩 섞어서 20ml로 만드는데, 단 "한 번밖에 할 수 없다".
    0에 가장 가까운 특성값 B를 출력

    2 ≤ N ≤ 100,000
    -100_000_000 ≤ Ai ≤ 100_000_000
    Ai-1 ≤ Ai

    사고과정.

    2개의 용액을 뽑아 모든 경우의 수를 구해본다?
    100_000 C 2 => (100_000 * 99_999) / 2

    시간초과남.

    O(N) 시간 복잡도로 해결을 해야됨.
    2개의 용액을 합해 0에 가깝다 ---> 절대값이 작다.

    절대값이 작으려면 서로 가장 차이가 많이 나는 2개의 용액을 섞어야된다!
    그럼 용액의 시작과 끝에서 부터 2개의 포인터를 가지고 탐색한다.

    포인터를 언제 움직여야 하는가??

    왼쪽 포인터 ->   절대값이 0 보다 작으면서 0이 아닌 경우
    오른쪽 포인터 ->  절대값이 0 보다 크면서 0이 아닌 경우

    예시)
    -101 -3 -1 5 93

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# if __name__ == '__main__':
#
#     left = 0
#     right = len(arr) - 1
#
#     answer = 200_000_001
#     while left < right:
#         sum = arr[left] + arr[right]
#
#         if abs(answer) > abs(sum):
#             answer = sum
#
#         if 0 > sum:
#             left += 1
#         else:
#             right -= 1
#     print(answer)
