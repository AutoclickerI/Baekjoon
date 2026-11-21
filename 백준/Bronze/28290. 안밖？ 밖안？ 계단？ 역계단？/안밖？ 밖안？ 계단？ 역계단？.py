i,j,p,q,P,Q='in-out','out-in','fdsa','jkl;','asdf',';lkj'
print({p+q:i,q+p:i,P+Q:j,Q+P:j,P+q:'stairs',Q+p:'reverse'}.get(input(),'molu'))