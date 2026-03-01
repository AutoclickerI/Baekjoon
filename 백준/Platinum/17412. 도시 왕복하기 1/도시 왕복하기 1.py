import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# ---------------------------
# Dinic (클래스 없이, 리스트로 구현)
# g[u] = [[to, cap, rev], ...]
#  - to  : 도착 정점
#  - cap : 남은 용량(Residual capacity)
#  - rev : 반대 간선이 g[to]에서 몇 번째 인덱스인지
# ---------------------------
def add_edge(g, fr, to, cap):
    g[fr].append([to, cap, len(g[to])])      # 정방향 간선
    g[to].append([fr, 0,   len(g[fr]) - 1])  # 역방향(처음 용량 0)

def dinic_maxflow(g, s, t):
    n = len(g)
    flow = 0
    INF = 10**18

    while True:
        # 1) BFS로 레벨 그래프 구성: s에서 각 정점까지 최단(간선 수) 레벨
        level = [-1] * n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in g[v]:
                if cap > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)

        # t에 도달 불가면 더 이상 증가 경로가 없음 -> 종료
        if level[t] == -1:
            break

        # 2) DFS로 blocking flow 찾기 (레벨 그래프 위에서만 흘림)
        it = [0] * n  # 각 정점에서 다음에 탐색할 간선 위치(현재 호)
        def dfs(v, pushed):
            if v == t:
                return pushed
            while it[v] < len(g[v]):
                i = it[v]
                to, cap, rev = g[v][i]
                if cap > 0 and level[to] == level[v] + 1:
                    tr = dfs(to, min(pushed, cap))
                    if tr:
                        # 유량을 흘렸으니 잔여 용량 갱신
                        g[v][i][1] -= tr
                        g[to][rev][1] += tr
                        return tr
                it[v] += 1
            return 0

        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            flow += pushed

    return flow

def main():
    N, P = map(int, input().split())
    # 17412는 정점이 1..N 이므로 편하게 N+1로 잡고 0은 비움
    g = [[] for _ in range(N + 1)]

    # 각 길(간선)은 "한 경로에서 쓰였으면 다른 경로에서 못 씀" -> 용량 1
    for _ in range(P):
        u, v = map(int, input().split())
        add_edge(g, u, v, 1)

    # 1번에서 2번으로 갈 수 있는 "서로 간선이 겹치지 않는" 경로 최대 개수 = maxflow
    ans = dinic_maxflow(g, 1, 2)
    print(ans)

if __name__ == "__main__":
    main()