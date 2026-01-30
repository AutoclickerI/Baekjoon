[K],_,*l=[map(int,i.split())for i in open(0)]
for M,N in l:print(+(M-K-3<N-M<K-N+2))