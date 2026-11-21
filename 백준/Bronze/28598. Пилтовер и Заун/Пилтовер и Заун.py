x,y,n=map(int,input().split())
q,r=divmod(x-y,2)
print("YNEOS"[r>0 or q<n::2])