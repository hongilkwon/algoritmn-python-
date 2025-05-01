"""
    과일 탕후루

    막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다

    1 <= n <= 20 0000
    
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))

if __name__ == '__main__':
    answer = 0
    d = defaultdict(int)

    left, right, fruit_type_cnt = 0, 0, 0

    while right < n:
        # 한번도 사용하지 않은 과일,
        if d[arr[right]] == 0:
            fruit_type_cnt += 1
        d[arr[right]] += 1

        # 사용된 과일의 종류가 2개 이상
        while fruit_type_cnt > 2:
            d[arr[left]] -= 1
            if d[arr[left]] == 0:
                fruit_type_cnt -= 1
            left += 1

        answer = max(answer, right - left + 1)
        right += 1

    print(answer)