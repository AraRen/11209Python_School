import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
from youbikeTreeView import YoubikeTreeView
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror('錯誤','網路錯誤\n將關閉應用程式\n請稍後再試')
            self.destroy()
        
        #print(datasource.last_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1,width=300,height=200)
        tk.Label(topFrame,text="台北市Youbike即時資料",font=("arial",20),bg="#333333",fg="#FFFFFF").pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        bottomFrame = tk.Frame(self)

        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show='headings',columns=('sna','sarea','mday','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack()
        bottomFrame.pack(pady=30)

        lastest_data = datasource.last_datetime_data()
        self.youbikeTreeView.update_content(lastest_data)



t = None
def main():
    def on_closing():
        print('視窗關閉')
        t.cancel()
        window.destroy()

    def updata_data()->None:
        datasource.updata_sqlite_data()
        global t
        t = Timer(20,updata_data)
        t.start()

    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    updata_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()


if __name__ == '__main__':
    main()