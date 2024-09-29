c=1
while c:a,b,c=map(int,input().split());exec('a,b=b,a+b;'*min(c,99));c>0!=print(b)