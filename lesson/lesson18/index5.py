'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("會員登入")
        #self.geometry("300x250")
        #self.configure(background='#E79460')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both',padx=10,pady=10)

        #標題
        heading = ttk.Label(self,text="會員登入",font=('Helvetica',20),foreground='red')
        heading.grid(column=0,row=0,columnspan=2,padx=(20,0))

        username_label = ttk.Label(self,text="使用者名稱",font=('Helvetica',10))
        username_label.grid(column=0,row=1,pady=5,padx=(10,1))

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1,row=1,padx=(0,10))

        password_label = ttk.Label(self,text="使用者密碼",font=('Helvetica',10))
        password_label.grid(column=0,row=2,sticky='e',padx=(10,1))

        password_entry = ttk.Entry(self,show='幹')
        password_entry.grid(column=1,row=2,padx=(0,10))

        login_button = tk.Button(self,text='登入')
        login_button.grid(column=1,row=3,sticky='E',pady=5,padx=(0,10))

def main():    
    window = Window()
    myFrame = MyFrame(window,"系統登入")
    window.mainloop()

if __name__ == "__main__":
    main()