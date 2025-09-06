# ინდექსინგი ნიშნავს ელემენტზე წვდომას მისი ინდექსის (პოზიციის) საშუალებით.
# ინდექსები იწყება 0-დან. მაგალითად: my_list[0] = პირველი ელემენტი, my_list[-1] = ბოლო ელემენტი.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[-1])
print(my_list[-2])

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("შეიყვანეთ რიცხვი 0-დან 10-მდე: "))

if 0 <= num <= 10:
    nums[num] = "შეცვლილი"
    print(nums)
else:
    print("არასწორი რიცხვია!")

my_list2 = ["apple", "banana", "cherry", "grape", "melon"]
for item in my_list2:
    print(item)

my_list3 = [10, 20, 30, 40, 50, 60, 70, 80]
my_list3[2] = 300   
my_list3[6] = 700   
print(my_list3)