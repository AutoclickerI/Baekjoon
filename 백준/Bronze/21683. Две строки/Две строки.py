s,t=input()*2,input()*2
p,q=len(s)//2,len(t)//2
print(max(int(s[i:i+p])for i in range(p))-min(int(t[i:i+q])for i in range(q)if'0'<t[i]))