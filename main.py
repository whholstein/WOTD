# This is a sample Python script.

from word import WOTD
from datetime import date

if __name__ == '__main__':

    from tkinter import *
    from tkinter import ttk

    today = date.today().strftime("%B %d, %Y")

    # Collect Word of the Day
    try:
        results = WOTD()
        #print(results)

    except:
        exit(99)

    # Window definition
    root = Tk()
    root.title("Words of the day for " + today)

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text=results, borderwidth=2, relief="sunken",padding=10).grid(column=2, row=2, sticky=(W, E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Invoke Window
    root.mainloop()
