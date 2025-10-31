# 1) გამოითვალე სიის ყველა ელემენტის ნამრავლი
numbers = [2, 3, 4, 5]
product = 1
for num in numbers:
    product *= num
print("ნამრავლი:", product)


# 2) გამოიტანე მე0 ინდექსიდან მე8-მდე ელემენტები
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("მე0-იდან მე8-მდე ელემენტები:", my_list[0:9])


# 3) დაბეჭდე მხოლოდ ის რიცხვები, რომლებიც 5-ზე ნაკლებია
nums = [2, 7, 4, 9, 1]
for n in nums:
    if n < 5:
        print("5-ზე ნაკლებია:", n)


# 4) მომხმარებლის სახელი დიდი ასოებით და .lower()
name = input("შეიყვანე შენი სახელი დიდი ასოებით: ")
name = name.lower()
print("პატარა ასოებით:", name)


# 5) შენი გვარი პატარა ასოებით და .upper()
surname = "adamashvili"
surname = surname.upper()
print("დიდი ასოებით:", surname)


# 6) პირველი ასოს დიდი ასოდ გადაქცევა
text = "georgia"
text = text.capitalize()
print("პირველი ასო დიდია:", text)


# 7) ფუნქცია, რომელიც გამოითვლის ორ რიცხვს ჯამს
def add_numbers(a, b):
    print("ჯამი:", a + b)

add_numbers(3, 7)


# 8) ფუნქცია, რომელიც ამოწმებს ლუწია თუ კენტი
def even_or_odd(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(5))
print(even_or_odd(8))


# 9) ფუნქცია, რომელიც ამოწმებს დადებითია თუ უარყოფითი
def positive_or_negative(num):
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(positive_or_negative(-3))
print(positive_or_negative(10))


# 10) ფუნქცია, რომელიც მიესალმება სახელით
def greet(name):
    print("Hello", name)

greet("Giorgi")
greet("Luka")
