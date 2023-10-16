'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("400x250+300+300")
        self.title("Lines")
        self.configure(background='#DB4D6D')

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master=master,**kwargs)
        self.configure(background='#DC9FB4')
        self.pack(expand=1, fill="both")


def main():
    window = Window()
    myFrame = MyFrame(master=window)
    window.mainloop()
    
if __name__ == "__main__":
    main()