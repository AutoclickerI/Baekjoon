A,B,C,*l=map(int,input().split())
t=10**len(str(C))
i=1
S=A*B%t
while C!=S not in l[:-1]:S=S*B%t;l+=S,;i+=1
print(S-C and'NIKAD'or i)