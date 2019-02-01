a=[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
c=[]
for i in a:
    if i not in c:
        c.append(i)
a.sort()
b=0
print (a)
for i in range(0,len(c)):
    for j in range(0,len(a)):
        if c[i]==a[j]:
            b=b+1
    print (c[i]," - ",(b))
    b=0

        

