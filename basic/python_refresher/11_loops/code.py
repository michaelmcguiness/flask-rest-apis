number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ").lower()
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong")

friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)
for i in range(len(grades)):
    total += grades[i]
print(total / amount)

total = sum(grades)
print(total / amount)
