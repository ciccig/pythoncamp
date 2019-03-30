gal_pals = ["Marie", "Lorian", "Ingrid", "Pia"]

#For dictionaries
squares = {x: x*x for x in range(6)}
print(squares)

#For lists
squaresList = [i*i for i in range(6)]
print(squaresList)

#Loop and iterations
#break is to get out of the loop

#nested for-loop
for i in range(3):
    for y in range(2):
        print("Hip hip")
    print("Hurrah!")

for x in range(11):
    print(x)

#dognames
dogNames = ["Micke", "Molle", "Pluto"]

for name in dogNames:
    print("If I get a dog, I will call it " + name + ".")

#List of numbers
inputList = [4, 7, 4, 3, 9]
inputs = 3
count = 0

for i in inputList:
    if i == input:
        print(count)
    count = count + 1

#Shorter version
place = inputList.index(inputs)
print(place)

#Another way
for i, y in enumerate(inputList, 0):
    if inputs == y:
        print("Index for the input: " + str(y))
        break

#While-loop
counter = 5
while counter > 0:
    print("The count is "+ str(counter))
    counter = counter - 1

#Ask for input from user
#name = input("Type your name: ")
#print("Oh, hello " + name)

#ctr c if you end up an infinite loop

#Build-in funcions
word = "PINK"
print(word.lower())
print(word.upper())
print(word.swapcase()) #Look up!!!

sentence = "I love rain"
print(sentence)
print(sentence.replace("rain", "sun"))
ordlista = sentence.split(" ")
print(ordlista)
sentence2 = " ".join(ordlista)
print(sentence2)

x = "Hi {}, you look {} !".format("Pink", "awesome")
print(x)

list2 = [ 2, 6, 3, 0, 4, 13 ]
list2.sort()
print(list2)

senDog = ",".join(dogNames)
print(senDog)

#Functions
def royaltify(name, city):
    return "The Great {} of {}".format(name, city)

name = "Cecilia"
city = "Hafjell"

royal_name = royaltify(name, city)

print("Behold "+ royal_name + " !")

def cups_to_dl(cups):
    dl = cups * diff
    return dl

diff = 2.37
print(cups_to_dl(2))

def dl_to_cups(dl):
    cups = dl / diff
    return cups
dlFromUser = float(input("Ange antal dl: "))
convertedCups = dl_to_cups(dlFromUser)
print("{} dl motsvarar {} cups".format(dlFromUser,convertedCups))