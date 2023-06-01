n=sum(map(int,(i.replace('.','')for i in open(0))))
print(f'{n//100}.{n%100:02d}')