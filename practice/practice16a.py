#flatten a list

l=[[1,2,3],[4,5,6,7],[8,[9,10]]]
c=[]
for i in l:
    for j in i:
        if type(j)==list:
            for k in j:
                c.append(k)
        else:
            c.append(j)
print(c)

