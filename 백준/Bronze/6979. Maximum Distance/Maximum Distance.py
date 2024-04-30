for _ in[0]*int(input()):
    n=int(input())
    l1=input().split()
    l2=input().split()
    print(f'The maximum distance is {max(abs(i-j)*(l1[i]==l2[j])for i in range(n)for j in range(i,n))}\n')