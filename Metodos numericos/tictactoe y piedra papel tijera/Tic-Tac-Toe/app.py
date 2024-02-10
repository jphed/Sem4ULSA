import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'

        # crea botones
        self.buttons = [tk.Button(self.window, text='',
                         command=lambda i=i: self.move(i), font=('Arial', 24), width=5, height=2) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def move(self, square):
        if self.buttons[square]['text'] == '':  # si el cuadrado está vacío
            self.buttons[square]['text'] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # cambiar jugador

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()