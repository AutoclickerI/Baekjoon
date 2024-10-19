N=223
Mlim=500000 
Plim=1
Nlim=500000
nodes_used=2*N
div1=300
div2=1

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
        self.count+=need
        return self.node
    def connect(self,f):
        assert len(self)*len(f)<=Plim
        connections.append((self.getnode(len(f)),f.getnode(len(self))))

start=[]
for i in range(1,N+1,div1//div2):
    start+=cluster([*range(i,min(i+div1//div2,N+1))],True),

end=[]
for i in range(1,N+1,div1//div2):
    end+=cluster([*range(N+i,N+min(i+div1//div2,N+1))],False),

for i in range(0,len(start),div2):
    n_e=Plim//div1**2*div2
    for j in range(0,len(end),div2):
        node=getnode()
        for k in start[i:i+div2]:
            connections.append((k.getnode(n_e*div1//div2),node))
        for k in end[j:j+div2]:
            connections.append((node,k.getnode(div1//div2)))
    

assert len(connections)<=Mlim
print(nodes_used,len(connections))
for i in connections:print(*i)