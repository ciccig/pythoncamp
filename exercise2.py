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
inputWord = input("Enter a word: ")

word = inputWord.upper()
word2 = word.swapcase()

print(word2)