"""
    아날로그 시계(복잡구현, 수학)

    초침이
    시침/분침과 겹칠 때마다 알람이 울리는 기능이 있습니다.
    당신은 특정 시간 동안 알람이 울린 횟수를 알고 싶습니다.


    시침, 분침, 초침이 움직이는 "속도는 일정"하며 각각 다릅니다.
    시간이 23시 59분 59초를 초과해서 0시 0분 0초로 돌아가는 경우는 주어지지 않습니다.

    문제가 논리적으로 해결은 가능하나 생각을 하는게 쉽지 않다.
    예제를 이해도 쉽지 않다.

    1.각도를 계산하여 해결한다.(풀이가 너무 복잡하다. 생각하는 것, 코드작성 시간까지 고려하면 시간내에 풀기가 불가능함)

         1초     |  1분   | 1시간
    초침  6도     | 360도  |  -
    분침  0.1도   |  6도   | 360
    시침  1/120도 | 1/2도  | 30

    2. 단순 횟수를 계산해 본다.

    1. "최소단위"로 단위 통일한다.

    2. 시간이 정해져 있다. 즉, 0시 0분 0초 - 23시 59분 59초 까지

    * 예외) 정각 즉 0시 0분 0초, 12시 0분 0초  --> 1번만 울림.


"""


# def calDegree(time):
#     h_degree = time[0] * 30 + time[1] * (1 / 2) + time[2] * (1 / 120) % 360
#     m_degree = time[1] * 6 + time[2] * (1 / 10)
#     s_degree = time[2] * 5
#     return

# def to_second(h, m, s):
#     return h * 60 * 60 + m * 60 + s
#
#
# # 0시 0분 0초에서 입력으로 주어진 시간까지 총 울린 알람 횟수 계산
# def count_alarm(second):
#     # 시계의 분침이 1바퀴를 회전 하는데 걸리는 시간 => 1시간 => 3600초
#     # 시계의 분침이 1바퀴를 회전 하는데 초침과 만나는 횟수 => (60번-1번) => 59번
#     cntM = int(second / 3600 * 59)
#
#     # 시계의 시침이 1바퀴를 회전 하는데 걸리는 시간 => 12시간 => 3600*12 => 43200초
#     # 시계의 시침이 1바퀴를 회전 하는데 초침과 만나는 횟수 => (720번-1번) => 719번
#     cntH = int(second / 43200 * 719)
#
#     # 12시 0분 0초에 알람은 분침/시침 모두 카운트 되기 때문에, 1번은 빼줘야함.
#     # 정각 0시 0분 0초는 무조건 카운트됨.
#     cntNoon = 2 if second >= 43200 else 1
#
#     return (cntM + cntH) - cntNoon
#
#
# def solution(h1, m1, s1, h2, m2, s2):
#     start_time = to_second(h1, m1, s1)
#     end_time = to_second(h2, m2, s2)
#
#     answer = count_alarm(end_time) - count_alarm(start_time)
#
#     # 시작할때 부터 알람이 울린다면 1을 더 해준다.
#     if start_time % 3600 == 0 or start_time % 43200 == 0:
#         answer += 1
#
#     return answer
