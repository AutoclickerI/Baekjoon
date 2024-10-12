for a in[0]*int(input()):
    L=int(input())
    *l,=map(int,input().split())
    for i in range(L-1):
        for j in range(L+~i):
            if l[j]>l[j+1]:a+=1;l[j],l[j+1]=l[j+1],l[j]
    print('Optimal train swapping takes',a,'swaps.')