import tkinter as tk
import pyautogui

class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('auto clicker')
        self.win.geometry('400x500')
        self.win.resizable(width=False, height=False)


def main():
    win = Window()
    win.win.mainloop()

if __name__ == '__main__':
    main()