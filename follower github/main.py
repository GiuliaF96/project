
from requests import get
import re

BASE_URL: str = "https://github.com" 
END_URL: str = "tab=followers"

PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'
PATTERN_USER = r'<span class="Link--secondary(?: pl-1)?">([^<]+)</span>'
def is_next_button_present(text: str) -> bool:
  if not text:
    raise ValueError("La stringa non puo essere vuota!")

  return bool(re.search(PATTERN, text))

def main() -> None:
    counter: int = 0

    print("Start del programma")

    while True:
     try: 

        nome_utente: str = input("Inserisci lo username del profilo gitHub che vuoi analizzare: ")
        
        if not nome_utente:
            raise ValueError("Il nome utente non può essere vuoto")
        #TODO: il nome utente exit è presente
        if nome_utente.strip().lower() == "exit":
            break
        
        print(f"Stai cercando: {nome_utente}")
       
        response = get(f"{BASE_URL}/{nome_utente}")

        if response.status_code == 404:
                print("Il profilo non esiste")
            
        else: 
                print(f"Profilo {nome_utente} trovato")
                controller = True 
                break

     except Exception as e:
            print(f"Qualcosa è andato storto. Messaggio:{e}")
            
        
    while controller:
        counter +=1
        url = f"{BASE_URL}/{nome_utente}?page={counter}&{END_URL}"
        try:
            response = get(url)
            print(f"Errore: {response.status_code}")
        

            with open(f"tmp/pagina-{counter}.txt", "w") as f:
        
                f.write(response.text)
                controller = is_next_button_present(response.text)
                print("File salvato")


        except Exception as e:
            print(f"Errore: {e}") 
    lista_utenti: list[str] = []

    for i in range(counter):
        print(f"Couter: {i+1}")
        with open(f"tmp/pagina-{i+1}.txt", "r") as f:
            text = f.read()
            lista_utenti.extend(re.findall(PATTERN_USER, text))

        print(lista_utenti)

        print("Fine programma.\nArrivederci")
 
if __name__ == "__main__":
  main()