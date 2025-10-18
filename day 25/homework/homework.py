# 1)
# სხვადასხვა ტიპის ცვლადები
name = "Luka"          # str (ტექსტური მონაცემი)
age = 14               # int (მთელი რიცხვი)
height = 1.72          # float (ათწილადი რიცხვი)
is_captain = True      # boolean (ლოგიკური მნიშვნელობა)

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_captain, type(is_captain))


# 2)
name = input("შენი სახელი: ")
age = input("შენი ასაკი: ")
siblings = input("რამდენი და ან ძმა გყავს: ")

print("სახელი:", name, type(name))
print("ასაკი:", age, type(age))
print("და-ძმების რაოდენობა:", siblings, type(siblings))

# ასაკი და და-ძმების რაოდენობა გადავაქციოთ რიცხვებად
age = int(age)
siblings = int(siblings)
print("ასაკისა და და-ძმების ჯამი:", age + siblings)


# 3)
for number in range(3, 31):
    print(number, type(number))
    if number % 3 == 0:
        print(number, "არის სამის ჯერადი")
    else:
        print(number, "არ არის სამის ჯერადი")


# 4)
# ფუნქციები პროგრამაში იმიტომ გვჭირდება, რომ კოდი არ გავიმეოროთ და გავამარტივოთ მისი გამოყენება.
# მაგალითად, შეგვიძლია ერთი ფუნქცია გამოვიყენოთ ბევრჯერ სხვადასხვა მონაცემებით.
# ზოგი ცნობილი ფუნქცია:
# print() — ეკრანზე გამოსატანი ტექსტის ან მონაცემის ჩვენება.
# input() — მომხმარებლისგან ინფორმაციის მიღება.
# type() — ცვლადის ტიპის განსაზღვრა.


# 5)
# არგუმენტი — ეს არის მონაცემი, რომელიც ფუნქციაში გადაეცემა, რათა ფუნქციამ იმუშაოს ამ მონაცემზე.
# მაგალითად:

def greet(name):
    print("გამარჯობა,", name)

greet("ლუკა")  # აქ "ლუკა" არის არგუმენტი
