x = input("Введите первое случайное число:")
y = input("Введите второе случайное число:")
z = (int(x) % int(y))
m = int(z*13)
n = int((m)**0.5)
l = int(abs(n))
print(int(x) , int(y) , int(z) , "-" , int(m) , int(n) , int(l))


