a,b,c=map(int,input().split())
print(max(-1,round(((a-b*b/a)*(a-c*c/a))**.5-b*c/a)))