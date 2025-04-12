input()
s=input()

def cal(a,op,b):
    if op=='*':
        return int(a)*int(b)
    if op=='+':
        return int(a)+int(b)
    if op=='-':
        return int(a)-int(b)

maxval=-10**18
def DFS(v,idx):
    global maxval
    if idx==len(s)-1:
        maxval=max(v,maxval)
        return
    DFS(cal(v,s[idx+1],s[idx+2]),idx+2)
    if idx<len(s)-4:
        DFS(cal(v,s[idx+1],cal(s[idx+2],s[idx+3],s[idx+4])),idx+4)
DFS(int(s[0]),0)
print(maxval)