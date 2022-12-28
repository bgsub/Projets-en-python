
# learning to work with a list of integers 

print("\n \n ########### List of integers ############### \n")
liste_nombres = [1, 6, 98, 52, 1045, 3]
# 1) classez la liste
liste_nombres.sort() 
# 2) supprimez le premier élément de la liste
liste_nombres.pop(0)
# 3) ajoutez le nombre "1097" à la fin de la liste
liste_nombres.append(1097)
# 4) récupérez le deuxième élément dans une variable "deuxieme_element"
deuxieme_element = liste_nombres[1]
print(deuxieme_element) # la console devrait afficher "6" !

# 5) affichez la longueur de la liste
print(len(liste_nombres))
print(liste_nombres)

# dictionaries 
print("\n ###############   Dictionaries  ########### \n")
# 1) Créez une variable de type dictionnaire appelée "chaussure"
chaussure = dict()

""" 2) Ajoutez les éléments suivants dans le dictionnaire :
   - clef "taille" avec la valeur 42
   - clef "marque" avec la valeur "Nike"
   - clef "race" avec la valeur "berger-allemand"
"""
chaussure["taille"] = 42
chaussure["marque"] = "Nike"
chaussure["race"] = "berger-allemand"
# 3) On s'est trompés ! Supprimez la clef "race" du dictionnaire :)
chaussure.pop("race")
# 4) Récupérez la taille de la chaussure dans une variable appelée "taille"
taille = chaussure["taille"]
print(f"La taille de la chaussure est {taille}")  # 42 normalement !
print(chaussure)