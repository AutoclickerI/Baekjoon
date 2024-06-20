n,w,h=map(int,input().split())
*l,s=eval("eval(('+input()'*h)[1:]),"*-~n)
x=0
print(min([sum(j!=k for j,k in zip(s,i)),x:=x+1]for i in l)[1])