"""
    회전초밥(슬라이딩 윈도우)

    *회전초밥(2531) 참고

     2 ≤ N ≤ 3_000_000,
     2 ≤ d ≤ 3_000

    사고과정.

    완전탐색을 이용하여 모든 연속해서 k를 먹은 후 종류의 max 값을 갱신한다.
    3_000_000 * 3_000 = 9000_000_000 (90억)
    불가능하다.

    배울점.
    1. splice(start, end)의 시간 복잡도 O(end-start)
    2. 중복을 제거를 위해 dictionary을 사용
    3. 슬라이딩 윈도우
    4. 원형 자료구조 다루기 (% 모듈러 연산)
    5. 삼항 연산자  참인 경우 값 if (조건) else 거짓인 경우 값
"""

# import sys
#
# input = sys.stdin.readline
#
# n, d, k, c = map(int, input().split())
#
# arr = [0] * n
# for i in range(len(arr)):
#     arr[i] = int(input())
#
# if __name__ == '__main__':
#
#     d = dict()
#     for i in range(0, k):
#         if arr[i] in d:
#             d[arr[i]] += 1
#         else:
#             d[arr[i]] = 1
#
#     max_sushi = len(d) if c in d else len(d) + 1
#
#     for i in range(1, n):
#
#         pre = arr[i - 1]
#         post = arr[i + k - 1] if (i <= n - k) else arr[((i + k) % n) - 1]
#
#         if (d[pre] - 1) == 0:
#             d.pop(pre)
#         else:
#             d[pre] -= 1
#
#         if post in d:
#             d[post] += 1
#         else:
#             d[post] = 1
#
#         # 연속된 초밥을 먹을 경우 쿠폰으로 받는 추가 스시
#         if c not in d:
#             d[c] = 1
#
#         max_sushi = max(max_sushi, len(d))
#
#     print(max_sushi)
