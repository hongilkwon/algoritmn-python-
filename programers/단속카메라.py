"""
    단속 카메라

    "모든" 차량이 고속도로를 이용하면서 단속용 카메라를 "한 번"은 만나도록 카메라를 설치
    모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return


    1 <= 차량의 대수 <= 10_000
    -30,000 <= 진출 지점 <= 30_000

    사고과정.

    고속도로 진입구간(시작과 끝 특정 구간)을 포함하는지 안하는지 판별한다??

    최소한으로 카메라를 설치해야된다 즉, 어떤 상황에서 설치를 해야되는가?



    * 강의실 배정, 회의실 배정, 택배문제 참고

"""


# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: (x[1]))
#     # print(*routes)
#
#     e = routes[0][1]
#     cnt = 1
#     for i in range(1, len(routes)):
#         route = routes[i]
#
#         if route[0] <= e:
#             continue
#         else:
#             e = route[1]
#             cnt += 1
#
#     answer = cnt
#     print(cnt)
#     return answer
