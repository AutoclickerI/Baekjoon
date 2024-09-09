for i in[*open(0)][1:]:
    l=len(i.strip())
    N=min(int(i),int('4'+'9'*(l-1)))
    print(N*(int('9'*l)-N))