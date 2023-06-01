d=[0]*5+[1]
for i in range(10**6):d+=[sum(d[i:i+7])/6+1]
print(d[int(input())+4])