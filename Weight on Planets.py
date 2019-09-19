# J.Baldwin
# This program is a version of Weight on Planets with the exception of displaying all of the planets it will as

print("Welcome to Weight on Planet!\nTo begin please select the planet you want to calculate your weight\nand then insert your weight in pounds.")

userChoice = input("Please enter the planet you want: ")
userWeight = float(input("Please enter your weight in pounds: "))


planetNames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#This is planet Mercury
if userChoice == planetNames[0]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * .38)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Venus
elif userChoice == planetNames[1]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * .91)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Earth
elif userChoice == planetNames[2]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * 1.00)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Mars
elif userChoice == planetNames[3]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * .38)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Jupiter
elif userChoice == planetNames[4]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * 2.34)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Saturn
elif userChoice == planetNames[5]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * 1.06)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Uranus
elif userChoice == planetNames[6]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * .92)
    print("Your weight on this planet will be", formulaWeight)
#This is planet Neptune
elif userChoice == planetNames[7]:
    print("You have chosen", userChoice)
    formulaWeight = float(userWeight * 1.19)
    print("Your weight on this planet will be", formulaWeight)
else:
    print("Invalid name. Please enter a planet name in our solar system.")