from random import randint

def presentation():
    print("*****************************************")
    print("*     Welcome to the Guessing Game!     *")
    print("*****************************************")

def get_random_number():
    return randint(1, 100)

def get_user_number():
    user_number = int(input("I have chosen a number between 1 and 100, try to guess it: "))
    return user_number

def validate_user_number(user_number):
    if user_number < 1 or user_number > 100:
        print("\nYou entered an INVALID number!")
        print("Try a number between 1 and 100\n")
        return False
    else:
        return True

def get_difficulty():
    print("Choose the difficulty!")
    print("(1) Easy    (2) Medium    (3) Hard\n")

    difficulty = int(input("What is the difficulty? "))

    if difficulty not in [1, 2, 3]:
        print("Invalid difficulty! Try again.\n")
        difficulty = get_difficulty()
    else:
        return difficulty

def define_difficulty(difficulty):
    if difficulty == 1: return 20
    elif difficulty == 2: return 12
    else: return 6

def msg_difficulty(difficulty):
    print("")
    if difficulty == 1: 
        print("You selected the difficulty: Easy")
        print("So, you have 20 chances to get the right number!")
    elif difficulty == 2:
        print("You selected the difficultye: Medium")
        print("So, you have 12 chances to get the right number!")
    else: 
        print("You selected the difficulty: Hard")
        print("So, you have 6 chances to get the right number!")
    print()

def win():
    if random_number == user_number: 
        return True
    else: return False

def lose():
    if user_attempts > maximum_attempts: 
        return True
    else: return False

def is_bigger():
    if random_number > user_number: return True
    else: return False

def msg_win():
    print("Congratulations! You WIN!")
    print(f'The random number was {random_number}.\n')
    if user_attempts == 1:
        print(f'You got it right on {user_attempts}st attempt')
    elif user_attempts == 2:
        print(f'You got it right on {user_attempts}nd attempt')
    elif user_attempts == 3:
        print(f'You got it right on {user_attempts}rd attempt')
    else:
        print(f'You got it right on {user_attempts}th attempt')
    print(f'Total = {user_points} points.\n')

def msg_lose():
    print("You got it the maximum attempts.")
    print("So, you LOSE!! ... Try it Again ...\n")

presentation()

difficulty = get_difficulty()
maximum_attempts = define_difficulty(difficulty)
msg_difficulty(difficulty)

user_attempts = 1
user_points = 1000

random_number = get_random_number()

while user_attempts <= maximum_attempts:
    print(f"Attempts {user_attempts}º:")
    user_number = get_user_number()
    if not validate_user_number(user_number):
        user_attempts -= 1

    elif not win():
        print("Missed!", end=' ')
        if is_bigger():
            print("Try a BIGGER number.\n")
        else:
            print("Try a SMALLER number.\n")

        user_points -= (abs(user_number - random_number) / 2.0)

    elif win():
        break
    
    user_attempts += 1

print("\n... END GAME! ...\n")

if win(): 
    msg_win()
else: 
    msg_lose()
