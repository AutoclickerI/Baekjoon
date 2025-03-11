def solve():
    import sys
    input = sys.stdin.readline

    T = int(input().strip())
    
    def compute_pi(s):
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i-1]
            while j > 0 and s[i] != s[j]:
                j = pi[j-1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return pi

    def compute_z(s):
        n = len(s)
        Z = [0] * n
        Z[0] = n
        l, r = 0, 0
        for i in range(1, n):
            if i > r:
                l = r = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                Z[i] = r - l
                r -= 1
            else:
                k = i - l
                if Z[k] < r - i + 1:
                    Z[i] = Z[k]
                else:
                    l = i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    Z[i] = r - l
                    r -= 1
        return Z

    out_lines = []
    for t in range(1, T+1):
        s = input().strip()
        n = len(s)
        pi = compute_pi(s)
        Z = compute_z(s)
        candidate = pi[-1]
        ans = None

        # Ищем по убыванию кандидата (границы, являющиеся одновременно префиксом и суффиксом)
        while candidate > 0:
            if 3 * candidate <= n:
                # Чтобы среднее вхождение не перекрывало префикс [0, candidate-1] и суффикс [n-candidate, n-1],
                # его начало должно лежать в диапазоне [candidate, n - 2*candidate].
                # Проверим, есть ли такое вхождение с помощью Z-функции.
                found = False
                # Обратите внимание: range(start, end) в Python идёт до end-1, а нам нужен диапазон [candidate, n-2*candidate] включительно.
                for i in range(candidate, n - 2 * candidate + 1):
                    if Z[i] >= candidate:
                        found = True
                        break
                if found:
                    ans = s[:candidate]
                    break
            candidate = pi[candidate - 1]
        
        if ans is None:
            out_lines.append(f"Case {t}: -1")
        else:
            out_lines.append(f"Case {t}: {ans}")
    
    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    solve()
