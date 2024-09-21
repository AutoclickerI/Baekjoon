li=sorted(int(input())for _ in[0]*int(input()))[::-1]
stack=[li.pop()]
while len(stack)-stack[-1]-1:
    stack+=[li.pop()]
print(len(stack))