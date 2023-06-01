a=list(map(int,input().split()))
print('OK'if sum(a)>99 else['Soongsil','Korea','Hanyang'][a.index(min(a))])