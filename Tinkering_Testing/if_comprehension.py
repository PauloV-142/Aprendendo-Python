def letra():
    letr = input('Digite a letra: ')
    print("Vogal" if letr == 'a' else "Consoante")
    letra()
letra()