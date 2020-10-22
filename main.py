import random
import sys

sonad = []
with open('hangman_words.txt', 'r') as txtfile:
    for line in txtfile:
        xline = line.strip("\n")
        sonad.append(xline)

def vahe():
    print('---------------')

def word_choice():
    sona = []
    kriipsud = []
    random_sona = random.choice(sonad)
    random_sona_pikkus = len(random_sona)
    print(f'The word contains {random_sona_pikkus} letters')
    # print(f'The word is: {random_sona}')  # test purpose
    for letter in random_sona:
        sona.append(letter) 

    while random_sona_pikkus > 0:
        kriipsud.append('_')
        random_sona_pikkus -= 1
    print(" ".join(kriipsud))

    tries = 5
    while tries > 0:
        valik = input('Pick a letter: ').lower()
        vahe()
        if valik == random_sona:
            print('You won!')
            print(f"The word was '{random_sona}'.")
            sys.exit()

        elif valik in sona:
            print(f'Word contains letter {valik} ')
            sona_asukoht = sona.index(valik, 0, )
            kriipsud.pop(sona_asukoht)
            kriipsud.insert(sona_asukoht, valik)
            print(' '.join(kriipsud))
            if kriipsud == sona:
                print('You won!')
                print(f"The word was '{random_sona}'")
                sys.exit()

        elif valik not in sona:
            tries -= 1
            print(f"The word doesn't contain letter {valik}")
            print(f"{tries} tries left. ")
            print(" ".join(kriipsud))


    print('You ran out of tries.')
    print(f"The word was '{random_sona}'")


word_choice()
