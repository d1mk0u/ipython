## Russian Peasant multiplication
## Author DmitriS
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

a = input("Insert Your first number: ")
b = input("Insert Your second number: ")
print(ruspeace(a, b))
