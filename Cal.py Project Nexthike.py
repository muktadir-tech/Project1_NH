import tkinter as tk

# Colors and Fonts
BG_COLOR = "#f3f4f6"
BTN_COLOR = "#e0e0e0"
HOVER_COLOR = "#d5d5d5"
DISPLAY_COLOR = "#ffffff"
FONT = ("Segoe UI", 18)

# Hover effect functions
def on_enter(e):
    e.widget["bg"] = HOVER_COLOR

def on_leave(e):
    e.widget["bg"] = BTN_COLOR

# Calculator logic
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Muktadir's Calculator")
        self.geometry("350x550")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Display Entry
        self.display = tk.Entry(self, font=("Segoe UI", 24), bg=DISPLAY_COLOR, fg="black", bd=0, justify='right')
        self.display.pack(fill='both', ipadx=8, ipady=20, padx=10, pady=10)

        # Buttons layout
        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack()

        buttons = [
            ['C', '←', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]

        for row in buttons:
            row_frame = tk.Frame(btn_frame, bg=BG_COLOR)
            row_frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(
                    row_frame, text=btn_text, font=FONT, bg=BTN_COLOR, fg="black",
                    relief="flat", height=2, width=5, command=lambda b=btn_text: self.on_button_click(b)
                )
                btn.pack(side='left', expand=True, fill='both', padx=1, pady=1)
                btn.bind("<Enter>", on_enter)
                btn.bind("<Leave>", on_leave)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
