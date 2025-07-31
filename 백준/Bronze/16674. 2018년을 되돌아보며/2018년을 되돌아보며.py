t='2018'
f=sorted
print(6*(f(s:=input())==f(len(s)//4*t))+({*s}<={*t})+({*s}=={*t}))