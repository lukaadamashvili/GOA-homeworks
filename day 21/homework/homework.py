# Mutable (შეიძლება შეიცვალოს): list, and more
# Immutable (ვერ იცვლება): int, float, str.


my_list = list(range(1, 21)) 
my_list[-11] = 100  
my_list[-4] = 200   
print("განახლებული სია:", my_list)






password = "secret123"
user_input = ""

while user_input != password:
    user_input = input("შეიყვანეთ პაროლი: ")

print("თქვენ წარმატებით ჩაწერეთ პაროლი")




num = 40
while num >= 10:
    if num % 2 == 0:
        print(num)
    num -= 1
