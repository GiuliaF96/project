
prezzi = [45.5, 12.0, 78.3, 23.1, 56.7]

prezzi_ordinati = sorted(prezzi)
print(prezzi_ordinati)

print(min(prezzi))

print(max(prezzi))  

#if 23.1 in prezzi: 
   # print("Il prezzo 23.1 è presente nella lista")
print(23.1 in prezzi)

prezzo_maggiore = 50
#prezzi_maggiori = [prezzo for prezzo in prezzi if prezzo > prezzo_maggiore]

prezzi_maggiori = list(filter(lambda prezzo: prezzo > prezzo_maggiore, prezzi))


print(len(prezzi_maggiori))

counter = 0 
"""
for x in prezzi_ordinati:
	if x > 50:
	counter +=1

print(counter)
"""
