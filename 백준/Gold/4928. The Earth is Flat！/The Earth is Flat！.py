def H(s):
 a=''.join(s.split());i=0
 try:
  while a[-1-i].isdigit():i+=1
 except:return ''
 try:return ''.join(a[:-i])*int(a[-i:])
 except:return ''.join(a)
while(l:=input().rstrip())[0]!='$':
 l=l[:-1].replace('(',"H('").replace(')',"')");stack=[]
 for i in l:
  cache=[]
  if i==')':
   cache+=[i]
   while(l:=stack.pop())!='H':cache+=[l]
   stack+=[eval('H'+''.join(cache[::-1]))]
  else:stack+=[i]
 print(''.join(stack).rstrip())