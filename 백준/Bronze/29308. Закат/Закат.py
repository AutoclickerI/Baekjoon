_,*l=map(str.split,open(0))
print(max(l,key=lambda s:int(s[0])*(s[2]=='Russia'))[1])