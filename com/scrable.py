'''
Created on Feb 13, 2016

@author: Marko
'''

# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
   
    # inFile: file
    inFile = open(r"C:\Users\Marko\Desktop\words.txt", 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
    

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    sum = 0
    
    for i  in word:
        sum+=SCRABBLE_LETTER_VALUES.get(i,0)
    
    if len(word)==n:
         sum*=len(word)
         sum+=50
    else:
        sum*=len(word)
        
    return sum
    
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print (letter," ",end="")             # print all on the same line
    print()                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    
    for i in range(len(word)):
       
        letter = word[i]
        hand[letter] -=1
        if hand[letter]==0:
            hand.pop(letter)
        
    
    return hand
#
def is_valid_word(word, hand, word_list):
  
       
   count = 0
   for i in range(len(word)):
       
      if word[i] in hand:
          count+=1
          hand[word[i]]-=1
          if hand[word[i]]==0:
              hand.pop(word[i])
               
   
   
  

   if  word in word_list and len(word)==count:
       return True
   else:
       return False
   
   
def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    total = 0
    
   
    
    while(len(hand)>0  ):
        display_hand(hand)
        word = input("Enter a word or . to indicate that game is over ")
        score = get_word_score(word, HAND_SIZE)
        total+=score
        print(word ," earned ",score," Your total score is ",total)
        hand =update_hand(hand, word)
        
        

    print("your total score is ",total)

def play_game(word_list):
    print("currently in tha game")
    # TO DO...

def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("outgnawn", 8):146}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print ("FAILURE: test_get_word_score()")
            print ("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print ("SUCCESS: test_get_word_score()")
#

def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    word = "quail"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")")
        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function
        
    # test 2
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")" )       
        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function

    # test 3
    hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    word = "hello"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")"  )              
        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
        
        return # exit function

    print ("SUCCESS: test_update_hand()")




def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    hand = get_frequency_dict(word)

    if not is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "even"

    if  is_valid_word(word, hand, word_list):
        print ("FAILURE: test_is_valid_word()")
        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print ("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        
        failure = True        

    if not failure:
        print ("SUCCESS: test_is_valid_word()")





word_list = load_words()
hand = {"a":1,"c":1, "i":1 ,"h":1 ,"m":2 ,"z":1}


play_hand(hand, word_list)












   