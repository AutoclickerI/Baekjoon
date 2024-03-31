while i:=int(input()):
    for j in range(1,int(i**.5)+1):n=j*(i%j<1)or n
    print('Minimum perimeter is',2*(i//n+n),'with dimensions',n,'x',i//n)