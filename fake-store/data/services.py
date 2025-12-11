

def print_prodotto(product: dict[str, any]) -> None:
    print("*" * 30)
    print(f"PRODOTTO")
    print("*" * 30)
    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Category: {product["category"]}")
    print(f"PRICE: {product["price"]}")
    print(f"DESCRIPTION: {product["description"]}")

def print_lista_prodotti(products: list[dict[str, any]]) -> None:
    print("*" * 30)
    print(f"ELENCO PRODOTTI")
    print("*" * 30)
    for product in products:
        print(f"ID: {product['id']} - Titolo: {product['title']}")


def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }
    