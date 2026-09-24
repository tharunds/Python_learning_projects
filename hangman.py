# its a game user should guess the each letter of the word based on given clue.
# things needed;
# i need words so that computer can choose along with clue
# user guess the letter in word
# if letter exist letter will be shown in place
# if not eliminate letter in list
import random
import string
data=list(string.ascii_uppercase)
word_dic = {
    "apple": "fruit",
    "apricot": "fruit",
    "avocado": "fruit",
    "banana": "fruit",
    "fig": "fruit",
    "grape": "fruit",
    "lemon": "fruit",
    "mango": "fruit",
    "orange": "fruit",
    "papaya": "fruit",
    "pomegranate": "fruit",
    "strawberry": "fruit",
    "watermelon": "fruit",
    "monkey": "animal",
    "bear": "animal",
    "camel": "animal",
    "elephant": "animal",
    "fox": "animal",
    "lion": "animal",
    "owl": "animal",
    "tiger": "animal",
    "rama": "mythology",
    "centaur": "mythology",
    "chimera": "mythology",
    "dragon": "mythology",
    "griffin": "mythology",
    "hydra": "mythology",
    "kraken": "mythology",
    "lamia": "mythology",
    "leprechaun": "mythology",
    "mermaid": "mythology",
    "minotaur": "mythology",
    "naiad": "mythology",
    "pegasus": "mythology",
    "phoenix": "mythology",
    "sphinx": "mythology",
    "abdomen": "bodyparts",
    "arm": "bodyparts",
    "brain": "bodyparts",
    "cheek": "bodyparts",
    "elbow": "bodyparts",
    "eye": "bodyparts",
    "foot": "bodyparts",
    "heart": "bodyparts",
    "kidney": "bodyparts",
    "lung": "bodyparts",
    "mouth": "bodyparts",
    "nose": "bodyparts",
    "shoulder": "bodyparts",
    "skin": "bodyparts",
    "tongue": "bodyparts",
    "wrist": "bodyparts"
}

def computer_choice():
    
    word=random.choice(list((word_dic.keys())))# choice is used for list
    return word.upper()
    
    

def user_game(word):
    global data
    copy_letter=data[:]
    # guess letter of word: _ _ _ _
    #if letter in the word revel that letter in word 
    #eliminate that guessed letter in list
    answer=["_"]*len(word)
    while True:
        print(" ".join(data))
        
        print(" ".join(answer))
        guess=input("enter the letter(A-Z):").upper()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid alphabet letter.")
            continue
            
        if guess not in data:
            print(f"You already used '{guess}'. Try another one.")
            continue
            
        # Remove the guessed letter from the available letters pool
        data.remove(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update all instances of the guessed letter in the hidden word
            for i, letter in enumerate(word):
                if letter == guess:
                    answer[i] = guess
                    
        else:
            print(f"Wrong! '{guess}' is not in the word.")
            
    print(f"\nCongratulations! You guessed the word: {word}")





def main():
    
    target_word = computer_choice()
    print(target_word)
    print("your clue:",word_dic[target_word.lower()])
    user_game(target_word)

if __name__ == "__main__":
    main()



    
