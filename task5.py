first_name = input("Введите имя:")
second_name = input("Введите фамилию:")
current_year = input("Введите нынешний год:")
year_of_birth = input("Введите дату рождения:")
age = int(current_year) - int(year_of_birth)
x = input("Введите первое случайное число:")
y = input("Введите второе случайное число:")
z = (int(x) % int(y))
m = int(z*13)
n = int((m)**0.5)
l = int(abs(n))
print("Hello" , first_name , second_name , "." , "You are" , age , "years old." , "Your secret code is" ,
      int(x) , int(y) , int(z) , "-" , int(m) , int(n) , int(l) , ".")


