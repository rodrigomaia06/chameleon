#Imports
from collections import deque

#Dictionaries
letterdict = {
    "A": ("Ace_Spades-BLACK", "Ace_Hearts-RED"),
    "B": ("Two_Spades-BLACK", "Two_Hearts-RED"),
    "C": ("Three_Spades-BLACK", "Three_Hearts-RED"),
    "D": ("Four_Spades-BLACK", "Four_Hearts-RED"),
    "E": ("Five_Spades-BLACK", "Five_Hearts-RED"),
    "F": ("Six_Spades-BLACK", "Six_Hearts-RED"),
    "G": ("Seven_Spades-BLACK", "Seven_Hearts-RED"),
    "H": ("Eight_Spades-BLACK", "Eight_Hearts-RED"),
    "I": ("Nine_Spades-BLACK", "Nine_Hearts-RED"),
    "J": ("Ten_Spades-BLACK", "Ten_Hearts-RED"),
    "K": ("Jack_Spades-BLACK", "Jack_Hearts-RED"),
    "L": ("Queen_Spades-BLACK", "Queen_Hearts-RED"),
    "M": ("King_Spades-BLACK", "King_Hearts-RED"),
    
    "N": ("Ace_Clubs-BLACK", "Ace_Diamonds-RED"),
    "O": ("Two_Clubs-BLACK", "Two_Diamonds-RED"),
    "P": ("Three_Clubs-BLACK", "Three_Diamonds-RED"),
    "Q": ("Four_Clubs-BLACK", "Four_Diamonds-RED"),
    "R": ("Five_Clubs-BLACK", "Five_Diamonds-RED"),
    "S": ("Six_Clubs-BLACK", "Six_Diamonds-RED"),
    "T": ("Seven_Clubs-BLACK", "Seven_Diamonds-RED"),
    "U": ("Eight_Clubs-BLACK", "Eight_Diamonds-RED"),
    "V": ("Nine_Clubs-BLACK", "Nine_Diamonds-RED"),
    "W": ("Ten_Clubs-BLACK", "Ten_Diamonds-RED"),
    "X": ("Jack_Clubs-BLACK", "Jack_Diamonds-RED"),
    "Y": ("Queen_Clubs-BLACK", "Queen_Diamonds-RED"),
    "Z": ("King_Clubs-BLACK", "King_Diamonds-RED")
}

blackdict = {
    "Ace_Spades-BLACK": ("A", "Ace_Hearts-RED"),
    "Two_Spades-BLACK": ("B", "Two_Hearts-RED"),
    "Three_Spades-BLACK": ("C", "Three_Hearts-RED"),
    "Four_Spades-BLACK": ("D", "Four_Hearts-RED"),
    "Five_Spades-BLACK": ("E", "Five_Hearts-RED"),
    "Six_Spades-BLACK": ("F", "Six_Hearts-RED"),
    "Seven_Spades-BLACK": ("G", "Seven_Hearts-RED"),
    "Eight_Spades-BLACK": ("H", "Eight_Hearts-RED"),
    "Nine_Spades-BLACK": ("I", "Nine_Hearts-RED"),
    "Ten_Spades-BLACK": ("J", "Ten_Hearts-RED"),
    "Jack_Spades-BLACK": ("K", "Jack_Hearts-RED"),
    "Queen_Spades-BLACK": ("L", "Queen_Hearts-RED"),
    "King_Spades-BLACK": ("M", "King_Hearts-RED"),
    
    "Ace_Clubs-BLACK": ("N", "Ace_Diamonds-RED"),
    "Two_Clubs-BLACK": ("O", "Two_Diamonds-RED"),
    "Three_Clubs-BLACK": ("P", "Three_Diamonds-RED"),
    "Four_Clubs-BLACK": ("Q", "Four_Diamonds-RED"),
    "Five_Clubs-BLACK": ("R", "Five_Diamonds-RED"),
    "Six_Clubs-BLACK": ("S", "Six_Diamonds-RED"),
    "Seven_Clubs-BLACK": ("T", "Seven_Diamonds-RED"),
    "Eight_Clubs-BLACK": ("U", "Eight_Diamonds-RED"),
    "Nine_Clubs-BLACK": ("V", "Nine_Diamonds-RED"),
    "Ten_Clubs-BLACK": ("W", "Ten_Diamonds-RED"),
    "Jack_Clubs-BLACK": ("X", "Jack_Diamonds-RED"),
    "Queen_Clubs-BLACK": ("Y", "Queen_Diamonds-RED"),
    "King_Clubs-BLACK": ("Z", "King_Diamonds-RED"),  
}

reddict= {
    "Ace_Hearts-RED": ("A", "Ace_Spades-BLACK"),
    "Two_Hearts-RED": ("B", "Two_Spades-BLACK"),
    "Three_Hearts-RED": ("C", "Three_Spades-BLACK"),
    "Four_Hearts-RED": ("D", "Four_Spades-BLACK"),
    "Five_Hearts-RED": ("E", "Five_Spades-BLACK"),
    "Six_Hearts-RED": ("F", "Six_Spades-BLACK"),
    "Seven_Hearts-RED": ("G", "Seven_Spades-BLACK"),
    "Eight_Hearts-RED": ("H", "Eight_Spades-BLACK"),
    "Nine_Hearts-RED": ("I", "Nine_Spades-BLACK"),
    "Ten_Hearts-RED": ("J", "Ten_Spades-BLACK"),
    "Jack_Hearts-RED": ("K", "Jack_Spades-BLACK"),
    "Queen_Hearts-RED": ("L", "Queen_Spades-BLACK"),
    "King_Hearts-RED": ("M", "King_Spades-BLACK"),

    "Ace_Diamonds-RED": ("N", "Ace_Clubs-BLACK"),
    "Two_Diamonds-RED": ("O", "Two_Clubs-BLACK"),
    "Three_Diamonds-RED": ("P", "Three_Clubs-BLACK"),
    "Four_Diamonds-RED": ("Q", "Four_Clubs-BLACK"),
    "Five_Diamonds-RED": ("R", "Five_Clubs-BLACK"),
    "Six_Diamonds-RED": ("S", "Six_Clubs-BLACK"),
    "Seven_Diamonds-RED": ("T", "Seven_Clubs-BLACK"),
    "Eight_Diamonds-RED": ("U", "Eight_Clubs-BLACK"),
    "Nine_Diamonds-RED": ("V", "Nine_Clubs-BLACK"),
    "Ten_Diamonds-RED": ("W", "Ten_Clubs-BLACK"),
    "Jack_Diamonds-RED": ("X", "Jack_Clubs-BLACK"),
    "Queen_Diamonds-RED": ("Y", "Queen_Clubs-BLACK"),
    "King_Diamonds-RED": ("Z", "King_Clubs-BLACK"),
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

#Arraying the original deck
for line in d:
    columns = line.split()
    original_deck.append(columns[0])

#Arraying temporary decks          
for x in reversed(range(0, 52)):
    if "BLACK" in original_deck[x]:
        temporary_black_deck.append(original_deck[x])
    if "RED" in original_deck[x]:
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
response = input("Encrypt(E) or Dycrypt(D): ")
while True:
    if response == "E" or response == "e" or response == "D" or response == "d":
        break
    else:
        print("This is not a valid option.")
        response = input("Encrypt(E) or Dycrypt(D): ")
        
if response == "E" or  response == "e":
    decryped_message_raw = input("Decryped Message(CAPS): ")
    for i in range(0, len(decryped_message_raw)):
        decryped_message.append(decryped_message_raw[i])

    for k in decryped_message:
        # x = cipher_ready_deck.index(letterdict[k][0]) - 1
        # y = reddict[cipher_ready_deck[x]][1]
        # z = cipher_ready_deck.index(y) - 1
        if k == " ":
            encrypted_message.append(k)
            continue
        else:    
            z = cipher_ready_deck.index(reddict[cipher_ready_deck[cipher_ready_deck.index(letterdict[k][0]) - 1]][1]) - 1
            encrypted_message.append(reddict[cipher_ready_deck[z]][0])
            cipher_ready_deck[z], cipher_ready_deck[0] = cipher_ready_deck[0], cipher_ready_deck[z]
            cipher_ready_deck.rotate(-2)
    
    print("Encrypted Message: ", *encrypted_message, sep = "")
        
elif response == "D" or response == "d":
    encrypted_message_raw = input("Encrypted Message: ")
    for i in range(0, len(encrypted_message_raw)):
        encrypted_message.append(encrypted_message_raw[i])
    
    for k in encrypted_message:
        #w = cipher_ready_deck.index(letterdict[k][1])
        #x = cipher_ready_deck.index(letterdict[k][1]) + 1
        #y = blackdict[cipher_ready_deck[x]][1]
        #z = cipher_ready_deck.index(y) + 1
        if k == " ":
            decryped_message.append(k)
            continue
        else:
            w = cipher_ready_deck.index(letterdict[k][1])
            decryped_message.append(blackdict[cipher_ready_deck[cipher_ready_deck.index(blackdict[cipher_ready_deck[cipher_ready_deck.index(letterdict[k][1]) + 1]][1]) + 1]][0])
            cipher_ready_deck[w], cipher_ready_deck[0] = cipher_ready_deck[0], cipher_ready_deck[w]
            cipher_ready_deck.rotate(-2)

    print("Decrypted Message: ", *decryped_message, sep = "")

