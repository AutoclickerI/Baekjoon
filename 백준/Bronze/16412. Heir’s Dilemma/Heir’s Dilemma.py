s,e=map(int,input().split())
print(sum(len(z:=str(i))==len({*z}-{'0'})==sum(i%int(j)<1for j in z)for i in range(s,e+1)))