import random 

def rng_guesser():
    rng_value = random.randint(1,10)
    rng_guess = int(input("Choisi un nombre entre 1 et 10:"))
    print(rng_value)
    if rng_guess == rng_value:
        print("Vous avez deviné, un véritable médium !")
    else :
        print("T'es vraiment un putain de looser ! Ta mère te hait !")
        return rng_guesser()

rng_guesser()

