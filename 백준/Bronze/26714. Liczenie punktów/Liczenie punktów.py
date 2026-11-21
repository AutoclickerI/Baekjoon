n,s=open(0)
t=int(n)//10
print(sum(t*'T'==s[i:i+t]for i in range(0,len(s),t)))