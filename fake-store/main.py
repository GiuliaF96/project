from requests import get, exceptions
from requests.exceptions import  HTTPError, ConnectionError, Timeout, RequestException


BASE_URL: str = "https://api.escuelajs.co/api/v1/products"
def get_data(URL: str) -> dict[str, any] | list[dict[str, any]]:
    if URL is None: 
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = get(URL)
        response.raise_for_status()
        return response.json()

    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}") from e


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
    
def scelta_prodotto()-> int:
    id_str = input("Inserisci l'id del prodotto da visualizzare: ")
    try:
        id = int(id_str)
        return id
    except ValueError:
        raise ValueError("L'id deve essere un numero intero valido.")

def scelta_menu() -> None:
    print("1. Visualizza elenco prodotti")
    print("2. Visualizza dettaglio prodotto")
    print("3. Esci")   
    scelta = input("Scegli un'opzione: ")
    if scelta == "1":
        products_data = get_data(BASE_URL)
        products = [product_model(prod) for prod in products_data]
        print_lista_prodotti(products)
    if scelta == "2":
        try: 
            id = scelta_prodotto()
            product= product_model(get_data(f"{BASE_URL}/{id}"))
            print_prodotto(product)
            return
        except Exception as e:
            print(f"Errore: {e}")

    elif scelta == "3":
        print("Uscita dal programma.")
        return
    
def main() -> None:
    scelta_menu()

    


    try: 
        id = input("Inserisci l'id del prdotto da visualizzare:")
        product= product_model(get_data(f"{BASE_URL}/{id}"))
        print_prodotto(product)

    except Exception as e:
        print(f"Errore: {e}")
   


    

if __name__ == "__main__":
    main()