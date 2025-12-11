from io_utils import leggi_file
from text_analizer import conta_caratteri, frequenza_caratteri

print("Benvenuto nell'analizzatore di testo!")
percorso_file = input("Inserisci il percorso del file di testo da analizzare: ")


# 2. Leggo il testo
try:
    testo = leggi_file(percorso_file)
except FileNotFoundError:
    print("Errore: file non trovato!")
    exit()
testo = leggi_file(percorso_file)

totale_caratteri = conta_caratteri(testo)
print(f"\nNumero totale di caratteri: {totale_caratteri}")
frequenze = frequenza_caratteri(testo)

leggi_file()
conta_caratteri()
frequenza_caratteri()




"""
Step 3: Il programma principale Create un file main_analyzer.py. Questo sarà il punto di ingresso del programma.
Importate le funzioni create nello Step 1 e Step 2.
Il programma deve chiedere all'utente il percorso di un file di testo (potete crearne uno di prova, es: prova.txt).
Utilizzando le funzioni importate, il programma deve stampare a video:
Il numero totale di caratteri.
Solo i caratteri che compaiono più di 5 volte (usando il dizionario delle frequenze).

"""