I=lambda:map(int,input().split())
n,a,b=I()
print(eval('+sum(x.bit_count()*(b-a)+a*x.bit_length()for x in[*I()][1:])'*n))