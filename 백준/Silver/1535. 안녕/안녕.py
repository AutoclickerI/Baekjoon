d=[0]*100
for p,q in zip(*[*map(str.split,open(0))][1:]):d=[max(d[j],(d[v:=j-int(p)]+int(q))*(0<=v))for j in range(100)]
print(max(d))