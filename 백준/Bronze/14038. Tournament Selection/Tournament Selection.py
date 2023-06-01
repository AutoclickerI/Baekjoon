n=0
for i in[0]*6:
 if input()=='W':n+=1
print(-1 if n==0 else'3'if n<3 else'2'if n<5 else 1)