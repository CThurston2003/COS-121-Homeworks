#   Code Done by   |\___/|             
# Caleb A. Thurston)     (    
#       (CAT)     =\     /=  
#    (10/25/22)     )===(    
#(Art found online)/     \  
#   (Last Edited)  |     |    
#     (10/28/22)  /       \   
#                 \       /      
#          _/\_/\_/\_   _/_/\_/\_

#Prompt: Short program storing and looking up information
#My Idea: Instead of a group of like "celebrities", im doing game companies and some attributes among them

gameEntryList = []
#List to store all the game entries in
class gameCompany:
    def __init__(self,upperEnt,name,money,dateFound,founder,knownFor):
        self.upperEnt = upperEnt
        self.name = name
        self.money = money
        self.dateFound = dateFound
        self.founder = founder
        self.knownFor = knownFor
#This is a class for the game companies to store
def listStore(upperEName,eName,eMoney,eDateFound,eFounder,eKnownFor):
    #Function to store entries into a list
    eeName = gameCompany(upperEName,eName,eMoney,eDateFound,eFounder,eKnownFor)
    gameEntryList.append(eeName)
    #print("LIST STORE IS WORKING")
    #print(gameEntryList)
listStore("NINTENDO","Nintendo", "15.3 Billion","September 23rd, 1889","Fusajiro Yamauchi","Super Mario Bros")
listStore("SONY","Sony","24.9 Billion","May 7th, 1946","Akio Morita, Masaru Ibuka","The Last of Us/The Last of Us Remastered")
listStore("ACTIVISION","Activision","8.8 Billion","October 1st, 1979","David Crane, Alan Miller","World of Warcraft")
listStore("ELECTRONICARTS","Electronic Arts","5.6 Billion","May 27th, 1982","Trip Hawkins","FIFA")
listStore("TENCENT","Tencent","13.9 Billion","November 11th, 1998","Ma Huateng, Zhang Zhidong, Chenye Xu, Chen Yidan, Zeng Liqing","PUBG Mobile")
#This is where I pushed the values of the 5 preset entries

def listAtt(gClass):
    print(
        f"Name of Company: {gClass.name}","\n"
        f"Money made yearly: {gClass.money}","\n"
        f"Date company was founded: {gClass.dateFound}","\n"
        f"Founder(s) of the company: {gClass.founder}","\n"
        f"Most Popular Game: {gClass.knownFor}"
    )
#^^^ This is a function to list all the attributes of game company, when asked by the user ^^^

def userPrompt():

    userPromptStart = str(input("What would you like to do? (ADD new entry or READ existing entry or END to quit!): "))
    #Asking the User what they want to do

    userPromptActual = userPromptStart.upper()
    #this turns the user input into all uppercase to account for case insensitivity
    
    while userPromptActual != "END":
    #This gives an opportunity for an End statement
        if userPromptActual == "ADD":
        #This part of the function runs if the user says they want to add a new entry 
            nEntry = str(input("What is the name of the new Entry?: "))
            upperNEntry = nEntry.upper()
            nMoney = str(input("How much money do they make?: "))
            nDateFound = str(input("What date were they Founded?: "))
            nFounder = str(input("Who founded them?: "))
            nKnownFor = str(input("What games are they best known for?: "))
            listStore(upperNEntry,nEntry,nMoney,nDateFound,nFounder,nKnownFor)

            userPromptStart = str(input("What would you like to do? (ADD new entry or READ existing entry or END to quit!): "))
            userPromptActual = userPromptStart.upper()
            #Repeating the user prompt to keep program running
        
        elif userPromptActual == "READ":
        #This is when the User asks to read a entry
            entryName = str(input("What is the name of the entry?: "))
            entryNameActual = str(entryName.upper())
            for i in gameEntryList: #Checking if the entry is in the list
                if i.upperEnt == entryNameActual: #Change this to a loop?
                    listAtt(i)
                #This is where we call the specific entry in the list
            else:
                print("There is no entry with that name here! ")
                #This is what the user gets if what they try to read is not in the code
            userPromptStart = str(input("What would you like to do? (ADD new entry or READ existing entry or END to quit!): "))
            userPromptActual = userPromptStart.upper()
            #Repeating the user prompt to keep program running

        elif userPromptActual == "END":
            break
            #End statement to end the program if the user enters "end"

        else:
            userPromptStart = str(input("What would you like to do? (ADD new entry or READ existing entry or END to quit!): "))
            userPromptActual = userPromptStart.upper()
            #Repeating the user prompt to keep program running
#^^^ This is the main function of the program, controls the ADD, READ, and END actions in the program ^^^
userPrompt()