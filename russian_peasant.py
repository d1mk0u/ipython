## Russian Peasant multiplication
## Author DmitriS
while True:
    def ruspeace(a, b):
        if a == 1:
            a = a * b
            print("a * b equal", a)
            return "It Works"
        elif a < b:
            a, b = b, a
            #print(a, b)
        z = []
        num = 0
        while a >= 1:
            a = a // 2
            b = b * 2
            #print(a, b)
            if a % 2 == 1:
                z.append(b)
        for i in z:
            num = num + i
        print("a * b equal to", num)
        return "It Works"
    a = int(input("Insert Your first number: "))
    b = int(input("Insert Your second number: "))
    print(ruspeace(a, b))
