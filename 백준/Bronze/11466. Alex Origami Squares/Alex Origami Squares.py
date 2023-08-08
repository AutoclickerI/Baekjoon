a,b=map(int,input().split())
if a>b:a,b=b,a
print(max(min(a,b/3),a/2))