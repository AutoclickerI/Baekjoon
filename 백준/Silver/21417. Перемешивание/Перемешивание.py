C=input()
exec("l=['','']\nfor i in range(len(C)):l[i%2]+=C[~i]\nC=l[1]+l[0];"*int(input()))
print(C)