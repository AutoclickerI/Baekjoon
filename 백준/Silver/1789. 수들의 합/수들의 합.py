from bisect import*
print(bisect_right([i*(i+1)//2 for i in range(99999)],int(input()))-1)