n=[1,1]
exec('n+=[n[-2]+n[-1]];'*45)
for i in[*open(0)][1:]:print(n[int(i)])