N=223
Mlim=500000 
Plim=100
Nlim=500000
nodes_used=2*N
div1=div2=5

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
    def getnode(self,need):
        if Plim<self.count+need:
            self.reset()
        return self.node
    def connect(self,f):
        assert len(self)*len(f)<=Plim
        connections.append((self.getnode(len(f)),f.getnode(len(self))))
        self.count+=len(f)
        f.count+=len(self)

start=[]
for i in range(1,N+1,div1):
    start+=cluster([*range(i,min(i+div1,N+1))],True),

end=[]
for i in range(1,N+1,div1):
    end+=cluster([*range(N+i,N+min(i+div2,N+1))],False),

for i in start:
    for j in end:
        i.connect(j)
assert len(connections)<=Mlim
print(nodes_used,len(connections))
for i in connections:print(*i)