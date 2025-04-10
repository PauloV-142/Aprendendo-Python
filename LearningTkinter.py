from tkinter import *
janela = Tk() #Instancia uma janela

janela.geometry('620x420')#AlturaXLargura

janela.title('Primeira GUI')#Título

#janelaIcone = PhotoImage(file='nome.png')
#janela.iconphoto(True,janelaIcone)

janela.config(background='#305f6f')#RRGGBB
'''
legenda = Label(janela,
                text=input('Título: '),
                font=('Arial',10,'bold'),
                fg='#ff55ff',
                bg='#4343ff',
                relief=RAISED,
                bd=2,#grossura da borda
                padx=2,
                pady=2)
legenda.pack()#No centro do topo como um título
#legenda.place(x=int(input('X=')),
#              y=int(input('Y=')))#Coordenadas
'''
def click():
    print('oi')
botão = Button(janela, text='Click!!!!')
botão.pack()
janela.mainloop()#Inicia uma janela na tela e executa enventos