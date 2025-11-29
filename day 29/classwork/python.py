#1)
names = ["Luka", "Nika", "Ana", "Giorgi"]
result = ", ".join(names)
print(result)

#2)
text = input("შეიყვანე წინადადება: ")

list = text.split()

amount = 0
for i in list:
    amount += 1

print("სიტყვების რაოდენობა არის:", amount)

#3)
def only_upper(p):
    if p.isupper():
        print("მხოლოდ დიდებია.")
    else:
        print("დაჭერილი არაა მხოლოდ დიდებით.")

something = input("პაროლი: ")
only_upper(something)

#4)
Word = input("ტექსტი: ")

if Word.islower():
    print("ყველაფერი პატარაა.")
else:
    print("ტექსტი შერეულია")

#5)
s = input("შეიყვანე წინადადება: ")
new = s.swapcase()
print(new)

#6)
line = input("სტრიქონი სივრცეებით ან ტირეებით: ")
clean = line.strip(" -")
print(clean)

#7)
txt = input("ტექსტი: ")
num = txt.count("ა")
print(num)

#8)
nums = []
for i in range(1, 11):
    nums.append(i)

print(nums)

#9)
data = [1,2,3,4,5,6,7,8,9,10]
even = []

for i in data:
    if i % 2 == 0:
        print(i)
        even.append(i)

print(even)

#10)
sentence = input("წინადადება: ")
words = sentence.split()

words2 = []
for i in words:
    words2.append(i.capitalize())

joined = " ".join(words2)

print("ახალი წინადადება:", joined)
print("სიტყვების რაოდენობა:", len(words2))