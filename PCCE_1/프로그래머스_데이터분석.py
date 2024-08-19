"""
    [PCCE 기출문제] 10번 데이터분석

    data에서 ext 값이 val_ext보다 "작은 데이터"만 뽑은 후,
    sort_by에 해당하는 값을 기준으로 "오름차순"으로 정렬하여 return 하도록 solution 함수를 완성
"""

# dic = {
#     "code": 0,
#     "date": 1,
#     "maximum": 2,
#     "remain": 3
# }
#
#
# def solution(data, ext, val_ext, sort_by):
#     answer = []
#     idx = dic[ext]
#     for d in data:
#         if d[idx] < val_ext:
#             answer.append(d)
#
#     answer.sort(key=lambda x: x[dic[sort_by]])
#     return answer
