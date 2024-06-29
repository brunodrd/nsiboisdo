def feuillage_2(hf):
    figure = ' '*(...) + '^' + '\n'
    for i in range(hf-1):
        figure += ' '*(...) + '/'
        for k in range(2*i+1):
            if k%2 == 0:
                car = "'"
            else:
                car = '"'
            figure += car
        figure += '\\' + '\n'
    return ...