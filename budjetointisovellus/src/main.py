from tkinter import Tk
from ui.gui import GUI

def main():
    """Luokka, joka vastaa sovelluksen graafisen käyttöliittymän käynnistämisestä.
    """
    window = Tk()
    window.title("BudgetingApp")
    ui_view = GUI(window)
    ui_view.start()
    window.mainloop()

if __name__ == "__main__":
    main()
