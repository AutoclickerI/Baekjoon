R=range(96)
while n:=int(input()):print(max((v:=i**3+j*~j*~-~j//6)*(v<=n)for i in R for j in R))