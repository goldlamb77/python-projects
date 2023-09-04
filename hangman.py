import random

words = ["name", "keyboard", "table", "random", "python", "java", "black", "clash", "apple", "banana","book","project"]
word = random.choice(words)
hidden = ""
wrong = ""
for i in range(0, len(word)):
    hidden += "_"
print(hidden)
lives = 5
while lives > 0:
    guess = input("What is your guess")
    if guess not in word:
        lives -= 1
        if guess in wrong:
            wrong += ""
        else:
            wrong += guess + " "
        print("Your letter is not in the word")
        print("You have " + str(lives) + " lives left!")
        print("Wrong guesses: " + wrong)
        print(hidden)

    else:
        s = list(hidden)
        for i in range(0,len(s)):
            if guess == word[i:i+1]:
                s[i] = guess
            else:
                continue
        hidden = "".join(s)
        print("correct")
        print("You have " + str(lives) + " lives left!")
        print("Wrong guesses: " + wrong)
        print(hidden)
    if hidden == word:
        break
if lives == 0:
    print("You lose")
else:
    print("You win")
