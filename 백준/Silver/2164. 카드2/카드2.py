from collections import deque
l=deque(range(1,int(input())+1))
while len(l)-1:
    l.popleft()
    l.append(l.popleft())
print(l[0])