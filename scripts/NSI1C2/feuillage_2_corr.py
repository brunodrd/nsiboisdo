def feuillage_2(hf):
    """
    Renvoie une chaîne de caractères correspondant au feuillage d'un sapin s'étendant sur hf lignes.
    """
    figure = ' '*(hf-1) + '^' + '\n'
    for i in range(hf-1):
        figure += ' '*(hf-i-2) + '/'
        for k in range(2*i+1):
            if k%2 == 0:
                car = "'"
            else:
                car = '"'
            figure += car
        figure += '\\' + '\n'
    return figure