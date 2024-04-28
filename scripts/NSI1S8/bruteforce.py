# Deux fonctions utiles à la résolution du pb KP par brute force

def generer(n):
    """
    Renvoie une liste de TOUTES les combinaisons binaires possible de 0 à 2^n -1
    """
    liste = [None] * 2**n
    for i in range(2**n):
        k = bin(i)[2:] # conversion en binaire avec la fonction python 'bin',
        # en prenant soin d'enlever le '0b' en tête.
        s = '0' * (n - len(k)) + k # Astuce permettant d'ajouter le nb de 0 correct en tête
        liste[i] = s
    return liste

def combinaisons_possibles(liste_objets, combinaison, poids_max):
    """
    Renvoie la liste des combinaisons d'objets possibles ainsi que la liste de poids associée, 
    compte tenu de la contrainte poids_max
    """
    
    v, p = [], [] # deux variables contenant le résultat    
    for k in combinaison: # On boucle sur toutes les combinaisons fournies
        poids_comb, valeur = 0, 0
        # On examine les objets de cette combinaison k
        for i in range(len(liste_objets)): 
            if k[i] == '1': # Si le i-ème objet est choisi ...
                nom, poids_i, valeur_i = liste_objets[i] # on récupère ses caractéristiques:
                poids_comb = poids_comb + poids_i # poids et ...
                valeur = valeur + valeur_i # ...valeur !  
        if poids_comb > poids_max :
            valeur = 0 # la contrainte n'est pas respectée, cette combinaison est à rejeter
        v.append(valeur)
        p.append(poids_comb)
    return v, p

#################### Knapsack par bruteforce ###########################################
OBJETS =[["A",13,700], 
      ["B",12,500], 
      ["C",8,200], 
      ["D",10,300],
      ["E", 14,600],
      ["F",18,800]]
POIDS_MAX = 40

combinaisons = generer(len(OBJETS)) # On génère TOUTES les combinaisons
valeurs, poids = combinaisons_possibles(OBJETS, combinaisons, POIDS_MAX) # on retient celles
# qui respectent la contrainte POIDS_MAX.

valeur_maxi = max(valeurs)
indice_maxi = valeurs.index(valeur_maxi)

solution = combinaisons[indice_maxi]
poids_solution = poids[indice_maxi]
print(solution, poids_solution)