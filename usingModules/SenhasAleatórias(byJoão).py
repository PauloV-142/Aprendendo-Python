import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
import string

# Cria a aplicação
app = ttk.Window(themename="cosmo")

app.title('Gerador de Senhas Seguras')

app.geometry('400x300')

app.resizable(False, False)

# Adiciona campos de entrada e opções
length_lbl = ttk.Label(app, text="Comprimento da senha:")
length_lbl.pack(pady=5)
length = ttk.Entry(app)
length.pack(pady=5)

uppercase_var = ttk.BooleanVar()
uppercase_chk = ttk.Checkbutton(app, text="Incluir letras maiúsculas", variable=uppercase_var)
uppercase_chk.pack(pady=5)

lowercase_var = ttk.BooleanVar()
lowercase_chk = ttk.Checkbutton(app, text="Incluir letras minúsculas", variable=lowercase_var)
lowercase_chk.pack(pady=5)

numbers_var = ttk.BooleanVar()
numbers_chk = ttk.Checkbutton(app, text="Incluir números", variable=numbers_var)
numbers_chk.pack(pady=5)

special_var = ttk.BooleanVar()
special_chk = ttk.Checkbutton(app, text="Incluir caracteres especiais", variable=special_var)
special_chk.pack(pady=5)

result_lbl = ttk.Label(app, text="")
result_lbl.pack(pady=5)

# Função para gerar a senha
def gerar_senha():
    try:
        length_val = int(length.get())
        if length_val <= 0:
            result_lbl.config(text="Por favor, insira um comprimento válido")
            return
        
        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation
        
        if not characters:
            result_lbl.config(text="Por favor, selecione pelo menos uma opção")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length_val))
        result_lbl.config(text=f'Sua senha é: {password}')
    except ValueError:
        result_lbl.config(text="Por favor, insira um comprimento válido")

# Adiciona um botão para gerar a senha
btn = ttk.Button(app, text="Gerar Senha", bootstyle=SUCCESS, command=gerar_senha)
btn.pack(pady=20)

# Inicia o loop principal da aplicação
app.mainloop()
