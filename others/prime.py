list1 = []
i = 2
for i in range(2,101):
    j = 2
    for j in range (2,i):
        if i%j == 0:
            break
    else:
        list1.append(i)