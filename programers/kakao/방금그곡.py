"""
    방금그곡

    한곡을 반복해서 재생

    시작 -- 끝 시작 -- 끝

    한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도,
    그 곡이 네오가 들은 곡이 아닐 수도 있다

    네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교


    사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개

    각 음은 "1분에 1개씩 재생"된다

    음악은 반드시 "처음부터 재생"되며,
    음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 "처음부터 반복해서 재생"된다

    음악이 00:00를 넘겨서까지 재생되는 일은 없다.

    조건이 일치하는 음악이 여러 개일 때에는 라디오에서 "재생된 시간이 제일 긴" 음악 제목을 반환
    재생된 시간도 같을 경우 "먼저 입력된" 음악 제목을 반환한다.

    조건이 일치하는 음악이 없을 때에는 “(None)”을 반환

    1<= m <= 1439

    사고과정.

    100개의 노래 1439개 문자열 확인
    완전탐색 단순구현.

    문제를 똑바로 이해안하고 풀면 한 없이 틀리게 되어있음...


"""


# def convert(idx, info):
#     s, e, name, music = info
#     start_time = int(s[:2]) * 60 + int(s[3:])
#     end_time = int(e[:2]) * 60 + int(e[3:])
#
#     runtime = end_time - start_time
#
#     music = music.replace('A#', '1').replace('C#', '2').replace('D#', '3').replace('F#', '4').replace('G#', '5')
#     if len(music) < runtime:
#         # 악보정보 < 런타임
#         music += music * (runtime // len(music)) + music[:runtime % len(music)]
#     elif len(music) > runtime:
#         # 악보정보 > 런타임
#         music = music[:runtime]
#
#     return idx, runtime, name, music
#
#
# def solution(m, musicinfos):
#     answer = ''
#
#     convertd_musicinfos = []
#     for i, info in enumerate(musicinfos):
#         convertd_musicinfos.append(convert(i, info.split(",")))
#     # print(*convertd_musicinfos)
#
#     temp = []
#     m = m.replace('A#', '1').replace('C#', '2').replace('D#', '3').replace('F#', '4').replace('G#', '5')
#     for info in convertd_musicinfos:
#         if m in info[3]:
#             temp.append(info)
#
#     if temp:
#         temp.sort(key=lambda x: (-x[1], x[0]))
#         answer = temp[0][2]
#     else:
#         answer = "(None)"
#     # print(answer)
#     return answer
#
# if __name__ == '__main__':
#     solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
