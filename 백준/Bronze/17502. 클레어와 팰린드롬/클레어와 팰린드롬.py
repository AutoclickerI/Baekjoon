_,s=open(0)
print(*map(max,s,s[-2::-1],'a'*100),sep='')