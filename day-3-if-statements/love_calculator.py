print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

names_combined = name1 + name2

total_in_true = 0

total_in_true += names_combined.count('t')

total_in_true += names_combined.count('r')

total_in_true += names_combined.count('u')

total_in_true += names_combined.count('e')

total_in_love = 0

total_in_love += names_combined.count('l')

total_in_love += names_combined.count('o')

total_in_love += names_combined.count('v')

total_in_love += names_combined.count('e')

true_love_score = int(str(total_in_true) + str(total_in_love))

if true_love_score < 10 or true_love_score > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif 39 < true_love_score < 51:
    print(f"Your score is {true_love_score}, you are alright together.")
elif true_love_score > 50:
    print(f'Your score is {true_love_score}, you guys look silly :)')
else:
    print(f"Your score is {true_love_score}.")
