a,f=1000000,[0, 1];p=a//10*15
for i in range(2,p):f.append(f[i-1]+f[i-2]);f[i]%=a
print(f[int(input())%p])