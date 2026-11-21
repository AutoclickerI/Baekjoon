f=lambda:map(int,input().split())
for T in range(*f()):n,m=f();l=eval('int(input()),'*n);s=0;exec('h,w,d,i=f();s+=h*w*d*l[i-1];'*m);print(f'Data Set {T+1}:\n{s}')