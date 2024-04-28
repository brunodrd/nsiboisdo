def ratio(objet):
    """ 
    Renvoie le rapport prix/poids d'un objet de type ["nom", poids, prix]
    """

    nom, poids, prix = objet
    # Rmq: 'nom' n'est jamais utilisé ici, il est d'usage d'utiliser la 
    # construction suivante: _, poids, prix = objet  en python.
    return prix / poids


def kp(objets, poids_max, poids_sac):
    """
    Renvoie la liste de nom des objets pris dans 'objets' et
    satisfaisant à la condition poids total < 'poids_max'
    """
    # Code à compléter
    butin = []
    objets_tries = sorted(objets, key=ratio, reverse=True)

    for nom, poids, prix in objets_tries:
        if poids + poids_sac <= poids_max:
            butin.append(nom)
            poids_sac += poids

    return butin
