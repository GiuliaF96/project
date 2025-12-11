def conta_caratteri(testo: str) -> int: #restituisce il numero totale di caratteri nella stringa (spazi inclusi).
    return len(testo)

def frequenza_caratteri(testo: str) -> dict[str, int]: #restituisce un dizionario dove la chiave è il carattere e il valore è il numero di volte che appare nel testo.
    frequenza = {}
    for char in testo:
        if char in frequenza:
            frequenza[char] += 1
        else:
            frequenza[char] = 1
    return frequenza

__all__ = ['conta_caratteri', 'frequenza_caratteri'] 