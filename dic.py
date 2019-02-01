dict={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
d=dict
def func(d):
    if d!=0:
        print (d)
        c=0
        for i in d:
            c= c+ d[i]
    print (c)

func(d)

