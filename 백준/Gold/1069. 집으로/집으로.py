X,Y,D,T=map(int,input().split())
print(min(v:=abs(X+Y*1j),abs(D-v)+T,max(z:=v//D*T,T)+T,z+v%D))