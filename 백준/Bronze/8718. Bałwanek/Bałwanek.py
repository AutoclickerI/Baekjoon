a,b=list(map(int,input().split()))
print(b*7*1000 if b*7<=a else b*7*500 if b*7<=2*a else b*7*250 if b*7<=4*a else 0)