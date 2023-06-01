a = []
for i in range(10):
    n = int(input())
    if n%42 in a:
        pass
    else:
        a.append(n%42)
print(len(a))
        