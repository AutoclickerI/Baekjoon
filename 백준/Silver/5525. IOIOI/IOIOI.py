import re
n,_,s=open(0)
print(sum(max(len(s)//2-int(n)+1,0)for s in re.findall('(?:IO)*I',s)))