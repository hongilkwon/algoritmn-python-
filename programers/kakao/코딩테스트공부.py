"""
    코딩 테스트 공부

    1.알고력 공부 -> +1
    2.코딩력 공부 -> +1
    3.문제풀기

    문제가 요구하는 시간이 필요하며 같은 문제를 "여러 번" 푸는 것이 가능

    0 ≤ alp,cop ≤ 150
    1 ≤ problems의 길이 ≤ 100

    "모든 문제들"을 풀 수 있는 알고력과 코딩력을 얻는 최단시간
    모든 문제들을 1번 이상씩 풀 필요는 없습니다.

    사고과정.

    제한사항의 크기가 큰것은 아니지만, 완전탐색을 생각해보면,
    2개 + problems의 길이.. 너무나 많은 경우의 수를 가진다.

    dp문제

    - table 차원
    - 상향(tabulation)? 하향(memoization)?
    - table 초기값 확정
    - table을 어떻게 채워나갈 것인가!!!

    table[alp][cop] => 최소시간

    * 모든 문제를 해결할 수 있다는 것은 "이상"
    table[alp_max][j]는 알고력이 alp_max "이상", 코딩력 j를 달성하는데 필요한 최소 시간,
    table[i][cop_max]는 알고력 j, 코딩력 cop_max "이상"을 달성하는데 필요한 최소 시간


"""

problems = []
goal_alp, goal_cop = 0, 0

INF = 1_000_000_000

# 0 ≤ alp, cop ≤ 150이면 151이어야 되는데...왜 152???
table = [[INF for _ in range(156)] for _ in range(156)]


def solution(alp, cop, _problems):
    global goal_alp, goal_cop, min_time, problems
    problems = _problems

    answer = 0

    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost  = problem
        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    # 초기값이 이미 모든 문제를 해결한 능력치에 다다른 경우
    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)

    table[alp][cop] = 0

    for a in range(alp, goal_alp + 1):
        for c in range(cop, goal_cop + 1):
            # 알고력과 코딩력을 1씩 공부함.
            table[a+1][c] = min(table[a+1][c], table[a][c] + 1)
            table[a][c+1] = min(table[a][c+1], table[a][c] + 1)
            # 문제풀이.
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                # 현재수치로 풀수 없는 문제라면 넘어감.
                if a < alp_req or c < cop_req: continue

                # table 최대치 처리
                alp_nxt = min(goal_alp, a + alp_rwd)
                cop_nxt = min(goal_cop, c + cop_rwd)

                table[alp_nxt][cop_nxt] = min(table[alp_nxt][cop_nxt], table[a][c] + cost)
    answer = table[goal_alp][goal_cop]
    return answer