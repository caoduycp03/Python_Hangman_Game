import random
n = input("Input game text file: ")
with open(n, "r") as f:
    words1 = f.readlines()
    words = []
    for word in words1:
        words.append(word[:-1])

def menu():
    print(f"""     _______________________________ 
    |                               |
    |Press 0: Play the hang man game|
    |Press any key to Exit          |
    |_______________________________|""")

    userChoice = input("Enter your choice: ")
    if userChoice == '0':
        return
    else:
        print("Good bye!!")
        exit()

def pick_word(words):
    lst = range(len(words))
    n = random.choice(lst)
    chosen_word = words[n]
    return chosen_word

def word_display(word_dct):
    displayed_word = ''
    for i in word_dct:
        displayed_word += word_dct[i]
    return displayed_word

menu()

word = pick_word(words)
word_dct = {i:"_" for i in range(len(word))}

user_guess = 0
m = 0
n = 0
guessed_word = []
while True:
    print("_____________________________________________________________________________________________________")
    print(f"\nHere is your puzzle: {word_display(word_dct)}")
    
    if m == len(word):
        print("\nCongratulations. You won!!!")
    if n == 5:
        print("\nSorry, you have made 5 incorrect guesses. You lose.")
        print(f"The correct word was {word}")
        break
    user_guess = input("\nPlease enter your guess: ")
    if user_guess in guessed_word:
        print("\nSorry, you have guessed that letter already.")
        continue
    else:
        guessed_word.append(user_guess)

    if len(user_guess) < 2 and user_guess.isalpha():
        user_guess = user_guess.upper()
        if user_guess in word:
            print("\nCongratulations, you guessed a letter in the puzzle!")
            for i in word_dct:
                if word[i] == user_guess:
                    word_dct[i] = user_guess
                    m += 1
        else:
            print("\nSorry, that letter is NOT in the puzzle.")
            n += 1
        print(f"You currently have {n} incorrect guesses.")
    else:
        print("\nError. Please try again!")




    


    

