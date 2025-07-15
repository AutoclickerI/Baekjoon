s=lambda x:~x*x//-2
c=lambda x:~-~x*~x*x//6
(m,p),(M,P)=map(lambda d:(m:=-int(((1+8*int(d))**.5-1)//-2),int(d)-~-m*m//2),input().split())
print(s(P)-s(-p)+(s(m)+c(M-1)-c(m))*(m<M))