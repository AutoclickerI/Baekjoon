N,M,a,b=map(int,open(0).read().split())
print(('S'*M+'\n')*a+'E'*b+'W'*(M-b)+('\n'+'N'*M)*(N+~a))