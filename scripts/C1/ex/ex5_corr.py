def placer(x, t):
    if len(t) == 0:
        return [x]
    elif x < t[0]:
        return [x] + [elt for elt in t]
    else:
        return [t[0]] + placer(x, t[1:])