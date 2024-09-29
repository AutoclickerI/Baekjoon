c=1
while c:a,b,c=map(int,input().split());a+b and exec('a,b=b,a+b;'*c);c>0!=print(b)