a,b,c,d=map(int,input().split())
print(min(abs(a+b-c-d),abs(a+c-b-d),abs(b+c-a-d)))