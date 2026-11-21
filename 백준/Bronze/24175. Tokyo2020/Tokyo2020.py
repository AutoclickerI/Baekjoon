s=range(2022)
while n:=int(input()):d=[[0,0]for i in s];exec("v,w,x=input().split();d[int(v)][x[0]=='G']+=1;"*n);print(max(s,key=lambda i:d[i][1]),max(s,key=lambda i:sum(d[i])))