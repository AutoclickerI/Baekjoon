a,b=max(zip(s:=sorted(map(int,[*open(0)][1].split())),s[1:]),key=lambda x:x[1]-x[0]>>1)
print([-1,a+b>>1][b-a>1])