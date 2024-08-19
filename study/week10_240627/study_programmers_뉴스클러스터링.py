"""
    뉴스 클러스터링(문자열, 단순구현, 조건이 좀 까다로움)
    
    "자카드 유사도"
    - 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
    - A,B 모두 공집합일 경우 j(A, B) = 1 
    
    2 <= 문자열 길이 <= 1_000 
    
    문자열  
    2글자씩 끊어서 다중집합을 만든어 자카드 유사도 구하기
    
    영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
    
    *대문자와 소문자의 차이는 무시
    65536을 곱하고 소수부 버리고 정수부만 출력한다.
    
    배울점.
    python str.upper(), lower()은 다른 문자, 공백이 섞여있어도 가능하다.
    chr(), ord() 사용법 알아두기.
"""


# import copy
#
#
# def create_str_set(str):
#     list = []
#     str = str.lower()
#
#     for i in range(len(str) - 1):
#         c1 = str[i]
#         c2 = str[i + 1]
#         if 97 <= ord(c1) <= 122 and 97 <= ord(c2) <= 122:
#             list.append(c1 + c2)
#
#     return list
#
#
# def solution(str1, str2):
#     answer = 0
#
#     set1 = create_str_set(str1)
#     set2 = create_str_set(str2)
#     print(*set1)
#     print(*set2)
#     # 둘다 공집합 일때.
#     if not set1 and not set2:
#         return 1 * 65536
#
#     cnt_inter = 0
#     temp = copy.deepcopy(set2)
#     for e in set1:
#         if e in temp:
#             temp.remove(e)
#             cnt_inter += 1
#
#     cnt_union = len(set1) + len(set2) - cnt_inter
#
#     answer = int((cnt_inter / cnt_union) * 65536)
#     return answer
