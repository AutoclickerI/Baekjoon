for i in[*open(0)][:-1]:
    stack=[]
    try:
        for j in i:
            if j=='(':
                stack+=[0]
            if j=='[':
                stack+=[1]
            if j==']':
                if stack.pop()!=1:raise
            if j==')':
                if stack.pop()!=0:raise
        if len(stack):raise
        print('yes')
    except:print('no')