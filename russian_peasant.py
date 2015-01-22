def ruspeace(a, b):
    z = []
    num = 0
    while a > 1:
        a = a // 2
        b = b * 2
        
##        print(a, b)
        if a % 2 == 1:
            z.append(b)
    for i in z:
        num = num + i
    return num
            
ax = ruspeace(10,6)
print(ax)
