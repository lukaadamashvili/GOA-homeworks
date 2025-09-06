# list არის მონაცემთა ტიპი Python-ში, რომელიც ინახავს ელემენტების კრებულს.
# მას ვიყენებთ მაშინ, როცა გვჭირდება ერთ ცვლადში რამდენიმე მონაცემის შენახვა.
# მაგალითად: რიცხვები, სიტყვები, სახელები და სხვა.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0])   
print(numbers[-1])  

my_list = ["red", "blue", "green", "yellow", "black"]

user_input = input("Enter any data to add in the list: ")

my_list = my_list + [user_input]

print(my_list)

fruits = ["apple", "banana", "cherry", "orange", "mango"]
print(fruits[3])
print(fruits[4])

for num in range(10, 100, 2):
        print(num)

names = ["Luka", "Ana", "Giorgi", "Nino", "Mari"]
index = int(input("Enter a number between 0 and 4: "))

if 0 <= index <= 4:
    print("Name at index", index, "is:", names[index])
else:
    print("Number out of Range!")