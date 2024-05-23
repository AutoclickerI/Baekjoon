f=lambda:{*input().split()}
f()
print(len(s:=f()&f()),*sorted(s,key=int))