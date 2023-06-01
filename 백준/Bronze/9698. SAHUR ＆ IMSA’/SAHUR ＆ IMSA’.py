for i in range(int(input())):
    p,q=map(int,input().split())
    print(f'Case #{i+1}:',(p+(q-45)//60)%24,(q-45)%60)