M,*s=open(0)
n=int(M.split()[0])
print(sum(any(x[:len(y)-1]in y for x in s[:n])for y in s[n:]))