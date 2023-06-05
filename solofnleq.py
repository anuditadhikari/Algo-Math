def f1(x, y):
    return (x**2) - (y**2) - 4


def f2(x, y):
    return (x**2) + (y**2) - 16


def j(x, y):
    return 8 * x * y


x = float(input("enter x: "))
y = float(input("enter y: "))
n = int(input("Enter the max iteration: "))
e = float(input("Enter tolerable error: "))
h = (-f1(x, y) * 2 * y - f2(x, y) * 2 * y) / j(x, y)
print("h : %f", h)
step = 1
while abs(h) > e:
    if j(x, y) == 0.0:
        print("Jacobian is 0")
        break
    h = (-f1(x, y) * 2 * y - f2(x, y) * 2 * y) / j(x, y)
    k = (-f2(x, y) * 2 * y + f1(x, y) * 2 * y) / j(x, y)
    x = x + h
    y = y + k
    step += 1
    print(f"Iteration:{step} root x:{x} y:{y} h:{h} k:{k} f1:{f1(x,y)} f2:{f2(x,y)}")

    if step > n:
        print("Not convergent")
        break
print(f"root is x:{x} and y:{y}")
