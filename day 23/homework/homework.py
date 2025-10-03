word = input("შეიყვანე სიტყვა: ")

if word == word[::-1]:
    print("ეს განსაკუთრებული (palindrome) სიტყვაა")
else:
    print("ეს ჩვეულებრივი სიტყვაა")


words = ["სათვალე", "კომპიუტერი", "ფეხბურთი", "ტელეფონი", "გალაქტიკა", "ნოტბუქი"]

reversed_list = words[::-1]

for word in reversed_list[::2]:
    print(word)


word = input("შეიყვანე სიტყვა: ")
print("შებრუნებული სიტყვა:", word[::-1])



text = "ეს არის Python-ის დავალება სტრინგებზე" 

print("პირველი 5:", text[:5])

print("ბოლო 4:", text[-4:])

print("4-დან 10-მდე:", text[3:10])

print("შებრუნებული:", text[::-1])

print("ყოველი მეორე:", text[::2])
