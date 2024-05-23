s=''.join(sorted(input()))
print(f'%0{len(s)}d'%(int(s[::-1])-int(s)))