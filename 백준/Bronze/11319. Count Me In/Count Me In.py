for i in[*open(0)][1:]:v=''.join(i.split());n=sum(map(v.count,'AaEeIiOoUu'));print(len(v)-n,n)