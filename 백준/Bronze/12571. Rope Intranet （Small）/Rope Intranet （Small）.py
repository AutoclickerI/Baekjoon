I=lambda:map(int,input().split())
for i in range(*I()):
 [n]=I();r=0;a,b=I()
 if n==2:c,d=I();r+=(a-c)*(b-d)<0
 print(f"Case #{i+1}: {r}")