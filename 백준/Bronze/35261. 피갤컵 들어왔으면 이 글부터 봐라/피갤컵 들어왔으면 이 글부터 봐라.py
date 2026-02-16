_,s=open(0)
print(min(sum(map(str.__ne__,'eagle',s[k:]))for k in range(len(s)-5)))