# while loop გამოიყენება მაშინ, როცა წინასწარ არ ვიცით რამდენჯერ უნდა შესრულდეს ციკლი
# for loop კი გამოიყენება მაშინ, როცა ზუსტად ვიცით რამდენჯერ უნდა შესრულდეს ციკლი ან გვინდა სიაზე/რიცხვების გადავლისას

for i in range(10, 51, 2):
    print(i)

i = 0
while i <= 20:
    if i % 2 != 0:
        print(i)
    i = i + 1

word = input("Enter a word: ")
for letter in word:
    print(letter)

age = int(input("Enter your age: "))

if age < 18:
    print("you are a child")
elif age == 18:
    print("you just became an adult")
else:
    print("you are an adult")