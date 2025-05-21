_,s=open(0)
print(len(s)-2-s.count('][')+sum(i+j in'22 55'for i,j in zip(s,s[1:])))