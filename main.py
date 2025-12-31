"""
usage:
Enter the path of the file with your words 
(i have provided a file in this code, just type wordbank.txt)

Now try and guess the word! Red means wrong letter,
yellow means correct letter but wrong position, 
and green means right letter and position!

Remember, you only have 6 tries! good luck!
"""

import random
import sys

correct_letters = []
position = []
blank_template = [".",".",".",".",".","."]
display_colors = [".",".",".",".",".","."]

#Introduction
print("⣿⣿⣿⣿⣿⠟⠁⣠⣶⣦⣤⣶⣶⣶⣶⣤⣀⣀⣀⣈⠉⠁⣤⣤⣄")
print("⣿⣿⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢀⣼⣿⠿")
print("⣿⣿⣿⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠐⠈⢁⣀")
print("⣿⣿⠇⢀⣿⡿⠿⠛⠋⠉⠉⠉⢀⢀⣀⣀⣠⣤⣼⣷⣾⣿⣿⡿")
print("⠿⠏⢀⡾⢀⢀⣀⣀⣠⣤⣶⡶⠞⣿⣿⣉⡟⣬⢙⠿⣿⣿⠏⠁⣰")
print("⣤⣤⡴⣷⠛⣿⣿⣿⣿⣿⣿⠇⢀⠙⠻⢿⣿⣧⡾⠶⢻⠛⢀⣼⣿")
print("⠘⠻⢶⣯⡝⢠⣍⣻⣿⣿⠋⢀⢀⢀⢀⢀⢀⢀⢀⢀⡿⢀⣼⣿⣿")
print("⢀⢀⢀⠙⣟⠋⠉⠉⢀⢀⠠⠴⠖⠛⠉⢀⢀⢀⢀⣼⠁⣰⣿⣿⣿")
print("⢀⢀⢀⢀⠈⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⠞⠁⣠⣿⣿⣿⣿")
print("⢀⢀⢀⢀⣠⣀⠈⠓⠦⣄⣀⣀⣀⣀⣤⣴⣾⠁⢠⣾⣿⣿⣿⣿⣿")
print("⢀⢀⢀⣸⣿⣿⣿⣦⣄⢀⢹⣿⣿⣿⣿⣿⣿⡆⠈⣿⣿⣿⣿⣿⣿")
print("⢀⢀⣼⣿⣿⣿⣿⣿⡏⢀⢸⣿⣿⣿⣿⣿⣿⣷⢀⢻⣿⣿⣿⣿⡟")
print("⢀⠘⠛⠛⠛⠛⠛⠛⢀⢀⠘⠛⠛⠛⠛⠛⠛⠛⠃⢀⠛⠛⠛⠛")
print("𝑺𝒂𝒓𝒗𝒆𝒔𝒉 𝑻𝒉𝒊𝒂𝒈𝒂𝒓𝒂𝒋𝒂𝒏 𝑷𝒓𝒆𝒔𝒆𝒏𝒕𝒔")
print("BREAST CANCER AWARENESS WORD SEARCH!")

while True: 
    try:
        file_path = str(input("------------------------------------------\nEnter the path of your .txt file of your wordbank: ")) #find and read path
        with open(file_path, "r", encoding="utf-8") as f:
            wordbank_data = f.read()
        break
    except:
        print("Error! That is not a valid path or your file type isn't a .txt!")
        continue
    

wordbank_list = wordbank_data.split('\n') 

for i in range(len(wordbank_list)):
    if len(wordbank_list[i]) != 6:
        print("Error! The word: " + str(wordbank_list[i] + " is not 6 letters! Please make sure every word is exactly 6 letters!"))

random.shuffle(wordbank_list)
current_word = str(wordbank_list[0])
current_word = list(current_word)
#print(current_word)

for i in range(6):    
    while True:    
        word_guess = input("------------------------------------------\nEnter a 6 letter word: ")
        if len(word_guess) != 6:
            print("That is not 6 letters! Try again")
            continue
        break
    word_guess = list(word_guess)
    
    correct_letters.clear()
    position.clear()
    
    for j in range(6):
        if word_guess[j] == current_word[j]:
            correct_letters.append(word_guess[j])
            position.append(j)
    
    for i in range(len(correct_letters)):
        blank_template[position[i]] = correct_letters[i]


    for i in range(6):
        if word_guess[i] == current_word[i]:
            display_colors[i] = "🟩"
        elif word_guess[i] in current_word:
            display_colors[i] = "🟨"
        else:
            display_colors[i] = "🟥"

    result = " ".join(display_colors)
    print(result)

    if "".join(word_guess) == "".join(current_word):
        print("You guessed the word correctly! Nice Job!")
        sys.exit()

    blank_template = [".",".",".",".",".","."]
    display_colors = [".",".",".",".",".","."]

print("The word was: " + "".join(current_word))
print("Try again by running the code again!")
