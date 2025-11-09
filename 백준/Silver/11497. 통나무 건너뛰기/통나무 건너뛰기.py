for i in[*open(0)][2::2]:
    l=sorted(map(int,i.split()))
    l+=l[-1],
    l=l[::-1]
    l1=l[::2]
    l2=l[1::2]
    print(max(max(i-j for i,j in zip(l1,l1[1:])),max(i-j for i,j in zip(l2,l2[1:])),abs(l1[-1]-l2[-1])))