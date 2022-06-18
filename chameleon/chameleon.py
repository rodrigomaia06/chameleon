#Imports
from collections import deque
import argparse

#Dictionaries
letterdict = {
    "A": ("Ace_Spades", "Ace_Hearts"),
    "B": ("Two_Spades", "Two_Hearts"),
    "C": ("Three_Spades", "Three_Hearts"),
    "D": ("Four_Spades", "Four_Hearts"),
    "E": ("Five_Spades", "Five_Hearts"),
    "F": ("Six_Spades", "Six_Hearts"),
    "G": ("Seven_Spades", "Seven_Hearts"),
    "H": ("Eight_Spades", "Eight_Hearts"),
    "I": ("Nine_Spades", "Nine_Hearts"),
    "J": ("Ten_Spades", "Ten_Hearts"),
    "K": ("Jack_Spades", "Jack_Hearts"),
    "L": ("Queen_Spades", "Queen_Hearts"),
    "M": ("King_Spades", "King_Hearts"),
    
    "N": ("Ace_Clubs", "Ace_Diamonds"),
    "O": ("Two_Clubs", "Two_Diamonds"),
    "P": ("Three_Clubs", "Three_Diamonds"),
    "Q": ("Four_Clubs", "Four_Diamonds"),
    "R": ("Five_Clubs", "Five_Diamonds"),
    "S": ("Six_Clubs", "Six_Diamonds"),
    "T": ("Seven_Clubs", "Seven_Diamonds"),
    "U": ("Eight_Clubs", "Eight_Diamonds"),
    "V": ("Nine_Clubs", "Nine_Diamonds"),
    "W": ("Ten_Clubs", "Ten_Diamonds"),
    "X": ("Jack_Clubs", "Jack_Diamonds"),
    "Y": ("Queen_Clubs", "Queen_Diamonds"),
    "Z": ("King_Clubs", "King_Diamonds")
}

blackdict = {
    "Ace_Spades": ("A", "Ace_Hearts"),
    "Two_Spades": ("B", "Two_Hearts"),
    "Three_Spades": ("C", "Three_Hearts"),
    "Four_Spades": ("D", "Four_Hearts"),
    "Five_Spades": ("E", "Five_Hearts"),
    "Six_Spades": ("F", "Six_Hearts"),
    "Seven_Spades": ("G", "Seven_Hearts"),
    "Eight_Spades": ("H", "Eight_Hearts"),
    "Nine_Spades": ("I", "Nine_Hearts"),
    "Ten_Spades": ("J", "Ten_Hearts"),
    "Jack_Spades": ("K", "Jack_Hearts"),
    "Queen_Spades": ("L", "Queen_Hearts"),
    "King_Spades": ("M", "King_Hearts"),
    
    "Ace_Clubs": ("N", "Ace_Diamonds"),
    "Two_Clubs": ("O", "Two_Diamonds"),
    "Three_Clubs": ("P", "Three_Diamonds"),
    "Four_Clubs": ("Q", "Four_Diamonds"),
    "Five_Clubs": ("R", "Five_Diamonds"),
    "Six_Clubs": ("S", "Six_Diamonds"),
    "Seven_Clubs": ("T", "Seven_Diamonds"),
    "Eight_Clubs": ("U", "Eight_Diamonds"),
    "Nine_Clubs": ("V", "Nine_Diamonds"),
    "Ten_Clubs": ("W", "Ten_Diamonds"),
    "Jack_Clubs": ("X", "Jack_Diamonds"),
    "Queen_Clubs": ("Y", "Queen_Diamonds"),
    "King_Clubs": ("Z", "King_Diamonds"),  
}

reddict= {
    "Ace_Hearts": ("A", "Ace_Spades"),
    "Two_Hearts": ("B", "Two_Spades"),
    "Three_Hearts": ("C", "Three_Spades"),
    "Four_Hearts": ("D", "Four_Spades"),
    "Five_Hearts": ("E", "Five_Spades"),
    "Six_Hearts": ("F", "Six_Spades"),
    "Seven_Hearts": ("G", "Seven_Spades"),
    "Eight_Hearts": ("H", "Eight_Spades"),
    "Nine_Hearts": ("I", "Nine_Spades"),
    "Ten_Hearts": ("J", "Ten_Spades"),
    "Jack_Hearts": ("K", "Jack_Spades"),
    "Queen_Hearts": ("L", "Queen_Spades"),
    "King_Hearts": ("M", "King_Spades"),

    "Ace_Diamonds": ("N", "Ace_Clubs"),
    "Two_Diamonds": ("O", "Two_Clubs"),
    "Three_Diamonds": ("P", "Three_Clubs"),
    "Four_Diamonds": ("Q", "Four_Clubs"),
    "Five_Diamonds": ("R", "Five_Clubs"),
    "Six_Diamonds": ("S", "Six_Clubs"),
    "Seven_Diamonds": ("T", "Seven_Clubs"),
    "Eight_Diamonds": ("U", "Eight_Clubs"),
    "Nine_Diamonds": ("V", "Nine_Clubs"),
    "Ten_Diamonds": ("W", "Ten_Clubs"),
    "Jack_Diamonds": ("X", "Jack_Clubs"),
    "Queen_Diamonds": ("Y", "Queen_Clubs"),
    "King_Diamonds": ("Z", "King_Clubs"),
}

#Opening deck file
d = open("deck.txt", "r")

#Variables
original_deck = []
temporary_black_deck = []
temporary_red_deck = []
cipher_ready_deck = []
decryped_message = []
encrypted_message = []
parser = argparse.ArgumentParser(description="A program to encode and decode using the chameleon cipher.")

#Arraying the original deck
for line in d:
    columns = line.split()
    original_deck.append(columns[0])

#Arraying temporary decks          
for x in reversed(range(0, 52)):
    if "Spades" in original_deck[x] or "Clubs" in original_deck[x]:
        temporary_black_deck.append(original_deck[x])
    if "Hearts" in original_deck[x] or "Diamonds" in original_deck[x]:
        temporary_red_deck.append(original_deck[x]) 
        
#Arraying cipher ready deck
cb = 0
cr = 0
for f in range(0, 52):
    if f % 2 == 0:
        cipher_ready_deck.append(temporary_black_deck[cb])
        cb = cb + 1
    else:
        cipher_ready_deck.append(temporary_red_deck[cr])
        cr = cr + 1 
cipher_ready_deck.reverse()
cipher_ready_deck = deque(cipher_ready_deck)

#Getting user input
parser.add_argument("-e", "--encrypt_string", help = "Encrypt the phrases.")
parser.add_argument("-d", "--decrypt_string", help = "Decrypt the phrases.")
args = parser.parse_args()
        

if args.encrypt_string:
    decryped_message_raw = args.encrypt_string.upper()
    for i in range(0, len(decryped_message_raw)):
        decryped_message.append(decryped_message_raw[i])

    for k in decryped_message:
        # x = cipher_ready_deck.index(letterdict[k][0]) - 1
        # y = reddict[cipher_ready_deck[x]][1]
        # z = cipher_ready_deck.index(y) - 1
        if (k >= 'A' and k <= 'Z'):
            z = cipher_ready_deck.index(reddict[cipher_ready_deck[cipher_ready_deck.index(letterdict[k][0]) - 1]][1]) - 1
            encrypted_message.append(reddict[cipher_ready_deck[z]][0])
            cipher_ready_deck[z], cipher_ready_deck[0] = cipher_ready_deck[0], cipher_ready_deck[z]
            cipher_ready_deck.rotate(-2)
        else: 
            encrypted_message.append(k)
            continue    
    
    print("Encrypted Message: ", *encrypted_message, sep = "")


elif args.decrypt_string:
    encrypted_message_raw = args.decrypt_string.upper()
    for i in range(0, len(encrypted_message_raw)):
        encrypted_message.append(encrypted_message_raw[i])
    
    for k in encrypted_message:
        #w = cipher_ready_deck.index(letterdict[k][1])
        #x = cipher_ready_deck.index(letterdict[k][1]) + 1
        #y = blackdict[cipher_ready_deck[x]][1]
        #z = cipher_ready_deck.index(y) + 1
        if (k >= 'A' and k <= 'Z'):
            w = cipher_ready_deck.index(letterdict[k][1])
            decryped_message.append(blackdict[cipher_ready_deck[cipher_ready_deck.index(blackdict[cipher_ready_deck[cipher_ready_deck.index(letterdict[k][1]) + 1]][1]) + 1]][0])
            cipher_ready_deck[w], cipher_ready_deck[0] = cipher_ready_deck[0], cipher_ready_deck[w]
            cipher_ready_deck.rotate(-2)
        else:
            decryped_message.append(k)
            continue
        
    print("Decrypted Message: ", *decryped_message, sep = "")

else:
    print("Please use valid arguments. For more information use '-h'.")
