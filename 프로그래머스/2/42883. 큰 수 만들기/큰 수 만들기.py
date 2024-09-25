def solution(s,k,l=[]):
 for i in s:
  while k and l and l[-1]<i:l.pop();k-=1
  l+=i
 return''.join(l[:len(l)-k])