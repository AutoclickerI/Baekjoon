from fractions import Fraction
class BOJ:
    def __init__(self,a,b=None):
        self.type='point'
        if b==None:
            self.type=a.type
            self.data=a.data
        else:
            self.data=a,b
    def __matmul__(self,b):
        ret=BOJ(0,0)
        if self.type==b.type=='point':
            ret.type='line'
            ax,ay=self.data
            bx,by=b.data
            ret.data=(by-ay,ax-bx,ay*bx-ax*by)
        elif self.type==b.type=='line':
            A,B,C=self.data
            D,E,F=b.data
            ret.data=(Fraction(B*F-E*C,A*E-B*D),Fraction(C*D-A*F,A*E-B*D))
        else:
            a=self
            if b.type=='line':a,b=b,a
            A,B,C=a.data
            D,E=b.data
            v1,v2=-2*C-B*E-A*D,-B*D+A*E
            ret.data=(Fraction(v1*A-v2*B,A*A+B*B),Fraction(v1*B+v2*A,A*A+B*B))
        return ret
    def __repr__(self):
        return f'{float(self.data[0]):.8f} {float(self.data[1]):.8f}'
for i in[*open(0)][:-1]:print(eval(i.replace('(','BOJ(')))