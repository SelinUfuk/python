a = 1
b = 1

fibonachi = [a,b]

for i in range(10):

    a,b = b, a+b
    print("a:",a ,"b:",b)

    fibonachi.append(b)

print(fibonachi)
