s=input()
p=s.find('U')
q=s.rfind('F')
print('-'*p+'U'+'C'*~(p-q)+'F'+'-'*~(q-len(s)))