PIECES = [100, 50, 20, 10, 5, 2, 1] # système monnaitaire canonique

assert rendu_aux(0, [], 0) == []
assert rendu_aux(37, [], 0) == [20, 10, 5, 2]
assert rendu_aux(300, [], 0) == [100, 100, 100]