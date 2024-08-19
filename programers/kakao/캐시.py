"""
    캐시

    LRU(Least Recently Used)를 사용

    cache hit일 경우 실행시간은 1
    cache miss일 경우 실행시간은 5

    대,소문자 구분을 하지 않는다.

    0 ≦ cacheSize ≦ 30
    * cacheSize 0일수 도 있음

    1 <= 도시 수  <= 100_000

    사고과정
    단순구현 문제로 쉬운문제
    히자만 예외처리를 2개 해주어야됨.

    배운점.
    python

    dict의 원소 제거 방법 -> del(dict[key]), dict.pop(key)
    대, 소문자 변경 함수 -> s.lower(), s.upper()
     temp = [s.lower() for s in list]
     temp = list(map(lambda x: x.upper(), ["a", "b", "c"]))
"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(cacheSize, cities):
#     answer = 0
#
#     if cacheSize == 0:
#         return len(cities) * 5
#
#     cities = [citiy.lower() for citiy in cities]
#
#     cache = dict()
#     time = 0
#     for idx, city in enumerate(cities):
#         if city in cache:
#             cache[city] = idx
#             time += 1
#         else:
#             if len(cache) >= cacheSize:
#                 temp = list(cache.items())
#                 temp.sort(key=lambda x: x[1])
#                 key = temp[0][0]
#                 del (cache[key])
#             cache[city] = idx
#             time += 5
#
#     answer = time
#     return answer
#
#
# if __name__ == '__main__':
#     solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
