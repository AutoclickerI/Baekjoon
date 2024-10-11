exec('''w=int(input());c=0;r=1
for b in input().split():
 if c+len(b)>w:r+=1;c=len(b)+1
 else:c+=len(b)+1
print(r);'''*int(input()))