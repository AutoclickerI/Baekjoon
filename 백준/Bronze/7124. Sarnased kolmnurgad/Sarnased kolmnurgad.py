def fetch():
    a,b,c,d,e,f=map(int,input().split())
    return sorted(map(abs,[a-c+(b-d)*1j,c-e+(d-f)*1j,e-a+(f-b)*1j]))
a,b,c=fetch()
d,e,f=fetch()
eps=10**-6
scale=[a/d,b/e,c/f]
if max(scale)<min(scale)+eps:
    print(scale[0])
else:
    print(-1)