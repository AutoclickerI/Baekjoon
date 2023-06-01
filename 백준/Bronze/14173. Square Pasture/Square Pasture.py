a,b,c,d=map(int,input().split())
e,f,g,h=map(int,input().split())
print(max(max(c,g)-min(a,e),max(d,h)-min(b,f))**2)