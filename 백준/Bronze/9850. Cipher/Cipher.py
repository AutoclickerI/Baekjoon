s,=open(0,'rb')
print(*[k for j in range(26)if'CHIPMUNKS'in(k:=''.join(chr([i,(i+j-65)%26+65][64<i<91])for i in s))and'LIVE'in k])