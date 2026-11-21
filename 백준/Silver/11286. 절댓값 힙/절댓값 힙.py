from heapq import*
h=[]
for n in[*open(0)][1:]:heappush(h,(abs(a),a))if(a:=int(n))else print(len(h)and heappop(h)[1])