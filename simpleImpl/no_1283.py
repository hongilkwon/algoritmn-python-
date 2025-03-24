"""
    단축키 지정(구현, 문자열).

    옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명

    1. 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다.
    만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
    2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
    3. 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
    4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

    replace(old, new, count)
    print('구분자'.join(list))

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# options = list()
# for _ in range(n):
#     option = input().rstrip().split(' ')
#     options.append(option)
#
# # print(options)
#
# used_key = set()
#
# if __name__ == '__main__':
#
#     for option in options:
#         flag = False
#
#         # 1번 조건.
#         for i in range(len(option)):
#             word = option[i]
#             if word[0] not in used_key:
#                 flag = True
#                 used_key.add(word[0].upper())
#                 used_key.add(word[0].lower())
#                 option[i] = word.replace(word[0], '[' + word[0] + ']', 1)
#                 break
#
#         # 2번 조건.
#         if flag: continue
#
#         for i in range(len(option)):
#             word = option[i]
#             for j in range(len(word)):
#                 c = word[j]
#                 if c not in used_key:
#                     flag = True
#                     used_key.add(c.upper())
#                     used_key.add(c.lower())
#                     option[i] = word.replace(c, '[' + c + ']', 1)
#                     break
#             if flag: break
#
#     # 출력
#     for option in options:
#         print(' '.join(option))