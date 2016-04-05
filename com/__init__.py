
import random
import string





def getting_words():
    lines =open(r"C:\Users\Marko\Desktop\words.txt").readlines()

    line = lines[0]

    words = line.split() 
    myword = random.choice(words)
    return myword


def check_letter(letter,list):
    if letter in list:
        return True
    else:
        return False


def menu():
    num_of_guesses = 8
    available_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"
                         ,"p","q","r","s","t","u","v","w","x","y","z"]
    
    
    word_to_guess = getting_words()
    menu_of_Hangman()
    print("Im thinking of word that has",len(word_to_guess)," letters")
    hidden_word = [" _ "] * len(word_to_guess)
    
    print(word_to_guess)
   

    iterate_available_letters(available_letters)
    
   
    letter = input("\nPlease guess the letter ")
    word_status = False
    
    
    while(num_of_guesses>0 or word_status==False):
        if check_letter(letter,word_to_guess):
            print("Good guess: ")
            add_letter_to_list(letter, word_to_guess, hidden_word)
            game_loop(letter, available_letters, hidden_word)
            
            
            
            word_status = check_words(word_to_guess, hidden_word)
            print("----------------------------------")
            print("\nYou have ",num_of_guesses," guesses  left")
            
            letter = input("Please guess the letter ")
        
        else:
            print("Oops! That letter is not in my word:")
            
            
            game_loop(letter, available_letters, hidden_word)
           
            word_status = check_words(word_to_guess, hidden_word)
            num_of_guesses-=1
            print("----------------------------------")
            print("\nYou have ",num_of_guesses,"guesses left")
            
            letter = input("Please guess the letter ")







def iterate_available_letters(list):
    
    for i in range(len(list)):
        print(list[i],end="")



def delete_letter_from_tuple(l,list):
    if l in list:
        list.remove(l)
            




def add_letter_to_list(l,word,list):
    
    for i  in range(len(word)):
        if l==word[i]:
            list[i]=l
    
    
    

def menu_of_Hangman():
    print("Welcome to the hangman game ")
    
    
def check_words(word,list):
    count = 0
    for i in range(len(word)):
        if word[i]==list[i]:
           count+=1

    if count==len(word):
        return True
    else:
        return False




def game_loop(letter,available_letters,hidden_word):
    delete_letter_from_tuple(letter, available_letters)
    iterate_available_letters(hidden_word)
    print()
    print("available letters are :",end="")
    iterate_available_letters(available_letters)
    print()
    
    
    
    
menu()