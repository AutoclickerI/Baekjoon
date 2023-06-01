a=list(input())
b=[0]*10
for i in a:
    b[int(i)]+=1
b[6],b[9]=(b[6]+b[9])/2,(b[6]+b[9])/2
b.sort()
print(round(b[-1]+0.1))