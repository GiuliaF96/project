
utenti = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest",
}

for chiave, valore in utenti.items():
    print("*"*30)
    print(f"Usernames:{chiave}: Ruolo:{valore}")
        
print("*"*30)

if "bob" in utenti:
    print("bob presente: True")

print("*"*30)

dict_keys = utenti.keys()
print(f"Usernames: {list(dict_keys)}")
print("*"*30)

dict_values = utenti.values()
print(f"Ruoli:  {list(dict_values)}")
print("*"*30)


