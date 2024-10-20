class token:
    def __init__(self,state='improper'):
        self.state=state
    def __ror__(self,n):
        assert n==1 and self.state=='improper'
        return token('proper')
    def __or__(self,n):
        assert self.state=='proper'
        return token()
    def __repr__(self):
        return "token('%s')"%self.state

s1=input().replace(*'%|').replace(*'/|').replace(*'-|').replace(*'+|').replace(*'*|')
for i in range(97,123):
    exec('%c=1'%i)
try:
    eval(s1)
    s2='(1|'+s1.replace('(','(1|')+')'
    for i in range(97,123):
        exec('%c=token()'%i)
    try:
        v=eval(s2)
        assert v.state=='improper'
        print('proper')
    except:
        print('improper')
except:
    print('error')