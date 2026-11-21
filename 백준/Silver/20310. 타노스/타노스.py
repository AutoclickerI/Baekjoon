s=input()
o,z=map(s.count,'10')
print(s.replace('1','',o//2)[::-1].replace('0','',z//2)[::-1])