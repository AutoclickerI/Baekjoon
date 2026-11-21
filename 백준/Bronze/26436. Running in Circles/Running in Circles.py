def norm(x, L):
    q, r = divmod(abs(x), L)
    return (q, (r if x >= 0 else -r))

def running_in_cycles():
    L, N = map(int, input().split())
    result = curr = 0
    for _ in range(N):
        D, C = list(input().split())
        D = int(D)
        curr += D if C == 'C' else -D
        cnt, curr = norm(curr, L)
        result += cnt
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, running_in_cycles()))