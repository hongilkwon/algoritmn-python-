"""
    싸이버 개강 총회(단순구현)

    ------ 총회 시작 ------ 총회 끝 ------ 스트리밍 끝


    1)
    학회원의 입장 여부는 개강총회가 시작한 시간 이전에 대화를 한 적이 있는 학회원의 닉네임을 보고 체크한다.
    개강총회를 시작하자마자 채팅 기록을 남긴 학회원도 제 시간에 입장이 확인된 것으로 간주

    2)
    강총회가 끝나고 스트리밍이 끝날 때까지 대화를 한 적이 있는 학회원의 닉네임을 보고 체크
    개강총회가 끝나자마자 채팅 기록을 남겼거나, 개강총회 스트리밍이 끝나자마자 채팅 기록을 남긴 학회원도 제 시간에 퇴장이 확인된 것으로 간주


    (00:00 ≤ S < E < Q ≤ 23:59)


"""

# import sys
#
#
# input = sys.stdin.readline
#
# S, E, Q = map(str, input().split(' '))
# chat_list = list()
#
#
# def convertTime(s):
#     temp_list = s.split(':')
#     h = int(temp_list[0])
#     m = int(temp_list[1])
#
#     return (h * 60) + m
#
#
# while True:
#     temp = list(map(str, input().split()))
#
#     if len(temp) == 0:
#         break
#
#     chat_list.append((convertTime(temp[0]), temp[1]))
#
#
# if __name__ == '__main__':
#
#     start_persons = set()
#
#     for chat in chat_list:
#         if chat[0] in range(0, convertTime(S)+1):
#             start_persons.add(chat[1])
#
#         if  chat[0] > convertTime(S):
#             break
#
#     end_persons = set()
#
#     for chat in chat_list:
#         if chat[0] in range(convertTime(E), convertTime(Q)+1):
#             end_persons.add(chat[1])
#
#     ret = start_persons.intersection(end_persons)
#     # print(ret)
#     print(len(ret))