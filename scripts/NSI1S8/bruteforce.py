obj =[["A",13,700], 
      ["B",12,500], 
      ["C",8,200], 
      ["D",10,300],
      ["E", 14,600],
      ["F",18,800]]

poids_max = 40

comb = []
for i in range(2**len(obj)):
    k = bin(i)[2:]
    s = '0'*(len(obj)-len(k)) + k
    comb.append(s)

v = [] 
p = []
for k in comb :
    poids_comb = 0
    valeur = 0
    for i in range(len(obj)): 
        if k[i] == '1':
            poids_comb += obj[i][1]
            valeur += obj[i][2]
    if poids_comb > poids_max :
        valeur = 0
    v.append(valeur)
    p.append(poids_comb)

m = max(v)
sol_comb = comb[v.index(m)]
poids_comb = p[v.index(m)]