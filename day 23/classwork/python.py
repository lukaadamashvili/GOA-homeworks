surname = input("შეიყვანეთ თქვენი გვარი: ")
reversed_surname = surname[::-1]   
for i in reversed_surname:
    print(i)

# Indexing - ვიყენებთ კონკრეტული ინდექსის მქონე ელემენტზე მისასვლელად
# Slicing - ვიყენებთ ელემენტების ნაწილის ამოსაღებად
# განსხვავება: indexing აბრუნებს მხოლოდ ერთ ელემენტს, ხოლო slicing აბრუნებს დიაპაზონს (მონაკვეთს).


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("ლუწ ინდექსებზე მდგომი ელემენტები:", nums[::2])


names = ["Nika", "Luka", "Ana", "Saba", "Gio", "lizi", "Dato", "gela", "Irakli", "alex"]
start = int(input("დასაწყისი ინდექსი: "))
end = int(input("დასასრული ინდექსი: "))
print(names[start:end])




list1 = list(range(1, 16))   
step = int(input("შეიყვანეთ step რიცხვი: "))
print("ყოველი", step, "ელემენტი:", list1[::step])


surname = input("შეიყვანეთ თქვენი გვარი: ")
if surname[-6:] == "shvili":
    print("Hello")
else:
    print("Byee")

