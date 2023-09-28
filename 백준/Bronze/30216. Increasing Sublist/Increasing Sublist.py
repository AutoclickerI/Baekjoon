e=s=m=0
for i in map(int,[*open(0)][1].split()):
    if e<i:
        s+=1
        m=max(m,s)
    else:
        s=1
    e=i
print(m)      