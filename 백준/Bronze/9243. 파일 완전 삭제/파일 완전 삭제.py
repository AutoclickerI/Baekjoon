n,a,b=open(0)
print('Deletion',['failed','succeeded'][int(n)%2*~-len(a)==(int(a,2)^int(b,2)).bit_count()])