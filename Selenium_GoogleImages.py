#WARNING: The script wsdump is installed in '/var/data/python/bin' which is not on PATH.
#consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#Who knows
#It works just give it some time
import time
from selenium import webdriver

#Qualquer nome de variável
navegador = webdriver.Firefox()

#Acessar um site
navegador.get('https://www.google.com')

#Maximizar a tela
navegador.maximize_window()

#Encontrar vários elementos visíveis    
links_google = navegador.find_elements("class name", "gb_X")#Retorna uma lista de elementos
for i in links_google:#(I será cada item da lista, um por vez)
    if 'Imagens' in i.text:
        i.click()
        break

    #Agora está no GoogleImages

#Encontrar o primeiro elemento com essas condições.
pesquisa_google = navegador.find_element("id", "APjFqb")    
#Clicar em um elemento
pesquisa_google.click()
pesquisa_google.send_keys(input('Pesquise Imagens: '))#window.prompt('Pesquise Imagens:')
botaoPesquisar = navegador.find_elements('class name', 'gNO89b')
icounter = 0
for i in botaoPesquisar:
    icounter += 1
    try:
        i.click()
        break
    except:
        continue
print(icounter)
#No caso do navegador fechar sozinho
#time.sleep(10)
