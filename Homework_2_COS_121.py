#   Code Done by      |\___/|             
# Caleb A. Thurston   )     (    
#       (CAT)        =\     /=  
#     (9/28/22)        )===(    
#(Art found online)   /     \  
#                     |     |    
#                    /       \   
#                    \       /      
#             _/\_/\_/\_   _/_/\_/\_

#Idea: Make a program that looks like "Oh Wow, fancy theoretical car journey" almost like a choose your own adventure

carDecelRate = 5

carMPG = 25
carTank = 13

def intro_func():
  intro = input("Hello Player! Welcome to the theoretical Car Journey Simulator! Please enter your player name! ")
  #Gimmicky function, getting the "players" name, to then disregard it
  print("Ok, now that we've got that useless info let's move on!")
  carDist = int(input("Ok, so, how far are we goin? (Miles) "))
 #Checking how many miles the player wants to go, to maybe give some attitude   
  if carDist < 4:
    print("Waste of gas, if I have anything to say about it...")
  else:
    print("Yea, sure... seems like a good distance")
  #Getting how fast the player wants to reach the destination
  carTime = float(input("Ok, so tell me, how soon do we wanna get there? (Hours)"))
  print("Ok, Calculating......")
  
  #Actual Speed of the car determined
  carSpeed = carDist/carTime
  print("The car's speed will be ", carSpeed, "!")

  #Assuming car can decelerate at 5mph/sec
  carDecel = carSpeed/carDecelRate

  #Section determining how many miles the car can go based on its Miles Per Gallon
  #This is based off the average car with a MPG of 25 and a tank of 13 gallons
  carLong = carMPG * carTank
  
  print("Here is your preliminary results! Total travel time: ", carTime, " hours."" Time to decelerate to a full stop (Just in case...): ", carDecel, " seconds. \n Also! The car can travel ", carLong, "miles before needing to refuel (If you fueled up before you left....)")
  
  return carDist, carTime, carSpeed, carDecel


#This creates global functions that I can use later in other functions
#I realize now, that I probably could've just made a class instead of this, but 
#I thought this implementation was cool, so I just decided to use it instead
CAR_DIST, CAR_TIME, CAR_SPEED, CAR_DECEL = intro_func()


#keep right function

def keepRight():
  print("Oh no! You're coming up on a roadway after coming off of a one way street where you don't have to worry about what side to drive on!")
  playerChoice = input("Dear Player, would you like to follow the traffic laws? (y/n)")
  if playerChoice == "y":
    print("You have chosen the lawful approach, the car will now steer right, to align itself")
  elif playerChoice == "n":
    print("You have chosen the chaotic approach, and you send the car careening down the middle of the lane, bobbing and weaving past cars, oncoming and on your side.")
  else:
    print("You have chosen an invalid input, due to your disobedience the car will choose for you. \nThe car will now start alighning itself into the right lane, following the law when the player does not....")

keepRight()

#this is deciding if there is a slow moving car on the road
isSlowMover = True

def slowMovers():
  print("Oh no! You're coming up on a highway that's known to have slow drivers! It has a speed limit of 60 MPH")
  
  #This statement with global is making it so I can access and edit the global CAR_SPEED variable in this function
  global CAR_SPEED
  
  #This if/elif statement is only triggered if the speed given at the start of the program is less than 60
  #It's to ask the player if they want to be a slow moving car or not, more or less
  if CAR_SPEED < 60:
    speedUp = input("Oh No, you're part of the problem! You're going too slow! \nWould you like to speed up to 60MHP? (y/n) ")
    if speedUp == "y":
      print("You have chosen the lawful option: The car speeds up to 60 MPH")
      CAR_SPEED = 60
      return CAR_SPEED
    elif speedUp == "n":
      print("You have chosen the inconvenient option.....you monster..")
    else:
      print("You have failed to give me a valid input, so the car will choose for you... \nThe Car speeds up to 60 MPH. ")
      CAR_SPEED = 60
  
  #Here's where we actually get into if there's a slow moving car on the road

  if isSlowMover == True:
    print("Looks like today's your unlucky day! Theres a slow moving car in the road")
    
    #Checking once again if the "player's car is going too slow"
    if CAR_SPEED < 60:
      print("Welp, looks like you're going slow like them, so you'll follow behind them for now... ")
      passOrNot = input("Would you like to speed up and pass this car? (y/n) ")
      if passOrNot == "y":
        #this line assumes the car speeds up only to pass, then slows back down to it's previous speed
        print("You pass this car on the left, and continue on your way. ")
      elif passOrNot == "n":
        print("Ok, you stay behind the car and travel behind it until your exit. ")
      else:
        print("Invalid Input given, car chooses for you, the car stays behind the car and continues to travel until your exit. ")
    
    elif CAR_SPEED >= 60:
        #This is the section for if the player is going the speed limit or more
      passOrNot = input("You are pulling up fast on a slow moving car, it is in the right lane allowing you to pass on the left \nWould you like to pass on the left? (y/n) ")
      if passOrNot == "y":
        print("Your car momentarily speeds up and you pass the car on the left, then get back in your own lane till you get off at your exit. ")
      elif passOrNot == "n":
        areYouSure = input("Are you sure? (y/n) ")
        #This is checking if the player is really sure that they don't want to pass
        if areYouSure == "y":
          print("Welp, your car careens towards the rear end of the vehicle in front of you \nAs your car collides with the car everything goes white.....")
          print("As the color fades back, you hear a gruff man say 'Hey you, You're finally awake. \nAnd then you blink and you're back in your car, passing on the left, like a NORMAL driver. ")
        elif areYouSure == "n":
          print("Good choice, your car momentarily speeds up and you pass the car on the left, then get back in your own lane till you get off at your exit.")
        else:
          print("Invalid Input, car chooses for you! Your car momentarily speeds up and you pass the car on the left, then get back in your own lane till you get off at your exit.")
      

  
    #If player doesn't choose a valid option
    else:
      print("Invalid Input, Car's Choice! I love it when that happens! Your car momentarily speeds up and you pass the car on the left, then get back in your own lane till you get off at your exit. ")


  else:
    print("Looks like today's your lucky day! There's no slow moving cars, and you're free to drive as you please!")
  

#this makes sure that the actions of this program have consequences
#so after the program if they choose to speed up, their speed is permanantly changed  
#CAR_SPEED = slowMovers()


slowMovers()

#Start of section for "Vehicles Turning Left!"

#global variable to decide if there is a vehicle, when the player's car is turning left
#If true, it means there will be a vehicle passing them, so it's one they should yield for when given the option
vehiclePass = True  

def vehicleLeft():
  yieldCar = input("As you're driving you come up on your turn, and you go to turn left. \nDo you yield as you turn? (y/n) ")
  if yieldCar == "y":

    #Code for when the player does yield to traffic

    if vehiclePass == True:
      print("The car yields to traffic and as you yield,\nyou see a car pass safely in front of you before you turn.")
    else:
      print("The car yields to traffic, but as you see no cars you take your turn safely. ")
  
  elif yieldCar == "n":

    #Code for when the player does NOT yield to traffic
    if vehiclePass == True:
      print("Reckless as ever.. As you take your turn, not even taking a moment to see, just before you finish your turn, a car hits the back of your car.")
      print("As your car is spinning, the world around you is a blur, \nbut as the car stops spinning you realize the car is heading perfectly down the street towards your location!")
    else:
      print("You leave your life in the hands of fate and whip the steering wheel towards your turn. \nThrough some dumb stroke of luck you pull through your turn perfectly fine and continue on your way.")
      print("Whew! A close one!")
  
  else:

    #Code when the player gives an invalid input

    if vehiclePass == True:
      print("Invalid Input, cars choice! The car yields to traffic and as you yield,\nyou see a car pass safely in front of you before you turn.")
    else:
      print("Invalid Input, cars choice! The car yields to traffic, but as you see no cars you take your turn safely. ")


vehicleLeft()

#section to make sure you don't go over the median

isMedian = True

def medianCheck():
  awk = input("You're taking a turn onto a major road way, watch out for medians!! (Type yes if you awknowledge this!)")
  print("I hoped you typed yes, but the fact you typed anything means you are awknowledging the risks!")

  if isMedian == True:
    print("There's a median in the way! Car is redirecting to make sure you don't hit it!")
  else:
    print("There's no median here, you're free to take your turn as normal and continue on your way!")

medianCheck()


#Area to watch out for maintanence

isMaintanence = True

def maintCheck():
  global CAR_SPEED
  check = input("Coming up on a possible maintanence area, type to awknowledge")
  if isMaintanence == True:
    print("There is maintanence in this area, taking percautions")
    if CAR_SPEED > 45:
      CAR_SPEED = 45
      print("Car was too fast, speed decreased in construction area! Speed is now ", CAR_SPEED)
    else:
      print("Car speed in acceptable range, speed was not changed")

maintCheck()









