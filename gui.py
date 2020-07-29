import tkinter as tk
from tkinter import messagebox
import random
from game import TicTacToeGame

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sage's Tic Tac Toe")
        self.root.geometry("420x520")
        self.root.config(bg="#F4F1EA")
        self.root.resizable(False, False)
        
        self.game = TicTacToeGame()
        
        self.paper_grains = [(random.randint(15, 345), random.randint(15, 345)) for _ in range(80)]
        
        self.create_widgets()
        self.animate_boil()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, 
            text="Player X's Turn", 
            font=("Comic Sans MS", 18, "bold"),
            bg="#F4F1EA",
            fg="#2C2C2C",
            pady=15
        )
        self.title_label.pack()

        self.canvas = tk.Canvas(
            self.root, 
            width=360, 
            height=360, 
            bg="#FAF7F2", 
            highlightthickness=2, 
            highlightbackground="#2C2C2C"
        )
        self.canvas.pack(pady=5)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.reset_btn = tk.Button(
            self.root,
            text="New Game",
            font=("Comic Sans MS", 12, "bold"),
            bg="#EFECE6",
            fg="#2C2C2C",
            relief=tk.RAISED,
            bd=3,
            padx=10,
            pady=2,
            command=self.reset_game
        )
        self.reset_btn.pack(pady=15)

    def draw_paper_texture(self):
        for x in range(30, 360, 30):
            self.canvas.create_line(x, 15, x, 345, fill="#EBE3D5", width=1)
        for y in range(30, 360, 30):
            self.canvas.create_line(15, y, 345, y, fill="#EBE3D5", width=1)
            
        for gx, gy in self.paper_grains:
            self.canvas.create_line(gx, gy, gx + 1, gy + 1, fill="#D8CEBE", width=1)

    def draw_sketch_line(self, x1, y1, x2, y2, color="#2C2C2C", width=2):
        offset_x = random.randint(-1, 1)
        offset_y = random.randint(-1, 1)
        self.canvas.create_line(
            x1 + offset_x, y1 + offset_y, 
            x2 + offset_x, y2 + offset_y, 
            fill=color, width=width, smooth=True
        )

    def draw_board_grid(self):
        self.draw_sketch_line(120, 20, 120, 340, width=3)
        self.draw_sketch_line(240, 20, 240, 340, width=3)
        self.draw_sketch_line(20, 120, 340, 120, width=3)
        self.draw_sketch_line(20, 240, 340, 240, width=3)

    def draw_x(self, x1, y1, x2, y2):
        for _ in range(3):
            dx1 = x1 + random.randint(-4, 4)
            dy1 = y1 + random.randint(-4, 4)
            dx2 = x2 + random.randint(-4, 4)
            dy2 = y2 + random.randint(-4, 4)
            self.canvas.create_line(dx1, dy1, dx2, dy2, fill="#2E7D32", width=3, smooth=True)
            
            dx3 = x2 + random.randint(-4, 4)
            dy3 = y1 + random.randint(-4, 4)
            dx4 = x1 + random.randint(-4, 4)
            dy4 = y2 + random.randint(-4, 4)
            self.canvas.create_line(dx3, dy3, dx4, dy4, fill="#2E7D32", width=3, smooth=True)

    def draw_o(self, cx, cy, r):
        for _ in range(3):
            rx = r + random.randint(-3, 3)
            ry = r + random.randint(-3, 3)
            self.canvas.create_oval(
                cx - rx, cy - ry, cx + rx, cy + ry,
                outline="#1565C0", width=3
            )

    def redraw_canvas(self):
        self.canvas.delete("all")
        self.draw_paper_texture()
        self.draw_board_grid()

        cell_size = 120
        for r in range(3):
            for c in range(3):
                player = self.game.board[r][c]
                x_center = c * cell_size + cell_size // 2
                y_center = r * cell_size + cell_size // 2

                if player == "X":
                    self.draw_x(x_center - 35, y_center - 35, x_center + 35, y_center + 35)
                elif player == "O":
                    self.draw_o(x_center, y_center, 35)

    def animate_boil(self):
        self.redraw_canvas()
        self.root.after(110, self.animate_boil)

    def on_canvas_click(self, event):
        if self.game.winner or self.game.is_tie:
            return

        col = event.x // 120
        row = event.y // 120

        if 0 <= row < 3 and 0 <= col < 3:
            if self.game.make_move(row, col):
                if self.game.winner:
                    self.title_label.config(text=f"Player {self.game.winner} Wins!")
                    messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                elif self.game.is_tie:
                    self.title_label.config(text="It's a Tie!")
                    messagebox.showinfo("Game Over", "It's a tie!")
                else:
                    self.title_label.config(text=f"Player {self.game.current_player}'s Turn")

    def reset_game(self):
        self.game.reset()
        self.title_label.config(text=f"Player {self.game.current_player}'s Turn")
