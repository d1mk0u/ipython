def ruspeace(a, b):
    if a == 1:
        a = a * b
        return a
    elif a < b:
        a, b = b, a
        print(a, b)
    z = []
    num = 0
    while a >= 1:
        a = a // 2
        b = b * 2
        
        print(a, b)
        if a % 2 == 1:
            z.append(b)
    for i in z:
        num = num + i
    return num

ax = ruspeace(23,1004)
print(ax)
