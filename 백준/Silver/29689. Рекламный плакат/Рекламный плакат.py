l=eval('input(),'*int(input()))
print(max([1]+[min(len(i),len(j))for i,j in zip(l,l[1:])]))