from heapq import*
i=heappush
o=heappop
l,r=[],[]
for a in[*open(0)][1:]:i(l,-int(a));i(r,-o(l));len(r)==len(l)or i(l,-o(r));print(-l[0])