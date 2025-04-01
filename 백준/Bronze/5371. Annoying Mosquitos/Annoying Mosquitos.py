f=lambda:[*map(int,input().split())]
r=range
for T in r(*f()):m,h=[f()for i in r(*f())],[f()for i in r(*f())];print(sum(any([abs(v-x)<51>abs(w-y)for v,w in h])for x,y in m))