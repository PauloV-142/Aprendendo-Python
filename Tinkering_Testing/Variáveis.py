# Variáveis string, Integer, Float, boolean
print(f"-------------------------------------------------------------------------")
#string
food = "Macarrão"
name = "Paulo"
email = "paulo142@sp.gov.br"
print(f"Eu gosto de {food}!")
print(f"Meu nome é {name}")
print(f"Meu email é: {email}")

#Integer
age = 15
print(f"Eu tenho {age} anos.")
#Float

price = 19.99
distance = 6.5
print(f"Custa {price}")
print(f"Eu corri {distance}km")

#Boolean
à_venda = True
if food == "Macarrão":
    if à_venda: #Se {} for verdade:
        print(f"{food} está a venda.")
    else:
        print(f"{food} não está a venda.")
print("-------------------------------------------------------------------------")