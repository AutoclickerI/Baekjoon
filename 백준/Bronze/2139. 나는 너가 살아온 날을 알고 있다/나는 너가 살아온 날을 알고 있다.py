from datetime import*
while'1'<(s:=input()):d,m,y=map(int,s.split());print(1+(date(y,m,d)-date(y,1,1)).days)