a = [32, 32, 32, 32, 94, 10, 32, 32, 32, 47, 39, 92, 10, 32, 32, 
     47, 39, 34, 39, 92, 10, 32, 47, 39, 34, 39, 34, 39, 92, 10, 
     47, 39, 34, 39, 34, 39, 34, 39, 92, 10]

b = [32, 32, 32, 32, 32, 32, 94, 10, 32, 32, 32, 32, 32, 47, 39, 
     92, 10, 32, 32, 32, 32, 47, 39, 34, 39, 92, 10, 32, 32, 32,
     47, 39, 34, 39, 34, 39, 92, 10, 32, 32, 47, 39, 34, 39, 34, 
     39, 34, 39, 92, 10, 32, 47, 39, 34, 39, 34, 39, 34, 39, 34, 
     39, 92, 10, 47, 39, 34, 39, 34, 39, 34, 39, 34, 39, 34, 39, 
     92, 10]
assert feuillage_2(5) == ''.join([chr(c) for c in a])
assert feuillage_2(7) == ''.join([chr(c) for c in b])