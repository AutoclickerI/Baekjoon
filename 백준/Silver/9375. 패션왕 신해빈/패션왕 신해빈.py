I=input
exec('l=[I().split()[1]for _ in[0]*int(I())];r=1\nfor e in{*l}:r*=l.count(e)+1\nprint(r-1);'*int(I()))