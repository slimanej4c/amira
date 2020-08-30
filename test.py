a=['omg yes','i am go 2 home']
b=[['omg','oh my GOD'],['2','to']]
for n, i in enumerate(a):

    for j in b:
        if j[0] in i:
            k=i.replace(j[0],j[1])
        a[n]=k
