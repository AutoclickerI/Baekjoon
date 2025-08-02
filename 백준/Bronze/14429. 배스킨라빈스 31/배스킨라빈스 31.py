i=0
print(*min(((a+b)//-~b*2,i:=i+1)for a,b in[map(int,i.split())for i in open(0)][1:])[::-1])