N=max(k:=int(input()),~k)
print(['short','int','long '*2][(N>>15>0)+(N>>31>0)])