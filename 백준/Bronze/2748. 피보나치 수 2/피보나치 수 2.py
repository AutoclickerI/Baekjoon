F = [0, 1];n = int(input())
for _ in range(n - 1):
    F.append(F[-1] + F[-2])
print(F[n])