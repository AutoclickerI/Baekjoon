N,M=map(int,input().split())
l=eval('[*input()],'*3*N)
f=lambda s:''.join(s).replace('#.#','###')
for j in l[1::3]:j[1::3]='#'*M
for i in zip(*[f(f(j))for j in zip(*[f(f(i))for i in l])]):print(*i,sep='')