def ruspeace(a, b):
    while a > 1:
        a = a // 2
        b = b * 2
        
##        print(a, b)
        if a % 2 == 1:
            z = []
            num = 0
            z.append(b)
            for i in z:
                num += i
                print(num)
            
ax = ruspeace(10,6)
print(ax) 
