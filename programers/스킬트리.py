"""
    스킬트리

    스킬은 중복해 주어지지 않습니다.

    사고과정.

    단순구현
    list.index(value) -> 해당 값을 가진 첫번째 index 반환
"""


# def solution(skill, skill_trees):
#     answer = -1
#
#     skill_set = set(skill)
#     cnt = 0
#     for skill_tree in skill_trees:
#         temp = []
#         for s in skill_tree:
#             if s in skill_set:
#                 temp.append(s)
#
#         flag = True
#         for i in range(len(temp)):
#             if temp[i] != skill[i]:
#                 flag = False
#                 break
#
#         if flag:
#             cnt += 1
#
#     answer = cnt
#     return answer