a,b,c=list(map(int,input().split()))
n=(a-11)*24*60+(b-11)*60+c-11
print(n if n>-1 else -1)