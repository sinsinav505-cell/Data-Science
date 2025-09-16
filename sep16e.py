#adding elements of nested list 
# return the result in nested list

l=[[1,2,3],[4,5,6]]
m=l[0]
n=l[1]
z=[]
for i in range(len(m)):
    z.append(m[i]+n[i])
print([z])