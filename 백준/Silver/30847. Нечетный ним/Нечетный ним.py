for b in[*open(a:=0)][1].split():a^=int(b)&1
print(*['Gleb','Misha'][::1-2*a])