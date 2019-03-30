num = 1500
lista = []
while num <=2700:
    divide7 = num % 7
    divide5 = num % 5

    if divide5 == 0 and divide7 == 0:
        lista.append(num)
    num = num + 1
str = " ".join(str(lista))
print(str)

#print(type(str(lista)))