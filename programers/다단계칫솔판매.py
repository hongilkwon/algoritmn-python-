"""
    다단계 칫솔 판매

    모든 판매원은 "칫솔의 판매에 의하여 발생하는 이익"에서 10% 를 계산하여,
    자신을 조직에 참여시킨 추천인에게 배분하고 나머지는 자신이 가집니다.

    모든 판매원은 자신이 칫솔 판매에서 발생한 이익 뿐만 아니라,
    자신이 조직에 추천하여 "가입시킨 판매원에게서 발생하는 이익"의 10% 까지 자신에 이익이 됩니다

    칫솔판매 10% 위로 상납
    자신의 이익 = 칫솔판매 90% + 가입시킨 판매원에게서 발생하는 이익 10%

    "10%를 계산한 금액이 1원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.

    seller 에는 같은 이름이 "중복"해서 들어있을 수 있습니다.
    칫솔 한 개를 판매하여 얻어지는 이익은 100 원으로 정해져 있습니다.

    <사고과정>

    각 자료를 정리하여 깊이우선탐색으로 자식 -> 루트로 올라가면서 계산한다?
    하지만, 이때 모든 자식의 수입을 더 하여 10%를 계산한다면, 오류가 발생할 수 있다.
    특히, seller에 이름이 "중복"해서 존대한다면

    예를 들어, A가 10개씩 칫솔을 10번 판매했다고 가정해보자.

    10*100원 =1000 씩 10번

    1번
    A 900
    A의 부모 90
    A의 부모의 부모 9
    A의 부모의 부모의 부모 1
    A의 부모의 부모의 부모의 부모 0

    10번합
    A 9000
    A의 부모 900
    A의 부모의 부모 90
    A의 부모의 부모의 부모 9
    A의 부모의 부모의 부모의 부모 1

    결론은 모든 판매를 순회하면서 각 판매별로 부모에게 누적 시켜야됨.

"""

# import math
#
# n = 0
# parent_dict = dict()
# idx_dict = dict()
#
#
# def solution(enroll, referral, seller, amount):
#     global n, parent_dict, idx_dict
#
#     n = len(enroll)
#     for i in range(n):
#         idx_dict[enroll[i]] = i
#         parent_dict[enroll[i]] = referral[i]
#
#     answer = [0 for _ in range(n)]
#
#     for i, v in enumerate(seller):
#         income = amount[i] * 100
#         name = v
#
#         print(name, income)
#         while True:
#
#             if name == "-":
#                 break
#
#             if income < 10:
#                 answer[idx_dict[name]] += income
#                 break
#
#             idx = idx_dict[name]
#             answer[idx] += math.ceil(income * 0.9)
#
#             income = math.floor(income * 0.1)
#             name = parent_dict[name]
#
#     print(*answer)
#     return answer


if __name__ == '__main__':
    solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
             ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
             ["young", "john", "tod", "emily", "mary"],
             [12, 4, 2, 5, 10]
             )
