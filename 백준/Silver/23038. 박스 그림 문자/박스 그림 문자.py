N,M=map(int,input().split())
l=eval('[*input()],'*3*N)
for j in l[1::3]:
    j[1::3]='#'*M
for i in zip(*[''.join(j).replace('#.#','###').replace('#.#','###')for j in zip(*[''.join(i).replace('#.#','###').replace('#.#','###')for i in l])]):print(*i,sep='')