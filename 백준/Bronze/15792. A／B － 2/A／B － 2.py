a,b=map(int,input().split())
print(f'{a//b}.{a%b*10**1000//b:01000d}')