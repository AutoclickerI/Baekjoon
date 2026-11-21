I=input
f=[I()for _ in[0]*int(I())]
exec('p,q=map(int,I().split());print(*f[p-1:q]);'*int(I()))