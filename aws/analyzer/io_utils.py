def leggi_file(percorso: str) -> str: #accetta il percorso di un file e ne restituisce il contenuto come stringa. Gestite eventuali errori se il file non esiste.
    percorso = percorso.strip() 
    try:
        with open(percorso, 'r') as file:
            contenuto = file.read()
        return contenuto
    except FileNotFoundError:
        print(f"Errore: Il file '{percorso}' non esiste.")
        return ""

percorso = leggi_file("testi.txt") 

__all__ = ['leggi_file'] 