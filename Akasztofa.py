import random
from szavak import szavak
from hangman_visual import eletek_visual_dict
import string


def get_valid_szo(szavak):
    szo = random.choice(szavak)  # Véletlenszerűen választott szó a könyvtárból
    while '-' in szo or ' ' in szo:
        szo = random.choice(szavak)

    return szo.upper()


def hangman():
    szo = get_valid_szo(szavak)
    hasznalt_betuk = set(szo)  # A betű benne van-e a szóban
    alphabet = set(string.ascii_uppercase)
    elhasznalt_betuk = set()  # A felhasználó által tippelt betűk tárolása

    eletek = 7

    # Felhasználó bemenet kezelése
    while len(hasznalt_betuk) > 0 and eletek > 0:
        # Használt betűk, életek kiírása
        print('Még ', eletek, 'életed van és a következő betűket használtad: ', ' '.join(elhasznalt_betuk))

        # Adott szóból milyen betűk vannak kitalálva
        szo_list = [letter if letter in elhasznalt_betuk else '-' for letter in szo]
        print(eletek_visual_dict[eletek])
        print('A jelenlegi szó: ', ' '.join(szo_list))

        user_letter = input('Tippelj egy betűt: ').upper()
        if user_letter in alphabet - elhasznalt_betuk:
            elhasznalt_betuk.add(user_letter)
            if user_letter in hasznalt_betuk:
                hasznalt_betuk.remove(user_letter)
                print('')

            else:
                eletek -= 1  # Élet levonása ha nem talált a betű
                print('\nA betű amit tippeltél: ', user_letter, 'nincs benne a szóban.')

        elif user_letter in elhasznalt_betuk:
            print('\nEzt a betűt már tippelted. Próbálkozz egy másikkal.')

        else:
            print('\nÉrvénytelen tipp.')

    # Ha elfogynak az életek, vagy minden betű jól volt megtippelve
    if eletek == 0:
        print(eletek_visual_dict[eletek])
        print('Sajnálom, nem sikerült kitalálni. A szó ', szo, 'volt.')
    else:
        print('Gratulálok! Sikerült kitalálnod, a szó ', szo, 'volt.')


if __name__ == '__main__':
    hangman()