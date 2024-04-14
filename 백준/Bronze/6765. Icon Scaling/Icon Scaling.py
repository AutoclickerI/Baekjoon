n=int(input())
*map(lambda s:exec("print(*[i*n for i in s],sep=''),"*n),['*x*',' xx','* *']),