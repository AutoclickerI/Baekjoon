K,L,*l=open(0).read().split()
print(*[*{*l[::-1]}][:~int(K):-1])