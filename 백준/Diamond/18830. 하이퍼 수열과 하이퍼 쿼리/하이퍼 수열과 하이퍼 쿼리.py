import sys
input=sys.stdin.readline

m,n,o,p,q,r,s,t,u,v,w=map(int,input().split())
arr=[[[[[[[[[[[*map(int,input().split())]for _ in[0]*v]for _ in[0]*u]for _ in[0]*t]for _ in[0]*s]for _ in[0]*r]for _ in[0]*q]for _ in[0]*p]for _ in[0]*o]for _ in[0]*n]for _ in[0]*m]
        
ps=[[[[[[[[[[w[:]for w in v]for v in u]for u in t]for t in s]for s in r]for r in q]for q in p]for p in o]for o in n]for n in arr]

def push(skip_ax):
    for mi in range(m):
        for ni in range(n):
            for oi in range(o):
                for pi in range(p):
                    for qi in range(q):
                        for ri in range(r):
                            for si in range(s):
                                for ti in range(t):
                                    for ui in range(u):
                                        for vi in range(v):
                                            for wi in range(w):
                                                aidx=[mi,ni,oi,pi,qi,ri,si,ti,ui,vi,wi]
                                                if aidx[skip_ax]:
                                                    aidx[skip_ax]-=1
                                                    mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww=aidx
                                                    ps[mi][ni][oi][pi][qi][ri][si][ti][ui][vi][wi]+=ps[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww]

for skip_ax in range(11):
    push(skip_ax)

for _ in[0]*int(input()):
    a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2=map(int,input().split())
    r=0
    for a,af in(a1-2,-1),(a2-1,1):
        if 0<=a:
            for b,bf in(b1-2,-1),(b2-1,1):
                if 0<=b:
                    for c,cf in(c1-2,-1),(c2-1,1):
                        if 0<=c:
                            for d,df in(d1-2,-1),(d2-1,1):
                                if 0<=d:
                                    for e,ef in(e1-2,-1),(e2-1,1):
                                        if 0<=e:
                                            for f,ff in(f1-2,-1),(f2-1,1):
                                                if 0<=f:
                                                    for g,gf in(g1-2,-1),(g2-1,1):
                                                        if 0<=g:
                                                            for h,hf in(h1-2,-1),(h2-1,1):
                                                                if 0<=h:
                                                                    for i,iif in(i1-2,-1),(i2-1,1):
                                                                        if 0<=i:
                                                                            for j,jf in(j1-2,-1),(j2-1,1):
                                                                                if 0<=j:
                                                                                    for k,kf in(k1-2,-1),(k2-1,1):
                                                                                        if 0<=k:
                                                                                            r+=ps[a][b][c][d][e][f][g][h][i][j][k]*af*bf*cf*df*ef*ff*gf*hf*iif*jf*kf
    print(r)