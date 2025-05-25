"""
    양팔저울

    서로 다른 k개의 추와 빈 그릇
    그릇의 무게 0

    추가 3개이고 그 무게가 각각 {1, 2, 6}이면, S = 9이고,
    양팔 저울을 한번만 이용하여 1부터 S사이 모든 정수에 대응하는 물을 다음과 같이 그릇에 담을 수 있다.

    "측정이 불가능한 경우의 수를 찾는 프로그램을 작성"

    예시)

    추가 3개이고 그 무게가 각각 {1, 2, 6}이면, S = 9

    1 ,2, 3, (6-2), (6-1), 6, 1+6, 2+6, 1+2+6

    추가 3개이고 그 무게가 각각 {1, 5, 7}이면, S = 13

    1, (7-5), (7-5+1), (5-1), 5, (7-1)

    추의 갯수.
    k(3 ≤ k ≤ 13)

    풀이

    완전 탐색,
    각 노드 마다 3가지 선택을 할 수 있음.

    1. 안놓기.
    2. 저울의 왼쪽
    3. 저울의 오른쪽


    dp (top-down)


"""

# import sys
#
# input = sys.stdin.readline
#
# k = int(input())
# weight = list(map(int, input().split()))
#
# arr = [0 for _ in range(sum(weight) + 1)]
#
#
# def go(idx, left_sum, right_sum):
#     if idx == k:
#         num = abs(left_sum - right_sum)
#         arr[num] = 1
#         return
#
#     go(idx + 1, left_sum, right_sum)
#     go(idx + 1, left_sum + weight[idx], right_sum)
#     go(idx + 1, left_sum, right_sum + + weight[idx])
#
#
# if __name__ == '__main__':
#     go(0, 0, 0)
#
#     answer = 0
#     for e in arr:
#         if e == 0:
#             answer += 1
#     print(answer)