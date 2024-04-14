def ratio(objet):
    # renvoie le rapport prix/poids d'un objet
    return objet[2] / objet[1]


def kp(objets, poids_max, poids_sac):
    """
    Renvoie la liste des objets pris dans 'objets' et
    satisfaisant à la condition 'poids_max'
    """
    # Code à compléter
    butin = []
    obj_tries = sorted(objets, key = ratio, reverse = True)

    for i in range(len(obj_tries)):
        poids_objet = obj_tries[i][1]
        if ... :
            butin.append(...)
            poids_sac += ...

    return butin
