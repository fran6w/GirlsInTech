liste_pays = ['ALLEMAGNE', 'AUTRICHE', 'BELGIQUE', 'BULGARIE', 'CHYPRE',\
			'CROATIE', 'DANEMARK', 'ESPAGNE', 'ESTONIE', 'FINLANDE',\
			'FRANCE', 'GRECE', 'HONGRIE', 'IRLANDE', 'ITALIE', 'LETTONIE',\
			'LITUANIE', 'LUXEMBOURG', 'MALTE', 'HOLLANDE', 'POLOGNE',\
			'PORTUGAL', 'TCHEQUIE', 'ROUMANIE', 'SLOVAQUIE', 'SLOVENIE', 'SUEDE']

def dessine_pendu(erreurs):
    if erreurs == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif erreurs == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif erreurs == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif erreurs == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif erreurs == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif erreurs == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("GAME OVER!")
