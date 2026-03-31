from models import Animal, Dog, Cat


name = input("Enter animal name: ")
age = int(input("Enter age: "))
color = input("Enter color: ")

dog_name = input("Enter dog name: ")
dog_age = int(input("Enter dog age: "))
dog_color = input("Enter dog color: ")
breed = input("Enter dog breed: ")

cat_name = input("Enter cat name: ")
cat_age = int(input("Enter cat age: "))
cat_color = input("Enter cat color: ")
lives = int(input("Enter cat lives: "))


animal = Animal(name, age, color)
dog = Dog(dog_name, dog_age, dog_color, breed)
cat = Cat(cat_name, cat_age, cat_color, lives)


animals = [animal, dog, cat]


for a in animals:
    print(a)
    print(a.speak())
    print(a.info())
    print()