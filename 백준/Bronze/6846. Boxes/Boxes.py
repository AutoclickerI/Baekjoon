f=lambda:map(int,input().split())
B=eval('sorted(f()),'*int(input()))
for _ in[0]*int(input()):L,W,H=sorted(f());l=[l*w*h for l,w,h in B if L<=l and W<=w and H<=h];print(min(l)if l else'Item does not fit.')