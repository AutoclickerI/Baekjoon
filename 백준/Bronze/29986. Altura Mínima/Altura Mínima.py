H,A=open(0)
print(sum(eval(i+'<='+H[2:])for i in A.split()))