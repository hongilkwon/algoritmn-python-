"""
    카드 합체 놀이(우선순위 큐)

    1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
    2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.


"""

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
#
# if __name__ == '__main__':
#     heapq.heapify(arr)
#
#     for _ in range(m):
#         a = heapq.heappop(arr)
#         b = heapq.heappop(arr)
#         c = a + b
#         heapq.heappush(arr, c)
#         heapq.heappush(arr, c)
#
#     print(sum(arr))
