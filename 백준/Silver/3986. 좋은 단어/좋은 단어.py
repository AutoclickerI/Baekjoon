a=0
for _ in[0]*int(input()):
    s=[]
    for i in input():
        if s==[] or s[-1]!=i:
            s+=i
        elif s and s[-1]==i:
            s.pop()
    a+=s==[]
print(a)