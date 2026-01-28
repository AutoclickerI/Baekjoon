b=[1]
for i in range(9**6):b+=b[i]+b[i+1>>1],
print(b[int(input())//2]%10**9)