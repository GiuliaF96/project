"""
- input -> programma-> output

Tipi di input:
-file nel file system
    -open("nomefile", "r")
-input da parte dell'utente
-dati che vengono da altri pc sulla rete

Tipi di output:
-file nel file system
    -open("nomefile", "w")
-output UI
-dati che vengono mandati ad altri pc sulla rete
- programma = set istruzioni
"""

"""def main(): #funzione- set istruzioni
    "istruzione 1"
    "istruzione 2"
    "istruzione 3"
"""
#dividere funzioni 
"""
def esegui_da_uno_a_due():
    "istruzione 1"
    "istruzione 2"

def main(): #funzione- set istruzioni
    
    esegui_da_uno_a_due()
    "istruzione 3"
    esegui_da_uno_a_due()

    return

    """
"""
def main():
    
    1. prendi il codice da questo file 
    2. leggi tutto il codice e scomponilo i ogni parola
    3. ogni parola a cosa corrisponde
   
     es.pizza
    
    1. prendi farina
    2. prendi lievito
    3. prendi acqua
    4. mischia farina lievito e acqua

    a = "farina"
    b = "lievito"
    c = "acqua"
    
    d = "farina" + "lievito" + "acqua"

    return

"""
"""
PROGRAMMA PER FARE LA PIZZA
-un programma che prenda gli ingredienti per fare
la pizza dall'utente,attraverso input testuale e restituisca
il risultato finale a schermo.
Il computer non sa fare la pizza quindi dobbiamo istruirlo noi.

-Passi:
1. prendi ingredienti da utente( interagisci con l'utente)(input)-> if / else per controllare input-> output
2. -prendi farina
3. -prendi acqua
4. -prendi lievito

--cosa serve
- input
    -perchè voglio prendere gli ingredienti dall'utente
-lista ingredenti ricetta
-lista ingredienti inseriti dall'utente
- if/else
    - input è vuoto?
    -caratteri piccoli
    -controllo che l'ingrediente non sia già inserito
    -se l'ingrediente passa i controlli aggiungi alla lista
    -altrimenti restituisci errore e poi input

-if / else
    -se la lista degli ingredieti ricetta == alla lista ingredienti inserita 
        dall'utente allora impasti
        -gli ingredienti sono 3?
        -controllo con un ciclo quali sono gli ingredienti che mancano
    -altrimenti riproponi input con messaggio degli ingredienti che mancano


5. impastala pizza
6. stendi pallina
7. prendi pomodoro
8. prendi mozzarella
9. metti pomodoro
10. metti mozzarella
11. metti in forno la pizza
12. sforna la pizza

"""
#venv creare ambiente per non far andare in conflitto le versioni dei software

def is_lista_utente_filled(lista_utente:list[str]) -> bool:

    if len(lista_utente) < 3:
        return True
    else: 
        False 

def get_ingrediente_formattato(ingrediente: str) -> str:
    if not ingrediente:     
            print("L'ingrediente non deve essere vuoto")
    return ingrediente.strip().lower()

def get_input_from_utente(text: str)-> str:
    if not text:
        print("Il messaggio non può essere vuoto")
    print("*"*30)
    return input(text)

def log_message(text: str, type):
    icon= None
    match type:
        case "ALERT":
            icon = "⚠️"

        case "INFO":
            icon =   "✅"

        case "PRESENTE":
            icon =   "⚠️"

        case "NON":
             icon = "⚠️"

        case "END":
             icon = "⛔"

    print(f"{icon}-{text}") 


    """match type:
        case "ALERT":
            print(f"⚠️-{text}")
        case "INFO":
            print(f"✅-{text}")
        case "PRESENTE":
            print(f"⚠️-{text}")
        case "NON":
            print(f"⚠️-{text}")

            """
    
        
  

def main()-> None:
    log_message("Start del programma", "INFO")

    lista_ricetta: list[str] = ["farina", "acqua", "lievito"]
    lista_utente: list[str] = []

    while is_lista_utente_filled(lista_utente):
        ingrediente = get_input_from_utente("Inserisci un ingrediente: ")
        if not ingrediente:     
            log_message("L'ingrediente non deve essere vuoto", "ALERT")
       
        ingrediente_formattato: str = get_ingrediente_formattato(ingrediente)

        if ingrediente_formattato  in lista_ricetta:
            if ingrediente_formattato in lista_utente:
                log_message("ingrediente già nella ricetta", "PRESENTE")
            else: 
                lista_utente.append(ingrediente_formattato)
                print(lista_utente)

        else: 
            log_message(" Ingrediente non valido", "NON")
            
            
    print("impasta e fai la pizza")
    log_message("End del programma", "END")


main()
 




