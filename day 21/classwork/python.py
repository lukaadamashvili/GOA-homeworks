# Mutable ობიექტები (მაგ: list, and more) შეიძლება შეიცვალოს შექმნის შემდეგ.
# Immutable ობიექტები (მაგ: int, float, str) ვერ იცვლება — თუ შეცვლი,ახალი ობიექტი შეიქმნება მეხსიერებაში.

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list[4] = "goa"
print(my_list)

secret_num = 7
guess = int(input("მოიგონე რიცხვი: "))

while guess != secret_num:
    print("არასწორია თავიდან ცადე")
    guess = int(input("მოიგონე რიცხვი: "))

print("შენ გამოიცანი რიცხვი")

# მოდი ნელა დავუშალოთ:
# True and False → False
# False or False → False
# True and (False and False) → True and False → False
# (True and True) → True
# (False or True) → True
# True and False → False
# საბოლოოდ გამოვა: False or False or False or True or True or False
# რაც არის → True

# პასუხი: ეს კოდი გამოიტანს True