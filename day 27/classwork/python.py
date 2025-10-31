# 1
names = ["Nika", "Luka", "Mariam", "Gio", "Ana"]
names.pop(0)
names.pop(-1)
print("1 შედეგი:", names)

# 2
# .insert(index, value) – ამატებს ელემენტს ინდექსზე
# .append(value) – ამატებს ბოლოში
# .pop(index) – შლის ელემენტს ინდექსით
# len(list) – აბრუნებს სიის სიგრძეს

# 3
names2 = ["Nino", "Sandro", "Elene", "Lasha", "Tamar"]
names2.insert(2, "Irakli")
print("3 შედეგი:", names2)

# 4
# .lower() – ყველა ასოს აქცევს პატარა ასოდ
# .upper() – ყველა ასოს აქცევს დიდ ასოდ
# .capitalize() – პირველი ასო დიდი, დანარჩენი პატარა
# .find('a') – პოულობს ასოს ინდექსს

# 5
surname = input("5) შეიყვანეთ თქვენი გვარი: ")
if surname[0].isupper():
    print("Hello")
else:
    print("Bye")

# 6
name = input("6) შეიყვანეთ თქვენი სახელი: ")
char = input("შეიყვანეთ ასო: ")
if char in name:
    print("found it", name.find(char))
else:
    print("Can't find character")

# 7
surname = input("7) შეიყვანეთ თქვენი გვარი: ")
choice = input("როგორ გსურთ შეიცვალოს? (upper/lower/capitalize): ")
if choice == "upper":
    print(surname.upper())
elif choice == "lower":
    print(surname.lower())
elif choice == "capitalize":
    print(surname.capitalize())
else:
    print("არასწორი არჩევანი")

# 8
numbers = [1,2,3,4,5,6,7,8,9,10]
print("8) კენტ ინდექსზე მდგომი ელემენტები:")
for i in range(len(numbers)):
    if i % 2 == 1:
        print(numbers[i])

# 9
nums = [10, 20, 30, 40, 50]
total = 0
for num in nums:
    total += num
print("9) ჯამი:", total)

# 10
numbers2 = [1,2,3,4,5,6,7,8,9,10]
print("10) კენტობა/ლუწობა:")
for i in numbers2:
    if i % 2 == 0:
        print(i, "luwia")
    else:
        print(i, "kentia")

# 11
# def — ქმნის ფუნქციას
# არგუმენტები — მნიშვნელობები, რომლებიც ფუნქციას გადაეცემა
# პარამეტრები — ცვლადები, რომლებიც იღებენ ამ არგუმენტებს
# return — აბრუნებს შედეგს, print — მხოლოდ აჩვენებს ეკრანზე

# 12
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print("12) ჯამი:", total)

sum([2, 4, 6, 8, 10])