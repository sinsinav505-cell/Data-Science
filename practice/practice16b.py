
l=[1,2,3,4,5,6,7]
m=[]
n=[]
for i in l:
    for j in l:
        if i+j==7:

            m=(i,j)
            if m not in n and m[::-1] not in n:
                n.append(m)
       
print(n)
        