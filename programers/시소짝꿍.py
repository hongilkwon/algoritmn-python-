"""
    시소짝꿍

    2 ≤ weights의 길이 ≤ 100_000

    2 => 1, 3/2, 2
    3 => 2/3,  1,  4/3
    4 => 1/2, 3/4   1


    1/2, 2/3, 3/4, 1, 4/3, 3/2, 2
"""



import sys

input = sys.stdin.readline

def solution(weights):
    answer = 0

    weight_cnt_dict = dict()
    for w in weights:
        if w in weight_cnt_dict:
            weight_cnt_dict[w] += 1
        else:
            weight_cnt_dict[w] = 1

    cnt = 0
    for w in weight_cnt_dict.keys():
        if weight_cnt_dict[w] > 1:
            cnt += (weight_cnt_dict[w] - 1) * weight_cnt_dict[w] / 2
        if w * (1 / 2) in weight_cnt_dict:
            cnt += weight_cnt_dict[w * (1 / 2)] * weight_cnt_dict[w]
        if w * (2 / 3) in weight_cnt_dict:
            cnt += weight_cnt_dict[w * (2 / 3)] * weight_cnt_dict[w]
        if w * (3 / 4) in weight_cnt_dict:
            cnt += weight_cnt_dict[w * (3 / 4)] * weight_cnt_dict[w]

    answer = cnt
    print(answer)
    return answer

if __name__ == '__main__':
    pass
