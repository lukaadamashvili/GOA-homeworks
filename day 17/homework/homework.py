# elif გვჭირდება მაშინ, როცა გვინდა ერთზე მეტი პირობის შემოწმება if/else-სთან ერთად.
# მაგ: თუ პირველი პირობა არ დაკმაყოფილდა, else-ს გამოყენების ნაცვლად შეგვიძლია გამოვიყენოთ elif
# რათა დავამატოთ სხვა პირობის შემოწმება.

for i in range(20, 101):
    if i % 2 != 0:
        print(i)

print("-------------------")

password = "12345"   # შენ შეგიძლია შენი პაროლი ჩაწერო
user_input = input("Enter password: ")

while user_input != password:
    print("incorrect password")
    user_input = input("Enter password again: ")

print("password is correct")

print("-------------------")

num = 100
while num >= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1
