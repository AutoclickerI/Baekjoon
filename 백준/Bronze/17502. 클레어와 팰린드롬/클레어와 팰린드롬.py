n,s=open(0)
print(''.join(max(s[i],s[-i-2],'a')for i in range(int(n))))