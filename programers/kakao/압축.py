"""
    압축
    사전에서 현재 입력과 일치하는 가장 긴 문자열 w
    
    
    msg의 길이는 1 글자 이상, 1000 글자 이하
    
    사고과정.
    
    시뮬레이션 문제로 단순구현!


"""

# def solution(msg):
#     answer = []
#
#     lzw_dict = dict()
#     lzw_idx = 1
#     for code in range(65, 91):
#         lzw_dict[chr(code)] = lzw_idx
#         lzw_idx += 1
#
#     # edge case(입력 문자열 길이가 1일때.)
#     if len(msg) == 1:
#         answer.append(lzw_dict[msg[0]])
#         return answer
#
#     cur_str = msg[0]
#     for i in range(1, len(msg)):
#
#         next_str = msg[i]
#
#         # 다음 문자를 추가해 봤을때 사전에 없다면 ==> 현재 입력과 일치하는 가장 긴 문자열
#         if not cur_str + next_str in lzw_dict:
#             answer.append(lzw_dict[cur_str])
#
#             key = cur_str + next_str
#             lzw_dict[key] = lzw_idx
#             lzw_idx += 1
#
#             cur_str = next_str
#         else:
#             cur_str += next_str
#
#         # 더 이상 다음 문자열이 없다면 =>  현재 입력과 일치하는 가장 긴 문자열
#         if i == len(msg) - 1:
#             answer.append(lzw_dict[cur_str])
#
#     return answer
