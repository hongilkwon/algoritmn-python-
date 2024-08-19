"""
    수강신청(해시맵,)


    수강신청 버튼이 활성화 된 후, 수강신청 버튼을 조금이라도 빨리 누른 학생이 대기목록에 먼저 들어간다.

    이미 대기열에 들어가 있는 상태에서 다시 수강신청 버튼을 누를 경우 대기목록의 맨 뒤로 밀려난다.

    잠시 후 수강신청 버튼이 비활성화 되면, 대기목록에서 가장 앞에 있는 학생부터 자동으로 수강신청이 완료되며,
    수강 가능 인원이 꽉 찰 경우 나머지 대기목록은 무시하고 수강신청을 종료한다.


     L(1 ≤ L ≤ 500_000)

     입력
     버튼을 클릭한 학생의 학번이 "클릭 순서"대로
     출력
     성공한 인원의 학번을 한 줄에 1개씩 출력

     사고과정

     "다시 수강신청 버튼을 누를 경우 대기목록의 맨 뒤로 밀려남"
     -> 순위가 바뀜.

     순서 카운팅 맵을 생성후, value로 정렬한다.
"""

# import sys
#
# input = sys.stdin.readline
#
# k, l = map(int, input().split())
#
# queue = [input().strip() for i in range(l)]
#
# if __name__ == '__main__':
#
#     dic = dict()
#
#     rank = 0
#     for number in queue:
#         dic[number] = rank
#         rank += 1
#
#     sorted_item = sorted(dic.items(), key=lambda item: item[1])
#
#     for i in range(k):
#         if i < len(sorted_item):
#             print(sorted_item[i][0])
#         else:
#             break
