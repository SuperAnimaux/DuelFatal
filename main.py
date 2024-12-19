from player import Player
from weapon import Weapon
import random



"""
Créer deux joueurs (deux instances de la classe Player) avec les attributs suivants:
Pseudos de votre choix.
Joueur 1: 20 points de vie, 3 points d'ataque.
Joueur 2: 15 points de vie, 5 points d'attaque.
"""

"""
Créer deux armes (deux instances de la classe Weapon) avec les attributs suivants:
Arme 1: couteau, 3 points d'attaque
Arme 2: batte, 4 points d'attaque
"""

"""
Simuler un combat entre les deux joueurs, qui s'arrête quand l'un des joueurs atteint 0 points
 de vie et retourne le nom du ou des joueurs morts 
(on pourra implémenter une méthode is_dead() supplémentaire dans la classe player)
"""

weapon1 = Weapon("couteau", 3)
weapon2 = Weapon("batte", 4)

player1 = None
player2 = None

#Pour faire beau !!!
print("""
 /$$$$$$$                      /$$       /$$$$$$$$         /$$               /$$
| $$__  $$                    | $$      | $$_____/        | $$              | $$
| $$  \ $$ /$$   /$$  /$$$$$$ | $$      | $$    /$$$$$$  /$$$$$$    /$$$$$$ | $$
| $$  | $$| $$  | $$ /$$__  $$| $$      | $$$$$|____  $$|_  $$_/   |____  $$| $$
| $$  | $$| $$  | $$| $$$$$$$$| $$      | $$__/ /$$$$$$$  | $$      /$$$$$$$| $$
| $$  | $$| $$  | $$| $$_____/| $$      | $$   /$$__  $$  | $$ /$$ /$$__  $$| $$
| $$$$$$$/|  $$$$$$/|  $$$$$$$| $$      | $$  |  $$$$$$$  |  $$$$/|  $$$$$$$| $$
|_______/  \______/  \_______/|__/      |__/   \_______/   \___/   \_______/|__/""")

#Permet au 2 joueurs de choisir leur pseudo
def player_choice():
    player1_name = str(input("-----------------------------------\nEntrez le pseudo du joueur 1 : \n"))

    player2_name = str(input("-----------------------------------\nEntrez le pseudo du joueur 2 : \n"))

    return player1_name, player2_name



#Cette fonction permet d'attribuer une arme aléatoire aux joueurs 
def set_weapons(attack_player, defense_player):

    attack_player_weapon_random = random.randint(0, 2)

    if attack_player_weapon_random == 0:
        attack_player.set_weapon(weapon1)
        print(f"-----------------------------------\nLe joueur {attack_player.pseudo} a reçu un {weapon1.name}")
    elif attack_player_weapon_random == 1:
        attack_player.set_weapon(weapon2)
        print(f"-----------------------------------\nLe joueur {attack_player.pseudo} a reçu une {weapon2.name}")
    else:
        print(f"-----------------------------------\nLe joueur {attack_player.pseudo} n'a pas reçu d'arme.")
    
    defense_player_weapon_random = random.randint(0, 2)

    if defense_player_weapon_random == 0:
        defense_player.set_weapon(weapon1)
        print(f"-----------------------------------\nLe joueur {defense_player.pseudo} a reçu un {weapon1.name}")
    elif defense_player_weapon_random == 1:
        defense_player.set_weapon(weapon2)
        print(f"-----------------------------------\nLe joueur {defense_player.pseudo} a reçu une {weapon2.name}")
    else:
        print(f"-----------------------------------\nLe joueur {defense_player.pseudo} n'a pas reçu d'arme.")


#Fonction qui simule le combat 
def fight_sim(attack_player_object, defense_player_object):

    # appelle la fonction set_weapons
    set_weapons(attack_player_object, defense_player_object)
    #choix du premier a attaqué
    random_start_player = random.randint(0,1)

    #variable qui compte le nombre de tours
    n = 1

    if random_start_player == 0:
        print(f"-----------------------------------\nLe joueur {attack_player_object.get_pseudo()} commence le combat")
        print("""
 ___      ___  ____   __ __  ______      ___    __ __         __   ___   ___ ___  ____    ____  ______ 
|   \    /  _]|    \ |  |  ||      |    |   \  |  |  |       /  ] /   \ |   |   ||    \  /    ||      |
|    \  /  [_ |  o  )|  |  ||      |    |    \ |  |  |      /  / |     || _   _ ||  o  )|  o  ||      |
|  D  ||    _]|     ||  |  ||_|  |_|    |  D  ||  |  |     /  /  |  O  ||  \_/  ||     ||     ||_|  |_|
|     ||   [_ |  O  ||  :  |  |  |      |     ||  :  |    /   \_ |     ||   |   ||  O  ||  _  |  |  |  
|     ||     ||     ||     |  |  |      |     ||     |    \     ||     ||   |   ||     ||  |  |  |  |  
|_____||_____||_____| \__,_|  |__|      |_____| \__,_|     \____| \___/ |___|___||_____||__|__|  |__|  \n""")
        while True:

            print(f"\n----------------------------------- Tour n°{n} -----------------------------------")
            n += 1

            #systeme de coup critique
            if random.random() < 0.1:
                attack_player_object.critical(defense_player_object)
                print(f"/!\ Le joueur {attack_player_object.get_pseudo()} inflige un coup fatal au joueur {defense_player_object.get_pseudo()}. /!\ ")
                win = f"-----------------------------------\nLe joueur {attack_player_object.pseudo}, a battu le joueur {defense_player_object.pseudo}"
                return win
            
            else:
                attack_player_object.attack_player(defense_player_object)
            
            if random.random() < 0.1:
                defense_player_object.critical(defense_player_object)
                print(f"/!\ Le joueur {defense_player_object.get_pseudo()} inflige un coup fatal au joueur {attack_player_object.get_pseudo()}. /!\ ")
                win = f"-----------------------------------\nLe joueur {defense_player_object.pseudo}, a battu le joueur {attack_player_object.pseudo}"
                return win
            else:

                defense_player_object.attack_player(attack_player_object)

            if defense_player_object.is_dead() == True and attack_player_object.is_dead() == True:
                win = f"-----------------------------------\nLes joueurs sont morts en meme temps. égalité."
                return win
        
            elif defense_player_object.is_dead() == True:
                win = f"-----------------------------------\nLe joueur {attack_player_object.pseudo}, a battu le joueur {defense_player_object.pseudo}"
                return win
      
        
            elif attack_player_object.is_dead() == True:
                win = f"-----------------------------------\nLe joueur {defense_player_object.pseudo}, a battu le joueur {attack_player_object.pseudo}"
                return win
    
    else:

        print(f"-----------------------------------\nLe joueur {defense_player_object.get_pseudo()} commence le combat")
        print("""
 ___      ___  ____   __ __  ______      ___    __ __         __   ___   ___ ___  ____    ____  ______ 
|   \    /  _]|    \ |  |  ||      |    |   \  |  |  |       /  ] /   \ |   |   ||    \  /    ||      |
|    \  /  [_ |  o  )|  |  ||      |    |    \ |  |  |      /  / |     || _   _ ||  o  )|  o  ||      |
|  D  ||    _]|     ||  |  ||_|  |_|    |  D  ||  |  |     /  /  |  O  ||  \_/  ||     ||     ||_|  |_|
|     ||   [_ |  O  ||  :  |  |  |      |     ||  :  |    /   \_ |     ||   |   ||  O  ||  _  |  |  |  
|     ||     ||     ||     |  |  |      |     ||     |    \     ||     ||   |   ||     ||  |  |  |  |  
|_____||_____||_____| \__,_|  |__|      |_____| \__,_|     \____| \___/ |___|___||_____||__|__|  |__|  \n""")
        
        while True :

            print(f"\n----------------------------------- Tour n°{n} -----------------------------------")
            n += 1

            if random.random() < 0.1:
                defense_player_object.critical(defense_player_object)
                print(f"/!\ Le joueur {defense_player_object.get_pseudo()} inflige un coup fatal au joueur {attack_player_object.get_pseudo()}. /!\ ")
                win = f"-----------------------------------\nLe joueur {defense_player_object.pseudo}, a battu le joueur {attack_player_object.pseudo}"
                return win
            
            else:
                defense_player_object.attack_player(attack_player_object)

            if random.random() < 0.1:
                attack_player_object.critical(defense_player_object)
                print(f"/!\ Le joueur {attack_player_object.get_pseudo()} inflige un coup fatal au joueur {defense_player_object.get_pseudo()}. /!\ ")
                win = f"-----------------------------------\nLe joueur {attack_player_object.pseudo}, a battu le joueur {defense_player_object.pseudo}"
                return win
            
            else:
                attack_player_object.attack_player(defense_player_object)
            
        
            if defense_player_object.is_dead() == True and attack_player_object.is_dead() == True:
                win = f"-----------------------------------\nLes joueurs sont morts en même temps. égalité."
                return win
        
            elif defense_player_object.is_dead() == True:
                win = f"-----------------------------------\nLe joueur {attack_player_object.pseudo}, a battu le joueur {defense_player_object.pseudo}"
                return win
      
        
            elif attack_player_object.is_dead() == True:
                win = f"-----------------------------------\nLe joueur {defense_player_object.pseudo}, a battu le joueur {attack_player_object.pseudo}"
                return win
                
        
       
pseudo = player_choice()

player1 = Player(pseudo[0], 20, 3)
player2 = Player(pseudo[1], 15, 5)

print(fight_sim(player1, player2))