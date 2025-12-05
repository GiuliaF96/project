
products: list[dict] = [
{"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
{"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
{"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
{"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

inventario: float = 0 

for product in products:
  inventario += product["prezzo"] * product["quantita"]
  print(product["prezzo"]) if  product["prezzo"] > 100 else None

print(inventario)
	



