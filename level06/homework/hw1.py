num = int(input('enter a number: '))
res = 0
for i in range(1, num + 1):
    if i % 2 != 0:
        res += i

print("correct answer is", res)



