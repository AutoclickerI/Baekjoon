import re
N,S=6-int(input()),input()
print(max(N,sum(not re.search(x,S)for x in['[\d]','[a-z]','[A-Z]','[!@#$%^&*()-+]'])))