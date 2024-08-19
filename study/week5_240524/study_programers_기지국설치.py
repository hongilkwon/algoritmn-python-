"""
    기지국 설치(아이디어, 복잡구현)

    5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달

    1 <= N <= 200_000_000 (2억)????
    1 <= stations <= 10_000
    1 <= W <= 10_000

    "증설할 기지국 개수의 최솟값"을 리턴

    사고과정

    기지국 1개를 설치하면 w + 1 + w 만큼 커버됨.

    전파가 안통하는 아파트가 연속으로 2w+1개를 넘으면 무조건 1개는 세워야됨

    안 세워진 곳의 크기를 측정하자!

    -> 주어진 입력값을 통해 직접 기존의 기지국을 세워서 해결(n의 크기가 2억이라 불가능)
    -> 스테이션을 기준으로 나눠서 센다.
"""

# n = 0
# stations = []
# w = 0
#
#
# def solution(_n, _stations, _w):
#     global n, stations, w
#
#     n = _n
#     stations = _stations
#     w = _w
#
#     cnt = 0
#     start = 0
#     for i in stations:
#         end = (i - 1) - w
#         size = end - start
#         # print("end:", end, "start:", start)
#         # print("size:", size)
#         if size > 0:
#             cnt += int(size / (2 * w + 1))
#             if size % (2 * w + 1):
#                 cnt += 1
#         start = (i - 1) + w + 1
#
#     if start < n:
#         size = n - start
#         # print("n:", n, "start:", start)
#         # print("size:", size)
#         cnt += int(size / (2 * w + 1))
#         if size % (2 * w + 1):
#             cnt += 1
#
#     answer = cnt
#     return answer
#
#
# if __name__ == '__main__':
#     solution(11, [4, 11], 1)
#     # solution(16, [9], 2)

# import sys
#
# n = 0
# stations = []
# w = 0
#
# check = []
#
#
# def install(i):
#     # 센터
#     check[i] = True
#     # 전파의 뒷 영역
#     for j in range(i - 1, i - w - 1, -1):
#         if j < 0 or j >= n:
#             continue
#         check[j] = True
#     # 전파의 앞 영역
#     for j in range(i + 1, i + w + 1):
#         if j < 0 or j >= n:
#             continue
#         check[j] = True
#
#
# def solution(_n, _stations, _w):
#     global n, stations, w, check
#
#     n = _n
#     stations = _stations
#     w = _w
#
#     check = [False] * n
#     for i in stations:
#         idx = i - 1
#         install(idx)
#     # print(check)
#
#     answer = 0
#     cnt = 0
#     for i in range(n):
#         if check[i] and cnt > 0:
#             answer += int(cnt / (2 * w + 1))
#             if cnt % (2 * w + 1):
#                 answer += 1
#             cnt = 0
#         if not check[i]:
#             cnt += 1
#     # 예외
#     if cnt > 0:
#         answer += int(cnt / (2 * w + 1))
#         if cnt % (2 * w + 1):
#             answer += 1
#
#     print(answer)
#     return answer
