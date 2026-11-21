k=1
f=sorted
while(i:=input())>'F':print(f'Case {k}:',['same','different'][f(i)!=f(input())]);k+=1