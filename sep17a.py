#calculate the sum of the list with itself.

l=[1,2,3,4,5,6]
m=[]
n=[]
s=0
for i in l:
    m.append(i)
    for j in m:
        if i==j:
            s=i+j
            n.append(s)
print(l)
print(n)