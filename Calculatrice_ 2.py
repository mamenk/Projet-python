# Calculatrice avec gestion des erreurs


a = input("Veuillez entrer un premier nombre : ")
b = input("Veuillez entrer un second nombre : ")

# Tant que a et b ne sont pas des nombres, on boucle

while not (a.isdigit() and b.isdigit()):

    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

    # On demande deux nombres à l'utilisateur

    a = input("Veuillez entrer un premier nombre : ")
    b = input("Veuillez entrer un second nombre : ")

    

# On affiche le résultat de l'addition
print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égale à {int(a) + int(b)}")



