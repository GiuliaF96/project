"""
PROGRAMMA PER CARRELLO SPESA
Obiettivo: Creare un programma che simuli una spesa al supermercato. 
Il programma deve gestire una Lista della Spesa (ciò che devi comprare) e un Carrello (ciò che stai prendendo).
Scenario: Siamo nel 2050. I carrelli del supermercato sono robotizzati. 
Per evitare sprechi, il carrello si rifiuta di aprirsi se cerchi di inserire un prodotto 
che non è nella tua lista della spesa digitale.

1. lista della spesa
2. carrello
    -input prodotti
3. if/else se i prodotti aggiunti al carrello sono presenti in lista
    - se già presenti reinserire un altro prodotto nel carrello
    - se non presenti in lista messaggio di errore
    - input è vuoto?
    -caratteri piccoli
    -se il prodotto passa i controlli aggiungi alla lista
    -altrimenti restituisci errore e poi input
4. aprire carrello
5.if/else lista== carrello 
6. spesa finita 
"""




def is_lista_carrello_filled(lista_carrello:list[str]) -> bool:

    if len(lista_carrello) < 5:
        return True
    else: 
        False 

def get_input_utente(text:str):
    if not text:
        print("Il messaggio non può essere vuoto")
    print("*"*30)
    return input(text)

def get_prodotto_formattato(prodotto: str) -> str:
    if not prodotto:     
            print("Il prodotto non deve essere vuoto")
    return prodotto.strip().lower()


def log_message(text: str, type):
    icon= None
    match type:
        case "ALERT":
            icon = "⚠️"

        case "ADD":
            icon =   "✅"

        case "PRESENTE":
            icon =   "⚠️"

        case "NON":
             icon = "⚠️"

        case "END":
             icon = "⛔"

    print(f"{icon}-{text}") 


def main():
    
    lista_spesa : list[str] = ["pane","pasta", "uova","latte", "biscotti"]
    lista_carrello : list[str] = []

    while is_lista_carrello_filled(lista_carrello):
        prodotto = get_input_utente("Inserisci un un prodotto da aggiungere al carrello: ")
        if not prodotto:     
            log_message("Il prodotto non deve essere vuoto", "ALERT")

        prodotto_formattato : str = get_prodotto_formattato(prodotto)
        
        if prodotto_formattato  in lista_spesa:
            if prodotto_formattato in lista_carrello:
                log_message("CARRELLO CHIUSO: Il prodotto è gia nel carrello", "PRESENTE")
            else: 
                print("CARRELLO APERTO: ")
                lista_carrello.append(prodotto_formattato)
                log_message(lista_carrello, "ADD")
               

        else: 
            log_message("IIMPOSSIBILE APRIRE IL CARRELLO: Prodotto non valido", "NON")
            
            
    log_message("Carrello completo", "END")



    return

main()
