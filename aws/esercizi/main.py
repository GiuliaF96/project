

def valida_scelta(scelta : str) -> bool:
   scelta_tmp = scelta.upper()
   if scelta_tmp() == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
   else:
        return False 


def mostra_domanda() -> None:
    print(
        
        """

        Chi parteciperà a Sanremo 2026?

        A. Nayt
        B. La Nina
        C. J-AX
        D. Rocco Papaleo

        """

    )



    def raccogli_risposta() -> str:
        risposta: str = input("Inserisci la tua scelta: ")
        return risposta
    
    #mostra_domanda ()

   risposta_da_validare: str = raccogli_risposta()
risposta_validata: bool= valida_scelta(risposta_da_validare)

    print(risposta_validata)