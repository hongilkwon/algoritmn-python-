"""
    단어 맞추기.

    완전탐색 불가능

    100개 =>

    A B C D E
    F G H I J
    K L N M O
    P Q R S T
    V U w X Y
    Z

    1. 오른쪽에서 왼쪽으로 오름차순이 아닌 index 찾기
    2. 지나온것중 가장 작은 문자(수)과 위치 교환.
    3.

    4! => 4*3*2*1 => 24

       <
    ABCD 1234

      <=
    ABDC 1243

       <
    ACBD 1324

      <=
    ACDB 1342

       <
    ADBC 1423

     <==
    ADCB 1432

       <

    BACD 2134
    .
    .
    .
     <==
    BDCA


    <===
    DCBA 4321

"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
#
# if __name__ == '__main__':
#
