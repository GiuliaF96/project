from requests import get, exceptions
from requests.exceptions import  HTTPError, ConnectionError, Timeout, RequestException


BASE_URL: str = "https://api.escuelajs.co/api/v1/products"

"""def get_prodotto(URL: str)->dict[str,any]:
    if URL is None:
        raise ValueError(f"problema con la response:{e}")
    
    try: 
        response: Response= get_data()
        return response.json()
    except exceptions("L'URL non può essere vuoto!")"""



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