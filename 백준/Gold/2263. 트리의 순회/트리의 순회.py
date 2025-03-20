import sys
sys.setrecursionlimit(10**5)

class node:
    def __init__(self,cur):
        self.cur=cur
        self.left=None
        self.right=None

def preorder(node):
    if node:
        print(node.cur,end=' ')
        preorder(node.left)
        preorder(node.right)

def build(pos,ino,pos_s,pos_e,ino_s,ino_e):
    if pos_s<pos_e:
        cur=node(pos[pos_e-1])
        idx=0
        while ino[idx+ino_s]!=pos[pos_e-1]:
            idx+=1
        cur.left=build(pos,ino,pos_s,pos_s+idx,ino_s,ino_e+idx)
        cur.right=build(pos,ino,pos_s+idx,pos_e-1,ino_s+idx+1,ino_e)
        return cur

input()
*inorder,=map(int,input().split())
*postorder,=map(int,input().split())
root=build(postorder,inorder,0,len(postorder),0,len(inorder))
preorder(root)