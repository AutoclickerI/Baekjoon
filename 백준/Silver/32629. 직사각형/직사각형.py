from bisect import bisect_left
arr=[i*i for i in range(31624)]

for n in[*open(0)][1:]:
    n=int(n)
    i=bisect_left(arr,n)
    if n<=i*~-i:
        print(i*4-2)
    else:
        print(i*4)