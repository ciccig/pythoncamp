#1 Function for
def NameSkillTown(name, town, skill):
    print("This is {} of {}, undefeated in {}!".format(name,town, skill))

name = "Cecilia"
town = "Täby"
skill = "Python coding"

NameSkillTown(name,town,skill)

# #2
# mealPrice = int(input("Enter the meal price: "))
#
# if mealPrice > 100:
#     tip = mealPrice*0.05
# else:
#     tip = mealPrice*0.1
#
# print(tip)

#3
# start = int(input("Enter a starting number: "))
# end = int(input("Enter a endign number: "))
#
# count = start
#
# while count <= end:
#     print(count)
#     count = count +1

#4
#inputWord = input("Enter a word: ")

#word = inputWord.upper()
#print(word)
#word2 = word[::-1]

#print(word2)

#5 Simple Authenication
import pandas as pd

#Usernames and password
df = {'Username': ["Agda", "Beata", "Celine", "Diana", "Eliza"], 'Password': ["111", "222", "333", "444","555"]}
df = pd.DataFrame(data=df)
df = df.set_index('Username')
#Name and password for authentications
user = input("Enter your username: ")

userindex = df.index == user
#Authentications
c = 0
for i in userindex:
    if i:
        passwordInput = input("Enter your password: ")
        if passwordInput == df.loc[user,"Password"]:
            print("authentication success")
        else:
            print("authentication failed")
    c = c+1

# 6 Hipp hipp hurray!
for i in [1, 2, 3]:
    for y in [1, 2]:
        print("Hipp")
    print("Hurray")

# 7 Rovarspraket
def rovarsprak(inputstring)
    for 