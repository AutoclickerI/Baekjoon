d=[0,1]
for i in[0]*10**6:d+=[sum(d[-6:])/6+1]
print(d[int(input())])