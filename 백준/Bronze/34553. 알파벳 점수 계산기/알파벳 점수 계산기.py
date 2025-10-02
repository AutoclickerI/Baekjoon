c=0
print(len(s:=input())+sum(c:=-~c*(i<j)for i,j in zip(s,s[1:])))