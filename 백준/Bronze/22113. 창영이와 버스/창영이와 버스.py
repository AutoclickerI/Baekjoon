_,b,*c=map(str.split,open(0))
print(sum(int(c[int(i)-1][int(j)-1])for i,j in zip(b,b[1:])))