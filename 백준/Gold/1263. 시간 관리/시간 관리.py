s=1e9
for S,T in sorted([*map(int,i.split())][::-1]for i in[*open(0)][1:])[::-1]:s=min(s,S)-T
print(max(s,-1))