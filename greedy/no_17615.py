"""
    볼 모으기(틀림, greedy)

    사고과정.

    볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다

    1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다
    2. 옮길 수 있는 볼의 색깔은 한 가지이다

    같은 색끼리 모으되 최소 이동횟수를 찾는 프로그램
    볼의 총 개수 N이 주어진다. (1 ≤ N ≤ 500,000)


    특정색의 공을 한쪽으로 전부 이동 시켜려면,
    왼쪽이든 오른쪽이던 옮기려는 색을 한쪽에 많이 몰려있는 쪽으로 옮겨야 최소 이동을할 수 있다.
    만약 양쪽에 옮기려는 공과 같은 색이 없다면, 공의 갯수만큼 옮겨야한다.

"""



import sys

input = sys.stdin.readline

n = int(input())
arr = input().rstrip()


def count_side_ball(color):
    l_side_cnt = 0
    for c in arr:
        if c == color:
            l_side_cnt += 1
        else:
            break

    r_side_cnt = 0
    for c in arr[::-1]:
        if c == color:
            r_side_cnt += 1
        else:
            break

    return max(l_side_cnt, r_side_cnt)

if __name__ == '__main__':

    cnt_red = 0
    cnt_blue = 0

    # 전체 배열에서 각 색깔의 갯수
    for c in arr:
        if c == 'R':
            cnt_red += 1
        if c == 'B':
            cnt_blue += 1
    
    side_cnt_red = count_side_ball('R')
    side_cnt_blue = count_side_ball('B')

    min_red = cnt_red - side_cnt_red
    min_blue = cnt_blue - side_cnt_blue

    print(min(min_red, min_blue))