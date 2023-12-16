# Oliwia Rogowska #
#   Zadanie 10    #
#     Python      #
#   16.12.2023    #
###################
import random
import sys
import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None, title="Roll a dice"):
        tk.Frame.__init__(self, master)
        self.rolled_number = tk.StringVar()
        self.master = master
        self.master.title(title)
        self.grid()
        self.create_widgets()

    def roll(self):
        self.rolled_number.set(str(random.randint(1, 6)))

    def create_widgets(self):
        self.label = tk.Label(root, textvariable=self.rolled_number, font="Symbol 20 bold")
        self.label.grid(row=0, column=0, sticky=tk.NSEW)
        self.button = tk.Button(root,
                                text="roll",
                                width=25,
                                height=5,
                                bg="white",
                                fg="gray",
                                command=self.roll,
                                )
        self.button.grid(row=1, column=0, sticky=tk.NSEW)
        self.button = tk.Button(root,
                                text="quit",
                                width=25,
                                height=5,
                                bg="white",
                                fg="gray",
                                command=sys.exit,
                                )
        self.button.grid(row=2, column=0, sticky=tk.NSEW)



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
