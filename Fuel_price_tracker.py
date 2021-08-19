from tkinter import*
import requests
from bs4 import BeautifulSoup
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox


class fuel_tracker:
    def __init__(self,root):
      self.root=root
      self.root.geometry("800x500+350+40")
      self.root.title("Fuel Price Tracker")
      self.root.iconbitmap("images/number.ico")
      self.root.resizable(False,False)
      

      self.background=Label(self.root,bg="black").place(x=0,y=0,relwidth=1,relheight=1)
      self.bg=PhotoImage(file=r"images/fuel.png")
      self.bg_image=Label(self.root,image=self.bg,bd=0).place(x=500,y=95)

      welcome_lbl=Label(self.root,text="--- Welcome to  The System ---",font="timesnewroman 14 bold underline",bg="black",fg="#58D68D",bd=0)
      welcome_lbl.place(x=250,y=20)

      title1=Label(self.root,text="State/City :-",font="timesnewroman 14 bold ",fg="#04B4AE",bg="black",bd=0)
      title1.place(x=50,y=100)

      self.type_var=StringVar()
      self.choose=ttk.Combobox(self.root,font=("times new roman",15,"bold"),state="readonly",textvariable=self.type_var)
      self.choose["values"]=("Select","state","city")
      self.choose.place(x=180,y=100,width=255,height=35)
      self.choose.current(0)

      title2=Label(self.root,text="Enter :-",font="timesnewroman 14 bold ",fg="#04B4AE",bg="black",bd=0)
      title2.place(x=60,y=150)

      self.name_var=StringVar()
      self.entry_window02=Entry(self.root,borderwidth=4,width=25,textvariable=self.name_var,relief=SUNKEN,bg="#FF7F50",fg="black",font="timesnewroman 14 bold")
      self.entry_window02.place(x=180,y=150,width=255,height=35)

      
      self.fuel_info=Label(self.root,text="Save Fuel Save Earth.",font="timesnewroman 14 bold ",fg="red",bg="black",bd=0)
      self.fuel_info.place(x=200,y=200,height=85)


      self.check=Button(self.root,text="Check",width=15,borderwidth=4,relief=SUNKEN,bg="#FF0040",fg="yellow",command=self.get_fuel_data,font="timesnewroman 10 bold")
      self.check.place(x=230,y=350)

      qui=Button(self.root,text="Quit",width=12,borderwidth=4,relief=SUNKEN,bg="#0A1B2A",font="timesnewroman 10 bold",fg="white",command=self.root.quit)
      qui.place(x=240,y=400)

    #### function declaration and definition ######
    def get_fuel_data(self):
      x=self.type_var.get()
      y=self.name_var.get()

      z=y.replace(" ","-")

      if x=="state":
        self.html_data=requests.get("https://www.ndtv.com/fuel-prices/diesel-price-in-"+z+"-state")
        self.beautify=BeautifulSoup(self.html_data.text,'html.parser')
        self.info_div=self.beautify.find("div",class_="tb-bar")
        self.fuel_info['text']=self.info_div.get_text()

 
      else:
        self.html_data=requests.get("https://www.ndtv.com/fuel-prices/diesel-price-in-"+z+"-city")
        self.beautify=BeautifulSoup(self.html_data.text,'html.parser')
        self.info_div=self.beautify.find("div",class_="tb-bar")
        self.fuel_info['text']=self.info_div.get_text()

      self.clear()

    def clear(self):
      self.type_var.set("Select")
      self.name_var.set("")

        
      
      

if __name__ == "__main__":
    root=Tk()
    obj=fuel_tracker(root)
    root.mainloop()
    
