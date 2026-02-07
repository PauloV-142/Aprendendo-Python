def quantasFigurinhasFaltam():
    N = int(input("Tamanho do Álbum: "))
    M = int(input("Figurinhas já coladas: "))
    
    # Set pq ele não permite repetições por padrão!
    album = set()

    while True:
        # Cada input é uma figurinha comprada.
        X = int(input("N° da figurinha comprada: ")) 

        # Para o loop terminar.
        if X == 0:

            # N° de fig. que faltavam ANTES da compra.
            print(N - M)

            # N° de fig. que falta colar APÓS a compra das novas.
            print(N - len(album)) 
            print(0)

            return
        # A parte mais importante.
        # Adiciona a fig comprada ao contador.
        # Se o número na fig. for repetida, o set *não adiciona* por padrão.
        album.add(X)

quantasFigurinhasFaltam()