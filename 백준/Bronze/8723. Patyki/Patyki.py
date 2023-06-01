a=sorted(list(map(int,input().split())))
print(2 if a[0]==a[-1]else 1 if a[0]**2+a[1]**2==a[2]**2 else 0)