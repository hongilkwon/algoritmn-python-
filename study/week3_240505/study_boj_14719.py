"""
    빗물(완전탐색, 아이디어)

    (1 ≤ H, W ≤ 500)

    사고과정

    1. 완전탐색

    물이 고인다?? --> "양쪽"으로 막혀 있다.
    얼마나 고이는가?? --> w 1칸을 기준으로 보면 왼쪽에서 가장 높은 블록, 오른쪽에서 가장 높은 블록중에서, 작은것 만큼 물이 고일 수 있다.
    처음 블록과 마지막 블록은 물이 고일 수가 없다.

    배울점

    h, w의 범위가 500으로 적기 때문에 500*500 = 250000 이기 때문에 충분히 완전탐색을 하더라도 시간은 충분하다.
    하지만 물이 고이는 조건을 논리적으로 생각하는게 조금 까다롭다.
    오히려, 모노톤스택, 투포인터 등등으로 시간적 효율성을 줄이려다가 문제가 더욱 어렵게 느껴질 수 있다.

"""

# import sys
#
# input = sys.stdin.readline
#
# h, w = map(int, input().split())
# arr = list(map(int, input().split()))
#
# if __name__ == '__main__':
#
#     answer = 0
#     for i in range(1, len(arr) - 1):
#         left = max(arr[0:i])
#         right = max(arr[i + 1:len(arr)])
#
#         waterHeight = min(left, right) - arr[i]
#         if waterHeight > 0:
#             answer += waterHeight
#
#     print(answer)
