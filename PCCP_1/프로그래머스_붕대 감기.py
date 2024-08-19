"""
    [PCCP 기출문제] 1번 붕대감기(단순구현)


    기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고,
    공격을 당하는 순간에는 체력을 회복할 수 없습니다.
    몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용하며,
    연속 성공 시간이 0으로 초기화

    *현재 체력이 0 이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없습니다.

    배울점
    단순 구현문제인데 기본적으로 파이썬 자료구조 함수를 좀 쓰는데 능숙해야 빠르게 작성 가능하다.
    또한, 생각보다 조건들이 많기 때문에 실수할 곳이 많다.
    기업코테의 1,2번 문제로 충분히 나올만 하다.

"""


# def solution(bandage, health, attacks):
#     answer = 0
#
#     combo = 0
#     current_hp = health
#     time = attacks[-1][0]
#
#     is_dead = False
#     for i in range(time + 1):
#         if attacks[0][0] == i:
#             attack = attacks.pop(0)
#             current_hp -= attack[1]
#             combo = 0
#
#             if current_hp <= 0:
#                 is_dead = True
#                 break
#             continue
#         else:
#
#             if current_hp + bandage[1] < health:
#                 current_hp += bandage[1]
#             else:
#                 current_hp = health
#             combo += 1
#             if bandage[0] == combo:
#                 if current_hp + bandage[2] < health:
#                     current_hp += bandage[2]
#                 else:
#                     current_hp = health
#                 combo = 0
#
#     return -1 if is_dead else current_hp


if __name__ == '__main__':
    ret = solution([4, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]])
    print(ret)
