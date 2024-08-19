"""
    키로거(LinkedList, 단순구현)

    최대 길이는 1,000,000 이기 때문에
    그 안에서 remove 연산을 하면 시간초과가 난다.

    python은 LinkedList 기본적으로 제공하지 않는다.

    아래와 같은 상황을 생각해 보자.

    [...] cursor [...]

    예) <<BP<A>>Cd-
    1. 문자가 입력되면 왼쪽에 글자를 넣음 -> cursor를 한칸 옮기는 것과 같다.
    2. '<' 왼쪽 리스트에서 마지막 원소를 꺼내서 오른쪽 제일 앞으로 이동.
    3. '>' 오른쪽 리스트에서 처음 원소를 꺼내서 왼쪽 마지막 으로 이동.
    4. '-' 왼쪽 리스트에서 마지막 원소를 지움

    단, <, >, - 의 문제에서 주어진 조건을 잘 확인해서 구현해야 된다.


"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#
#     for _ in range(tc):
#
#         pwd = str(input()).strip()
#
#         left = []
#         right = []
#
#         for c in pwd:
#             if c == '<':
#                 if left:
#                     right.append(left.pop())
#             elif c == '>':
#                 if right:
#                     left.append(right.pop())
#             elif c == '-':
#                 if left:
#                     left.pop()
#             else:
#                 left.append(c)
#
#         right.reverse()
#         answer = left + right
#         print("".join(answer))
