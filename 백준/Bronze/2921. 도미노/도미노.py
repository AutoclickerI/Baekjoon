l=[0]
for i in range(1,1001):l+=[l[-1]+i*i+(i+1)*(i+2)//2]
n=int(input())
print(l[n]-n)