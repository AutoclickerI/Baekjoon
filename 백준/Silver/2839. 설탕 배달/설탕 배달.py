a = [1, 2, 4, 7]
n = int(input())
if n in a:
    print(-1)
else:
    b = 0
    c = (n + 2) // 5  
    b += c * 5
    while b != n:
        while b > n:
            b -= 2
        if b != n:
            b += 5
            c += 1
    print(c)