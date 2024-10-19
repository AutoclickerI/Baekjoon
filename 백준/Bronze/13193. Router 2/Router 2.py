N=223
Mlim=500000
Plim=100
Nlim=500000
nodes_used=2*N
div1=3
div2=3

connections=[]

def getnode():
    global nodes_used
    nodes_used+=1
    assert nodes_used<=Nlim
    return nodes_used

class cluster:
    def __init__(self,l,head):
        self.l=l
        self.head=head
        self.reset()
    def reset(self):
        self.node=getnode()
        if self.head:
            for i in self.l:
                connections.append((i,self.node))
        else:
            for i in self.l:
                connections.append((self.node,i))
        self.count=0
    def __len__(self):
        return len(self.l)
    def connect(self,f):
        assert len(self)*len(f)<=Plim
        if Plim<len(self)*(self.count+len(f)):
            self.reset()
        self.count+=len(f)
        if Plim<len(f)*(f.count+len(self)):
            f.reset()
        f.count+=len(self)
        connections.append((self.node,f.node))

class cluster_2:
    def __init__(self,l,head):
        self.l=l
        self.head=head
        self.reset(True)
        self.len=sum(map(len,l))
    def reset(self,init=False):
        self.node=getnode()
        if self.head:
            for i in self.l:
                if not init:
                    i.reset()
                connections.append((i.node,self.node))
        else:
            for i in self.l:
                if not init:
                    i.reset()
                connections.append((self.node,i.node))
        self.count=0
    def __len__(self):
        return self.len
    def connect(self,f):
        assert len(self)*len(f)<=Plim
        if Plim<len(self)*(self.count+len(f)):
            self.reset()
        self.count+=len(f)
        if Plim<len(f)*(f.count+len(self)):
            f.reset()
        f.count+=len(self)
        connections.append((self.node,f.node))

start=[]
for i in range(1,N+1,div1):
    start+=cluster([*range(i,min(i+div1,N+1))],True),

end=[]
for i in range(1,N+1,div1):
    end+=cluster([*range(N+i,N+min(i+div1,N+1))],False),

start_2=[]
for i in range(0,len(start),div2):
    start_2+=cluster_2(start[i:i+div2],True),

end_2=[]
for i in range(0,len(end),div2):
    end_2+=cluster_2(end[i:i+div2],False),

for i in start_2:
    for j in end_2:
        i.connect(j)
assert len(connections)<=Mlim
print(nodes_used,len(connections))
for i in connections:print(*i)