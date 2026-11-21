from fractions import Fraction

def get():
  s = input()
  if "(" not in s:
    return Fraction(s)
  before = s[0:s.find("(")]
  after = s[s.find("(")+1:s.find(")")]
  numafter = len(before)-s.find(".")-1
  return Fraction(before) + Fraction(Fraction(int(after), -1 + 10**len(after)), 10 ** numafter)

ret=get()+get()
if ret.denominator==1:print(ret,end='/1')
else:print(ret)