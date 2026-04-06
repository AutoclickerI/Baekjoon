N,*b=map(int,open(0).read().split())

r=[[]for _ in[0]*N]
cnt=[0]*N
st=[]
st2=[]
for i in range(N):
    while st and b[st[-1]]<=b[i]:
        st.pop()
    cnt[i]+=len(st)
    if st:
        r[i]+=st[-1],
    st+=i,
    while st2 and b[~st2[-1]]<=b[~i]:
        st2.pop()
    cnt[~i]+=len(st2)
    if st2:
        r[~i]+=N-st2[-1]-1,
    st2+=i,

for ix,i in enumerate(r):
    if i:
        print(cnt[ix],min(i,key=lambda x:(abs(x-ix),x))+1)
    else:
        print(0)