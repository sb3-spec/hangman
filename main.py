import random as r

running = True
MAXLIVES = 5

words = [
    'hello', 'world'
]

def build_placeholder(word, blueprint=None):
    placeholder = ''
    
    for i in range(len(word)):
        placeholder += '_'
        
    for letter in correct_guesses.keys():
        for index in correct_guesses[letter]:
            placeholder.replace('_', letter, index)
    
    return placeholder
        

while running:
    correct_guesses = {}
    guesses = set()
    
    
    
    print('Welcome to hangman')
    
    random_word = words[r.randint(0, len(words) - 1)]
    placeholder = build_placeholder(random_word)
    tries = 0
    
    
    

    while placeholder != random_word:
        print('Please guess a letter, or chose to solve the word')
        user_input = input('>>>')
        user_input = user_input.strip().lower()
        
        lives = MAXLIVES
        if len(user_input) <= 1: 
            if user_input in guesses:
                print('You already guessed this, pick again')
            elif user_input == '':
                print('No value entered')
            else:
                tries += 1
                guesses.add(user_input)
                correct_count = 0
                for idx, letter in enumerate(random_word):
                    if letter == user_input:
                        correct_count += 1
                        if letter in correct_guesses.keys():
                            correct_guesses[user_input].append(idx)
                        else:
                            correct_guesses[user_input] = [idx]
                    
                if correct_count == 0:
                    lives -= 0
                    print(f"There were no {user_input}'s")
                elif correct_count == 1:
                    print(f"There was {correct_count} {user_input}")
                else:
                    print("There were {correct_count} {user_input}'s")
        else:
            tries += 1
            if user_input == random_word:
                print(f"You successfully guessed the word in {tries} tries")   
            else:
                lives -= 1
                print('Incorrect')
        placeholder = build_placeholder(random_word, correct_guesses)
                
        print(f"Live(s): {lives}")
        print(placeholder)

        
        
                    
        
    
    
    
    