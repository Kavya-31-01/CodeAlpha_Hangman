# codealpha_Hungman
import random

# Predefined list of 5 words
words = ["apple", "python", "chair", "table", "phone"]

# Randomly select a word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

# Main game loop
while incorrect_guesses < max_incorrect:
    display_word = ""
    
    # Display current word state
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word.strip())
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_incorrect - incorrect_guesses)
    
    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess not in secret_word:
        incorrect_guesses += 1
        print("❌ Wrong guess!\n")
    else:
        print("✅ Correct guess!\n")

# Lose condition
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over! You ran out of guesses.")
    print("The correct word was:", secret_word)
