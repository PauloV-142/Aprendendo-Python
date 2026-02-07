from tkinter import *

# Initialize the root window
root = Tk()
root.title('Jogo Da Velha')
root.config(background='#305f6f')  # RRGGBB
root.geometry('400x400')

# Game variables
jogador = 1
pontosx = 0
pontoso = 0
empates = 0
l_scores = [0] * 8  # Tracks scores for rows, columns, and diagonals
ocupados = set()  # Tracks occupied positions
buttons = {}  # Maps positions to buttons

# Images for X and O
imagemx = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-cross-90.png')
imagemo = PhotoImage(file='/sysroot/home/user/Documentos/Programaçao/VSCode Python/usingModules/TicTacToe/icons8-circle-64.png')

# Labels for scores
lblx = Label(font=('mono', 50, 'bold'), text='X: 0', bg='#305f6f', fg='white')
lblo = Label(font=('mono', 50, 'bold'), text='O: 0', bg='#305f6f', fg='white')
lble = Label(font=('mono', 50, 'bold'), text='Empates: 0', bg='#305f6f', fg='white')

# Helper functions
def MudarJogador():
    """Switches the current player."""
    global jogador
    jogador = 2 if jogador == 1 else 1

def xo():
    """Returns the image for the current player."""
    return imagemx if jogador == 1 else imagemo

def check_winner():
    """Checks if there's a winner or a draw."""
    global pontosx, pontoso, empates

    # Check for a win
    if 3 in l_scores:
        print("X Ganhou!")
        pontosx += 1
        lblx.config(text=f'X: {pontosx}')
        highlight_winner(3)
        disable_all_buttons()
        return #end function
    elif -3 in l_scores:
        print("O Ganhou!")
        pontoso += 1
        lblo.config(text=f'O: {pontoso}')
        highlight_winner(-3)
        disable_all_buttons()
        return

    # Check for a draw
    if len(ocupados) == 9:
        print("Deu velha! (Empate!)")
        empates += 1
        lble.config(text=f'Empates: {empates}')
        disable_all_buttons()

def highlight_winner(score):
    """Highlights the winning row, column, or diagonal."""
    winning_indices = [i for i, val in enumerate(l_scores) if val == score]
    for index in winning_indices:
        if index < 3:  # Rows
            for col in range(3):
                buttons[(index + 1, col)].config(bg='#ffcc66')
        elif index < 6:  # Columns
            for row in range(3):
                buttons[(row, index - 3)].config(bg='#ffcc66')
        else:  # Diagonals
            if index == 6:
                for i in range(3):
                    buttons[(i, i)].config(bg='#ffcc66')
            elif index == 7:
                for i in range(3):
                    buttons[(i, 2 - i)].config(bg='#ffcc66')

def button_click(row, col):
    """Handles button clicks."""
    global l_scores

    # Mark the button
    buttons[(row, col)].config(image=xo(), height=83, width=92, state=DISABLED)
    ocupados.add((row, col))

    # Update scores
    score = 1 if jogador == 1 else -1
    l_scores[row] += score  # Row
    l_scores[col + 3] += score  # Column
    if row == col:
        l_scores[6] += score  # Main diagonal
    if row + col == 2:
        l_scores[7] += score  # Anti-diagonal

    # Check for a winner or draw
    check_winner()

    # Switch player
    MudarJogador()

def disable_all_buttons():
    """Disables all buttons."""
    for button in buttons.values():
        button.config(state=DISABLED)

def enable_all_buttons():
    """Resets the game state and enables all buttons."""
    global l_scores, ocupados, jogador
    l_scores = [0] * 8
    ocupados = set()
    # Alterna o jogador inicial com base no total de pontos e empates.
    # Se a soma for ímpar, o jogador inicial será "O" (2). Caso contrário, será "X" (1).
    jogador = 2 if (pontosx + pontoso + empates) % 2 == 1 else 1 #Gut
    for button in buttons.values():
        button.config(image='', bg='#99ccff', state=ACTIVE, height=5, width=10)

# Create buttons and grid
for row in range(3):
    for col in range(3):
        button = Button(root, bg='#99ccff', activebackground='#6699ff', height=5, width=10,
                        command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row + 1, column=col)
        buttons[(row, col)] = button

# Place labels and reset button
lblx.grid(row=4, column=0)
lblo.grid(row=4, column=1)
lble.grid(row=4, column=2)
Button(root, font=('mono', 30, 'bold'), text='New round', command=enable_all_buttons).grid(row=5, column=1)

# Run the main loop
root.mainloop()