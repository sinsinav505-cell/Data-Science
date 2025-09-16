#adding elements of nested list 
# return the result in nested list

l=[[1,2,3],[4,5,6]]
m=[]
n=[]
for i in l:
    n=m
    m=[]
    for j in i:
        m.append(j)
print(n)
print(m)
z=[]
for k in n:
    for x in m:
        a=k+x
        z.append(a)
        break
print(z)
