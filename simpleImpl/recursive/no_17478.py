"""
    재귀함수가 뭔가요?

    교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.
    출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
#
# def go(cnt):
#     if cnt == n:
#         str5 = '____' * cnt + '"재귀함수가 뭔가요?"'
#         str6 = '____' * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"'
#         str7 = '____' * cnt + '라고 답변하였지.'
#         print(str5)
#         print(str6)
#         print(str7)
#         return
#
#     str1 = '____' * cnt + '"재귀함수가 뭔가요?"'
#     str2 = '____' * cnt + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
#     str3 = '____' * cnt + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
#     str4 = '____' * cnt + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
#     print(str1)
#     print(str2)
#     print(str3)
#     print(str4)
#     go(cnt + 1)
#
#     str7 = '____' * cnt + '라고 답변하였지.'
#     print(str7)
#
#
# if __name__ == '__main__':
#     print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
#     go(0)
