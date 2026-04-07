s=input()
r=0
st=[]
for i in s:
    if i in st:
        ix=st.index(i)
        r+=len(st)-ix-1
        st.pop(ix)
    else:
        st+=i
print(r)