myfile = open("secret.txt", 'r+')

for line in myfile:
    print(line)

myfile = myfile.write("\nHello from Python!")
myfile = myfile.write("\nGoodbye from Python!")

print(myfile.read())

myfile.close()