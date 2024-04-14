i,s=open(0)
N,_=map(int,i.split())
print(len({s[i:i+N]for i in range(len(s)-N)}))