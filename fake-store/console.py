from data.repository import get_data, BASE_URL
from data.services import print_lista_prodotti, print_prodotto, product_model

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