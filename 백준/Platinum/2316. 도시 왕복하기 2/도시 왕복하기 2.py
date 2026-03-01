import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def add_edge(g, fr, to, cap):
    g[fr].append([to, cap, len(g[to])])
    g[to].append([fr, 0,   len(g[fr]) - 1])

def dinic_maxflow(g, s, t):
    n = len(g)
    flow = 0
    INF = 10**18

    while True:
        level = [-1] * n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in g[v]:
                if cap > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)

        if level[t] == -1:
            break

        it = [0] * n
        def dfs(v, pushed):
            if v == t:
                return pushed
            while it[v] < len(g[v]):
                i = it[v]
                to, cap, rev = g[v][i]
                if cap > 0 and level[to] == level[v] + 1:
                    tr = dfs(to, min(pushed, cap))
                    if tr:
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
    # 정점 분할: i를 i_in, i_out으로 쪼갬
    # i_in  = 2*(i-1)
    # i_out = 2*(i-1) + 1
    def IN(i):  return 2 * (i - 1)
    def OUT(i): return 2 * (i - 1) + 1

    V = 2 * N
    g = [[] for _ in range(V)]
    INF = 10**9  # 실제 최대 답은 N 정도라 이 정도면 충분

    # (1,2 제외) "도시를 한 번만 방문"시키려면
    # i_in -> i_out 간선 용량을 1로 두면, 그 도시는 총 1유량만 통과 가능
    for i in range(1, N + 1):
        cap = INF if i == 1 or i == 2 else 1
        add_edge(g, IN(i), OUT(i), cap)

    # 길은 양방향: u <-> v
    # 정점 분할을 했으므로 "도시 u를 지난 다음"은 OUT(u)에서 출발,
    # "도시 v에 들어감"은 IN(v)로 도착.
    for _ in range(P):
        u, v = map(int, input().split())
        add_edge(g, OUT(u), IN(v), INF)
        add_edge(g, OUT(v), IN(u), INF)

    # 소스는 1번 도시에서 '나가는 상태'인 OUT(1)
    # 싱크는 2번 도시로 '들어가는 상태'인 IN(2)
    ans = dinic_maxflow(g, OUT(1), IN(2))
    print(ans)

if __name__ == "__main__":
    main()