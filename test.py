name = "Cecilia"
print("Hello, " + name + "!")

#Raining
raining = True
if raining == True:
    print("Take the umbrella")
else:
    print("Bring sunglasses !")

elephants = 100

if elephants == 0:
    print("No elephants")
elif elephants > 6:
    print("A lot of elephants!")

#Energy level, interger between 0 and 10
energy = int(input("How high is youre energy level? "))

if energy < 4:
    print("Time for a snack")
elif energy>=4 and energy<7:
    print("You're doing great ")
elif energy>=7:
    print("Whoa, time to slow down!!")