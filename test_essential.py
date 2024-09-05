"""
    1. 문자열
    - 아스키 코드 (A-65 ,a-97)
    - chr(97) ord('a')

    - lower() 소문자
    - upper() 대문자
    - islower(), isupper(), isdecimal()

    2. 기본 수학.

    순열, 조합.
    from itertools import combinations, permutations

    3. 정렬.

    4. heapq, deque

    5.
    ret => (h, m)
    answer = '%02d:%02d' % ret
"""

import sys
sys.setrecursionlimit(10**6)

from collections import deque
import heapq

input = sys.stdin.readline

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"person(name:{self.name}, age:{self.age})"

if __name__ == '__main__':
    pass
    # person_list = [Person('c', 8), Person('a', 8), Person('b', 8), Person('d', 15), Person('a', 20), Person('b', 13)]
    # person_list.sort(key= lambda x: (x.age, x.name))
    # print(person_list)
    #
    #
    # temp = ['1', '100', '04', '02', '16']
    # temp.sort(key=int)
    # print(temp)
    #
    # deque.append()
    # deque.pop()
    # deque.appendleft()
    # deque.popleft()


    # q = []
    # heapq.heappush(q, (-10,10))
    # heapq.heappush(q, (-5, 5))
    # heapq.heappush(q, (-12,12))
    #
    # print(heapq.heappop(q)[1])