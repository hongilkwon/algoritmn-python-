"""
    수식 최대화

    숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식
    같은 순위의 연산자는 없어야 합니다
    만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출하며 제출한 숫자가 가장 큰 참가자를 우승자로 선정

    expression은 길이가 3 이상 100 이하인 문자열
    피연산자(operand)는 0 이상 999 이하의 숫자

    402+-561*"처럼 잘못된 수식은 올바른 중위표기법이 아니므로 주어지지 않습니다.
    -56+100"처럼 피연산자가 음수인 수식도 입력으로 주어지지 않습니다.
    expression은 적어도 1개 이상의 연산자를 포함
    절댓값이 263 - 1 이하가 되도록 입력이 주어집니다.
    같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.


    사고과정.

    연산자 우선순위를 먼저 모두 정한다.
    그리고 주어진식을 판단한다.
    최대값을 갱신한다.

    로직은 어렵지 않았는데 구현이 생각보다 알아야하는 기능도 많고 많이 복잡했다...
    다른 사람의 단순화된 풀이를 참고해보자!

    python이 아니라 c++, java, kotlin? 이라면,

"""

# import itertools
# import copy
#
#
# def calExp(operator, exp):
#     ret = []
#
#     flag = False
#
#     for i in range(len(exp)):
#         if flag:
#             flag = False
#             continue
#         if exp[i] == operator:
#             temp = ''
#             if operator == '-':
#                 temp = str(int(ret.pop()) - int(exp[i + 1]))
#             if operator == '+':
#                 temp = str(int(ret.pop()) + int(exp[i + 1]))
#             if operator == '*':
#                 temp = str(int(ret.pop()) * int(exp[i + 1]))
#             ret.append(temp)
#             flag = True
#         else:
#             ret.append(exp[i])
#     return ret
#
#
# def solution(expression):
#     num = ''
#     expression_list = []
#     operator_set = set()
#     for c in expression:
#         if c in ['+', '-', '*']:
#             operator_set.add(c)
#             expression_list.append(num)
#             expression_list.append(c)
#             num = ''
#         else:
#             num += c
#     expression_list.append(num)
#
#     max_value = 0
#     permu = itertools.permutations(operator_set)
#     for operators in permu:
#         temp = copy.deepcopy(expression_list)
#         for operator in operators:
#             temp = calExp(operator, temp)
#         max_value = max(max_value, abs(int(temp[0])))
#
#     answer = max_value
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     # solution("100-200*300-500+20")
#     solution("50*6-3*2")
