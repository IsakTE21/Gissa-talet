import random
generate = random.randint(1, 100)

gissning = input("Gissa talet mellan 1-100: ")
rätt = False
while not rätt:
    if int(gissning) == generate:
        print("Du gissade rätt, bra jobbat!")
        rätt = True
    elif int(gissning) < generate:
        print("För lågt")
        gissning = input("Gissa talet mellan 1-100: ")
    elif int(gissning) > generate:
        print("För högt")
        gissning = input("Gissa talet mellan 1-100: ")
