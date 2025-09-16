#multiplying by 2 in a nested list

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
d=[]

for i in a:

    for j in i:

        c=j*5
        b.append(c)
        c=0
    d.append(b)
    b=[]
print(d)
