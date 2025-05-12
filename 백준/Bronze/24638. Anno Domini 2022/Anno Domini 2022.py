a,b=[eval(i.replace('AD','').replace('BC','*-1+1'))for i in open(0)]
print(abs(a-b))