class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print(f"-----------------------------------\nBienvenue au joueur {self.pseudo} \nPoints de vie: {self.health} \nAttaque: {self.attack}")

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        if self.weapon != None :
            damage = self.weapon.damage + self.attack
            target_player.damage(damage)
            if target_player.get_health() > 0 :
                print(f"Le joueur {self.pseudo} inflige {damage} dégâts. Le joueur {target_player.get_pseudo()} a maintenant {target_player.get_health()} points de vie.")

            else:
                print(f"Le joueur {self.pseudo} inflige {damage} dégâts. Le joueur {target_player.get_pseudo()} est presque mort.")
        else:
            damage = self.attack
            target_player.damage(damage)
            print(f"Le joueur {self.pseudo} inflige {damage} dégâts. Le joueur {target_player.get_pseudo()} a maintenant {target_player.get_health()} points de vie.")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def set_weapon(self, weapon_object):
        self.weapon = weapon_object

    def critical(self, target):
        target.damage(99)




#Ajouter une méthode set_weapon qui permet d'équiper une arme
#Modifier la méthode attack_player en conséquence
#Ajouter une méthode is_dead()