#Exos sur les boucles
"""
Recopier l’exemple du cours et vérifier qu’il fonctionne
"""
for compteur in range(10):
    print(compteur)

liste_invites = ["Marcel", "Hippolyte", "Berthe"] 
for invite in liste_invites:                
    print("Bienvenu " + invite)
    
#Afficher les nombres paires entre 0 et 30
i=0
while i<30:
    i=i+2
    print(i,end=' ')
    
    
#Afficher en ordre décroissant les nombres de 10 à 1
i=11
while i>1:
    i=i-1
    print(i,end=' ')
    
#Calculer 1 x 2 x 3 x 4 x 5 x 6 avec une boucle
"""
list_try=range(6)
For number in range(6):
    number=number*(number-1)
    print(number)
 """   
# Emeline helped me
resultat=1
for nombre in range(1,6):
        resultat=resultat*nombre
        print(resultat)

#Avec une boucle imbriquée dans une boucle, afficher le texte suivant. Les mots “Bonjour”, “Comment vas-tu”, “Au revoir”, “Paul”, “Rose”, “Etienne” ne doivent apparaître qu’une fois chacun dans le code

c=["Paul","Rose","Etienne"]
print(c)
for lettre in c :
    print(c)
    salutation= print("Bonjour"+ c)
    print(salutation)
"""
For element in list_name:
    salutation= ("Bonjour"+c)
    print(salutation)
"""

v="bonjour"
for lettre in v:
    print(lettre)
    