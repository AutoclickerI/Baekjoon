import sys
sys.setrecursionlimit(10**6)

class node:
    def __init__(self,cur):
        self.cur=cur
        self.left=None
        self.right=None

n,*l=map(int,open(0))
root=node(n)
ptr=0

def build(cur,par):
    global ptr
    v=l[ptr]
    if v<cur.cur:
        cur.left=node(v)
        ptr+=1
        build(cur.left,cur.cur)
    v=l[ptr]
    if cur.cur<v<par:
        cur.right=node(v)
        ptr+=1
        build(cur.right,max(cur.cur,par))

try:
    build(root,1e18)
except:
    0
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.cur)

postorder(root)