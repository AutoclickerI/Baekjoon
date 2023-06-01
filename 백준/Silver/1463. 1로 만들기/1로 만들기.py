d=[-1]
for i in range(1,int(input())+1):d+=[min(d[i//3]+i%3,d[i//2]+i%2,d[i-1])+1]
print(d[-1])