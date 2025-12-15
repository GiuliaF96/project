from data.repository import get_data, BASE_URL 
from data.services import print_lista_prodotti, print_prodotto, product_model
from console import scelta_menu, scelta_prodotto



    
def main() -> None:
    scelta_menu()

""" try: 
        id = input("Inserisci l'id del prdotto da visualizzare:")
        product= product_model(get_data(f"{BASE_URL}/{id}"))
        print_prodotto(product)

    except Exception as e:
        print(f"Errore: {e}")"""


if __name__ == "__main__":
    main()