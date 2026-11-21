while'0'<input():
 S=0;T=[11]*3
 for p in 1,-1:
  a=b=c=n=0
  for i in input().split():
   n+=1;a,b,c=b,c,int(i);S+=c*p
   if a==b==c:T[p]=min(T[p],n)
 S-=30*((T[1]>T[2])-(T[1]<T[2]));print('T'*(S==0)or'LM'[S>0])