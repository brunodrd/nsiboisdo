assert occurences(-1, [2,3,4,5,-1,6,7,-1]) == 2
assert occurences(-1, [2,3,4,5,1,6,7,1]) == 0
assert occurences(1, [1,1,1,1,1,1,1,1]) == 8