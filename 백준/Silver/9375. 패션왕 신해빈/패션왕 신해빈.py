I=input
exec('l=[I().split()[1]for _ in[0]*int(I())];r=1\nfor i in map(l.count,{*l}):r*=i+1\nprint(r-1);'*int(I()))