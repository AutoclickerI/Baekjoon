p=q=0
print(-sum((p:=min(q+(q:=min(-p,v:=int(i)))-v,0))-v*2for i in[*open(0)][1].split()))