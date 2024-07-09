assert appartient(5, []) == False
assert appartient(5, [1,2,3,4]) == False
assert appartient(5, [1,2,3,4,5]) == True
assert appartient(5, [1]) == False
assert appartient(5, [5]) == True