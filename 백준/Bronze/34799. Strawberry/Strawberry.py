v=[0]*26
for i in input():v[ord(i)-114]+=1
n=int(input())
print(n//26*sum(v)+sum(v[:n%26]))