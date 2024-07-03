import tkinter as tk
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x500")
window.configure(bg="#E2D7A7")
window.title("Is it me you're looking for???")

tk.Label(window, text="Is it me you're\n looking for???", font=('Ariel', 25), bg= '#E0A370', width =20).pack()
status_label = tk.Label(window, text="Turn: YES", font=('Ariel', 15), bg= '#E0A370', width =35)
status_label.place(x = -40, y =430)
def play_again():
    global current_chr
    current_chr = 'Y'
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="Turn: YES", side = BOTTOM)
    play_again_button.pack_forget()
play_again_button = tk.Button(window, text='Play again', font=('Ariel', 15), bg= '#8DB4AD', command=play_again)

current_chr = "Y"

play_area = tk.Frame(window, width=400, height=500, bg='#E2D7A7')
XO_points = []
X_points = []
O_points = []
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, bg='#DF7669', command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='#709F9D')
            self.value = current_chr
            if current_chr == "Y":
                X_points.append(self)
                current_chr = "N"
                status_label.configure(text="Turn: NO")
            elif current_chr == "N":
                O_points.append(self)
                current_chr = "Y"
                status_label.configure(text="Turn: YES")
        check_win()

    def reset(self):
        self.button.configure(text="", bg='#DF7669')
        if self.value == "Y":
            X_points.remove(self)
        elif self.value == "N":
            O_points.remove(self)
        self.value = None
for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_chr == 'Y':
            for point in X_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == 'N':
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]
def disable_game():
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('Y'):
            status_label.configure(text="YES YOU ARE")
            disable_game()
            return
        elif possibility.check('N'):
            status_label.configure(text="NO YOU ARE NOT")
            disable_game()
            return
    if len(X_points) + len(O_points) == 9:
        status_label.configure(text="MAYBE!")
        disable_game()
play_area.pack(pady=10, padx=10)

window.mainloop()

