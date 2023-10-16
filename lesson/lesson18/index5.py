'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("資料列表")
        #self.geometry("300x250")
        #self.configure(background='#E79460')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both',padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3'],show='headings')
        self.tree.heading('#1',text='第一個')
        self.tree.heading('#2',text='第二個')
        self.tree.heading('#3',text='第三個')

        contacts = []
        for n in range(1,11):
            contacts.append([f'first{n}',f'last{n}',f'email{n}:example.com'])
        
        for contact in contacts:
            self.tree.insert('',tk.END,values=contact)
        self.tree.pack()

    def choised(self):
        print(self.aligement.get())

def main():    
    window = Window()
    myFrame = MyFrame(window,"資料列表")
    window.mainloop()

if __name__ == "__main__":
    main()