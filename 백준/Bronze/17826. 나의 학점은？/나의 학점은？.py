n=[*map(int,input().split())].index(int(input()))
if n<5:
    v='A+'
elif n<15:
    v='A0'
elif n<30:
    v='B+'
elif n<35:
    v='B0'
elif n<45:
    v='C+'
elif n<48:
    v='C0'
else:
    v='F'
print(v)