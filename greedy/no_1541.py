"""
    잃어버린 괄호(그리디, String)

   괄호를 적절히 쳐서 이 식의 값을 최소
   식의 길이는 50보다 작거나 같다.

   1. 완전탐색

   V 55 V - V 50 V + V 40 V
   여는 괄호 및 닫는 괄호 어떻게 넣어야 수식이 될지 모른다.
   몇개의 괄호들이 추가 될지도 모른다.
   ???

   2. 최소값이 된다?? >>>> 음수 이후로 나오는 양수를 최대한 몰아서 괄호를 친후 뺴준다.

   새로운 음수 가나올때 까지
   즉  - (num1 + num2 + num3 .. )

   배울점.
    - 완전탐색이 충분히 가능한 문제로 보이나, 완전탐색을 어떻게 해야할지 알수없음.
    - String 함수  .split()
    - len(*iterable) - iterable 길이를 반환
    - map(func, *iterable) - iterable 원소 1개씩 func을 적용한 새로운 List 반환
    - sum(*iterable, start) iterable 합을 반환
"""

# import sys
#
# input = sys.stdin.readline
#
# exp = str(input())
#
# if __name__ == '__main__':
#
#     expList = exp.split("-")
#
#     answer = 0
#     for i in range(0, len(expList)):
#
#         if expList[i] == "":
#             continue
#
#         if i == 0:
#             answer += sum(map(int, expList[i].split("+")))
#         else:
#             answer -= sum(map(int, expList[i].split("+")))
#
#     print(answer)