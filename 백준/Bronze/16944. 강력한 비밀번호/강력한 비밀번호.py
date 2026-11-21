import re
N,S=open(0)
print(max(6-int(N),sum(not re.search(x,S)for x in['\d','[a-z]','[A-Z]','[!@#$%^&*()-+]'])))