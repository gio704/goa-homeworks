listn = [1, 2, 3, 4, 5, 6, "gio", "patashuri",]

def manual_pop(l, li):
    index = li+1
    new_listn = []

    z = 0

    for i in listn:
        z+=1
        if z != index:
            new_listn.append(i)


    return new_listn

print(manual_pop(listn, 8))
