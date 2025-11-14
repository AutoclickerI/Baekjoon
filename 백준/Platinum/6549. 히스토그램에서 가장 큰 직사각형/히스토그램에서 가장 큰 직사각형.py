def get_right_closest_index(l):
    l=list(reversed(l))
    stack=[]
    ans=[]
    for i in range(len(l)):
        while stack and l[i]<=l[stack[-1]]:
            stack.pop()
        if stack:
            ans.append(i-stack[-1])
        else:
            ans.append(i+1)
        stack.append(i)
    ans.reverse()
    return ans

while 1:
    l=list(map(int,input().split()))[1:]
    if not l:
        break
    right=get_right_closest_index(l)
    left=list(reversed(get_right_closest_index(list(reversed(l)))))
    max_area=0
    for i in range(len(l)):
        max_area=max(max_area,l[i]*(right[i]+left[i]-1))
    print(max_area)