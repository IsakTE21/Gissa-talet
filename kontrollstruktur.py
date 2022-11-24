import random
generate = random.randint(1, 100)

gissning = input("Gissa talet mellan 1-100")
rätt = False
while not rätt:
        gissning = input("Gissa talet mellan 1-100")
while generate == gissning:
        print("Du gissade rätt, bra jobbat")
        rätt = True
        
while rätt:
        print("You lost, please try again.")
