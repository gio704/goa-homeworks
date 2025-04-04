def cw1(L, num):
    res = []
    for i in L:
        if i % num == 0:
            res.append(i)
    return res
print(cw1([1,23,165,2,3,92,10,34,911], 3))        





