i,s=open(0)
N=int(i.split()[0])
print(len({s[i:i+N]for i in range(len(s)-N)}))