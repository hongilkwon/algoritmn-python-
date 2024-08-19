"""
    회전초밥(슬라이스)

    초밥의 종류를 번호로 표현
    벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.

    1. 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다.
    2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공

    접시 갯수 2 ≤ N ≤ 30_000,
    초밥 종류 2 ≤ d ≤ 3,000

    연속으로 먹는 갯수 2 ≤ k ≤ 3,000 (k ≤ N),
    쿠폰번호 초밥 1 ≤ c ≤ d이다.

    * 이벤트에 참여하지 않고 초밥을 먹는 경우는 없다. 무조건 이벤트에 참여해서 초밥을 먹음.

    먹을 수 있는 초밥의 가짓수의 최댓값

    사고과정.

    완전탐색을 이용하여 모든 연속해서 k를 먹은 후 종류의 max 값을 갱신한다.
    30_000 * 3_000 = 90_000_000 (9천만)
    1억보다 작기 때문에 가능하다. 단 splice(start, end) 함수이용.

    배울점.
    1. splice(start, end)의 시간 복잡도 O(end-start)
    2. 중복을 제거하기 위해 set 사용
    3. 원형 자료구조 다루기 (% 모듈러 연산)
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
#     max_sushi = 0
#     s = set()
#     for i in range(n):
#         if i <= n - k:
#             s.update(arr[i:i+k])
#         else:
#             temp = arr[i:] + arr[:(i + k) % n]
#             s.update(temp)
#         s.add(c)
#         max_sushi = max(max_sushi, len(s))
#         s.clear()
#
#     print(max_sushi)