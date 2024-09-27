c=open(0).read().count
[print(k,c(k))for j in(97,65)for i in range(26)if c(k:=chr(i+j))]