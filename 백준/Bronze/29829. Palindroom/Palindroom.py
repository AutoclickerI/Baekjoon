l=input().split()
print(*[['EI'],['JAH',*l[:len(l)//2]+l[~-len(l)//2::-1]]][sum(i>j for i,j in zip(l,l[::-1]))<2])