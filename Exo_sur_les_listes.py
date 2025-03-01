import sys

# Liste des éléments vides au départ
LISTE = []

# Choix 

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:

    user_choice = input(MENU)
    
    # Si élément pas conforme au menu
    if user_choice not in MENU_CHOICES:

        print("Veuillez choisir une option valide...")
        continue
    
    # Ajouter un élément 
    if user_choice == "1":
        item = input("Veuillez entrer le nom de l'élément à ajouter :")
        LISTE.append(item)
        print(f"l'élément {item} a bien été ajouté à la liste.")

    # Retirer un élément
    elif user_choice == "2":
        item = input("Veuillez entrer le nom de l'élément à retirer :")

        if item in LISTE:
            LISTE.remove(item)
            print(f"l'élément {item} a bien été retiré de la liste.")
        else:
            print(f"l'élément {item} n'est pas dans la liste.")

    # Afficher la liste
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de la liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("La liste est vide")

    # Vider la liste
    elif user_choice =="4":
        LISTE.clear()
        print("La liste a été vidé de son contenu")

    # Quitter le programme
    elif user_choice == "5":
        print("À bientôt !")
        sys.exit()
    
    # Pour separer les différents choix de l'utilisateurs 

    print("_" * 50)