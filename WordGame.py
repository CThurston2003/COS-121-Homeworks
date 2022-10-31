hangmanWord = str(input("What is the Word for the other player to guess?"))
wrongGuess = int(input("How many wrong guesses does the player get?"))

totalGuess = int(wrongGuess + len(hangmanWord))

def stringList(string):
    list1 = []
    list1[:0] = string
    return list1


playerList = stringList(hangmanWord)
#print(playerList)



def hangMan():
    wordLong = len(hangmanWord)

    playerAnswer = []

    counter = 0

    print(f"Your word is {wordLong} letters long")
    print(f"You get {wrongGuess} wrong letter guesses")
    for i in range(totalGuess):
        
        

        playerGuess = str(input("What letter do you guess first?"))

        if playerGuess in playerList[i]:

            playerAnswer.insert(i,playerGuess)
            print(playerAnswer)
        else:
            print("Wrong Guess!")
            counter += 1
        
        if counter >= wrongGuess:
            print("You've used all your wrong guesses, ending game!")
            break
        







hangMan()
