I=input
exec("v=[I().split()for _ in[0]*int(I())];print(''.join(chr(z+64)for i in range(1000)if(z:=sum(int(j)<=i<int(k)for _,j,k in v))));"*int(I()))