# Chavosh_Exchange : You can buy currency.
# Designed and created by Mahan Chavoshian!

from tkinter import Tk,Label,Button,Entry,Checkbutton,Toplevel,LabelFrame,Spinbox,Radiobutton,StringVar,Frame
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo,showerror
from time import strftime
from random import randint
from PIL import Image,ImageTk
from os import system
from platform import system as sys

def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")

terminal_cleaner()

root = Tk()
root.title("Chavosh_Exchange 2.0")
root["bg"] ="#0f0f0e"

country_dict ={
    "Argentina" : "Peso",
    "Australia" : "Australian_dollar",
    "Azerbaijan" : "Manat",
    "Brazil" : "Real",
    "Canada" : "Canada_dollar",
    "China" : "Chinese_Yuan",
    "USA" : "Dollar",
    "Russia" : "Ruble",
    "Bahrain" : "Bahrain_dinar",
    "Denmark" : "Danish_Krone",
    "Egypt" : "Egyptian_pound" ,
    "Finland":"Euro",
    "France": "Euro",
    "Georgia" : "Lari",
    "India" : "Indian_Rupee",
    "Iraq" : "Iraqi_Dinar",
    "Japan" : "Yen",
    "Kuwait" : "Kuwaiti_Dinar",
    "Mexico" : "Mexican_peso",
    "Oman" : "Omani_rial",
    "Turkey" : "Turkish_lira",
}

price_dict ={
   "Argentina" : 200,
   "Australia" : 38_000,
   "Azerbaijan" : 30_000,
   "Brazil" : 10_500,
   "Canada" : 30_000,
   "China" :  7_000,
   "USA" : 51_000,
   "Russia" : 650,
   "Bahrain" : 133_000,
   "Denmark": 7_300,
   "Egypt": 1_600,
   "Finland": 54_000,
   "France": 54_000,
   "Georgia" : 19_200,
   "India": 600,
   "Iraq" : 38,
   "Japan" : 340,
   "Kuwait" : 160_000,
   "Mexico": 2_900 ,
   "Oman": 129_000 ,
   "Turkey": 1900,
}

question_list = ["Yes","No"]
country_list = list(country_dict.keys())

black_cnf ={
    "bg" : "#0f0f0e",
    "fg" : "#fafaf5",
    "font" : ("Arial",16)
}

orange_cnf = {
    "bg" : "#f79102",
    "fg" : "#fafaf5",
    "font" : ("Arial",16)
}

def country():
        totalprice = (Argentina_money+ Australia_money+Azerbaijan_money+Brazil_money+Canada_money+China_money+usa_money+Russia_money+Bahrain_money+Denmark_money+Egypt_money+Finland_money+France_money+Georgia_money+India_money+Iraq_money+Japan_money+Kuwai_money+Mexico_money+Oman_money+Turkey_money)
        recipttime = strftime("%H:%M")
        recipt = open("Recipt.txt","a")
        recipt.write(f"\n")
        recipt.write(30*".__.")
        recipt.write(f"\nTime: {recipttime}")
        recipt.write("\nThanks for your purchase!")
        recipt.write(f"\nPrice: {totalprice}Toman")
        recipt.write("\nWe are glad that you choose one of the best exchanges!")
        recipt.close()

def refresh2():
    global country_get
    country_get = country_cb1.get()
    currency = country_dict[country_get]
    currency_cb.config(text=f"{currency}")
    currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")
    price = price_dict[country_get] 
    price_label1.config(text=f"{price}Toman")
    price_label1.grid(row=3 , column=0 ,padx=10,pady=10,sticky="nsew")

def refresh():
    global country_get
    country_get = country_cb2.get()
    currency = country_dict[country_get]
    currency_cb = Combobox(master=second_label_ftame,values=currency,font=("Arial",16))
    currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")

def send():
  showerror(title="Follow!",message="Follow me in GitHub!\nDesigned by: Mahan Chavoshian")
  showinfo(title="Send!",message="Your comment has been recorded!")
  root.destroy()

def opinion():
   final_window = Toplevel()
   final_window.title("Chavosh_Exchange")
   final_window ["bg"] = "#0fbf4a"
   alaki_var = StringVar()
   rate_label = Label(master=final_window,text="Send your rate!",bg="#f79102",font=("Arial",16))
   five_rb = Radiobutton(master=final_window,text="*****",variable=alaki_var,value="*****",bg="#0fbf4a",font=("Arial",16))
   four_rb = Radiobutton(master=final_window,text="****",variable=alaki_var,value="****",bg="#0fbf4a",font=("Arial",16))
   three_rb = Radiobutton(master=final_window,text="***",variable=alaki_var,value="***",bg="#0fbf4a",font=("Arial",16))
   two_rb = Radiobutton(master=final_window,text="**",variable=alaki_var,value="**",bg="#0fbf4a",font=("Arial",16))
   one_rb = Radiobutton(master=final_window,text="*",variable=alaki_var,value="*",bg="#0fbf4a",font=("Arial",16))
   send_button = Button(master=final_window,text="Send",bg="#f79102",font=("Arial",16),command=lambda:send())
    
   rate_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
   five_rb.grid(row=1 ,column=0 ,sticky="nsew",padx=10,pady=10)
   four_rb.grid(row=2 ,column=0 ,sticky="nsew",padx=10,pady=10)
   three_rb.grid(row=3 ,column=0 ,sticky="nsew",padx=10,pady=10)
   two_rb.grid(row=4 ,column=0 ,sticky="nsew",padx=10,pady=10) 
   one_rb.grid(row=5 ,column=0 ,sticky="nsew",padx=10,pady=10) 
   send_button.grid(row=6 ,column=0 ,sticky="nsew",padx=10,pady=10)
   
   final_window.mainloop()

def photo():
   window.iconify()
   country_get = country_cb2.get()
   photo_window = Toplevel()
   if country_get == "Argentina":
      photo = ImageTk.PhotoImage(Image.open("peso.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Australia":
      photo = ImageTk.PhotoImage(Image.open("Australian_dollar.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Azerbaijan":
      photo = ImageTk.PhotoImage(Image.open("Manat.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Brazil":
      photo = ImageTk.PhotoImage(Image.open("real.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Canada":
       photo = ImageTk.PhotoImage(Image.open("Canada_dollar.png"))
       real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "China":
      photo = ImageTk.PhotoImage(Image.open("yuan.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "USA":
      photo = ImageTk.PhotoImage(Image.open("dollar.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Russia":
      photo = ImageTk.PhotoImage(Image.open("Ruble.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Bahrain":
      photo = ImageTk.PhotoImage(Image.open("bahrain-currency.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Denmark":
      photo = ImageTk.PhotoImage(Image.open("Danish_Krone.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Egypt":
      photo = ImageTk.PhotoImage(Image.open("Egyptian_pound.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Finland":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "France":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Georgia":
       photo = ImageTk.PhotoImage(Image.open("Lari.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "India":
      photo = ImageTk.PhotoImage(Image.open("Indian_Rupee.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Iraq":
       photo = ImageTk.PhotoImage(Image.open("Iraqi_Dinar.jpg"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "Japan":
      photo = ImageTk.PhotoImage(Image.open("Yen.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Kuwait":
      photo = ImageTk.PhotoImage(Image.open("Kuwaiti.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Mexico":
      photo = ImageTk.PhotoImage(Image.open("Mexican_peso.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Oman":
      photo = ImageTk.PhotoImage(Image.open("Omani_rial.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Turkey":
      photo = ImageTk.PhotoImage(Image.open("Turkish_lira.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
def photo2():
   window.iconify()
   country_get = country_cb2.get()
   photo_window = Toplevel()
   if country_get == "Argentina":
      photo = ImageTk.PhotoImage(Image.open("peso.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Australia":
      photo = ImageTk.PhotoImage(Image.open("Australian_dollar.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Azerbaijan":
      photo = ImageTk.PhotoImage(Image.open("Manat.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Brazil":
      photo = ImageTk.PhotoImage(Image.open("real.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Canada":
       photo = ImageTk.PhotoImage(Image.open("Canada_dollar.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "China":
      photo = ImageTk.PhotoImage(Image.open("yuan.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "USA":
      photo = ImageTk.PhotoImage(Image.open("dollar.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Russia":
      photo = ImageTk.PhotoImage(Image.open("Ruble.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Bahrain":
      photo = ImageTk.PhotoImage(Image.open("bahrain-currency.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Denmark":
      photo = ImageTk.PhotoImage(Image.open("Danish_Krone.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Egypt":
      photo = ImageTk.PhotoImage(Image.open("Egyptian_pound.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Finland":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "France":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Georgia":
       photo = ImageTk.PhotoImage(Image.open("Lari.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "India":
      photo = ImageTk.PhotoImage(Image.open("Indian_Rupee.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Iraq":
       photo = ImageTk.PhotoImage(Image.open("Iraqi_Dinar.jpg"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "Japan":
      photo = ImageTk.PhotoImage(Image.open("Yen.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Kuwait":
      photo = ImageTk.PhotoImage(Image.open("Kuwaiti.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Mexico":
      photo = ImageTk.PhotoImage(Image.open("Mexican_peso.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Oman":
      photo = ImageTk.PhotoImage(Image.open("Omani_rial.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Turkey":
      photo = ImageTk.PhotoImage(Image.open("Turkish_lira.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = Button(master=photo_window,text="Opinion",cnf=orange_cnf,command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
def saveinfo(btn):
    global final_window,Argentina_money, Australia_money,Azerbaijan_money,Brazil_money,Canada_money,China_money,usa_money,Russia_money,Bahrain_money,Denmark_money,Egypt_money,Finland_money,France_money,Georgia_money,India_money,Iraq_money
    global Japan_money,Kuwai_money,Mexico_money,Oman_money,Turkey_money
    Argentina_money = 0 
    Australia_money = 0
    Azerbaijan_money = 0
    Brazil_money = 0
    Canada_money = 0
    China_money = 0
    usa_money = 0
    Russia_money = 0
    Bahrain_money = 0
    Denmark_money = 0
    Egypt_money = 0
    Finland_money = 0
    France_money = 0
    Georgia_money = 0
    India_money = 0
    Iraq_money = 0
    Japan_money = 0
    Kuwai_money = 0
    Mexico_money = 0
    Oman_money = 0
    Turkey_money = 0
    if btn == "save1":
     password1_get = int(password_Entry.get())
     password2_get = int(password_entry2.get())
     if password1_get != password2_get:
         showerror(title="Error",message="Your password is incorrect!")
     elif password1_get == password2_get:  
      showinfo(title="Save!",message="You bought!")
      money_get = int(money_entry.get()) 
      if country_get == "Argentina":
         Argentina_money = int(money_get * 200)
         price = country()
      elif country_get == "Australia":
         Australia_money = int(money_get * 38_000)
         price = country()
      elif country_get == "Azerbaijan":
         Azerbaijan_money = int(money_get * 30_000)
         price = country()
      elif country_get == "Brazil":
         Brazil_money = int(money_get * 10_500)
         price = country()
      elif country_get == "Canada":
         Canada_money = (money_get * 30_000)   
         price = country()
      elif country_get == "China":
         China_money = int(money_get * 7_000)
         price = country()
      elif country_get == "USA":
         usa_money = int(money_get * 51_000)
         price = country()
      elif country_get == "Russia":
         Russia_money = int(money_get * 650)
         price = country()
      elif country_get == "Bahrain": 
         Bahrain_money = int(money_get * 133_000)
         price = country()
      elif country_get == "Denmark":
         Denmark_money = int(money_get * 7_300)
         price = country()
      elif country_get == "Egypt":
         Egypt_money = int(money_get * 1_600)
         price = country()
      elif country_get == "Finland":
         Finland_money = (money_get * 54_000)   
         price = country()
      elif country_get == "France":
         France_money = int(money_get * 54_000)
         price = country()
      elif country_get == "Georgia":
         Georgia_money = int(money_get * 19_200)
         price = country()
      elif country_get == "India":
         India_money = int(money_get * 600)
         price = country()
      elif country_get == "Iraq":
         Iraq_money = int(money_get * 38)
         price = country()
      elif country_get == "Japan":
         Japan_money = int(money_get * 340)
         price = country()
      elif country_get == "Kuwait":
         Kuwai_money = int(money_get * 160_000)
         price = country()
      elif country_get == "Mexico":
         Mexico_money = (money_get * 2_900)   
         price = country()
      elif country_get == "Oman":
         Oman_money = int(money_get * 129_000)
         price = country()
      elif country_get == "Turkey":
         Turkey_money = int(money_get * 1_900)
         price = country()
      
      image = photo()
      
    elif btn == "save2":
      password1_get = int(password_Entry.get())
      password2_get = int(password_entry3.get())
      if password1_get != password2_get:
           showerror(title="Error",message="Your password is incorrect!")
      elif password1_get == password2_get:  
        showinfo(title="Save!",message="You bought!")
        money_get = int(money_entry.get()) 
      if country_get == "Argentina":
           Argentina_money = int(money_get * 200)
           price = country()
      elif country_get == "Australia":
         Australia_money = int(money_get * 38_000)
         price = country()
      elif country_get == "Azerbaijan":
         Azerbaijan_money = int(money_get * 30_000)
         price = country()
      elif country_get == "Brazil":
         Brazil_money = int(money_get * 10_500)
         price = country()
      elif country_get == "Canada":
         Canada_money = (money_get * 30_000)   
         price = country()
      elif country_get == "China":
         China_money = int(money_get * 7_000)
         price = country()
      elif country_get == "USA":
         usa_money = int(money_get * 51_000)
         price = country()
      elif country_get == "Russia":
         Russia_money = int(money_get * 650)
         price = country()
      elif country_get == "Bahrain": 
         Bahrain_money = int(money_get * 133_000)
         price = country()
      elif country_get == "Denmark":
         Denmark_money = int(money_get * 7_300)
         price = country()
      elif country_get == "Egypt":
         Egypt_money = int(money_get * 1_600)
         price = country()
      elif country_get == "Finland":
         Finland_money = (money_get * 54_000)   
         price = country()
      elif country_get == "France":
         France_money = int(money_get * 54_000)
         price = country()
      elif country_get == "Georgia":
         Georgia_money = int(money_get * 19_200)
         price = country()
      elif country_get == "India":
         India_money = int(money_get * 600)
         price = country()
      elif country_get == "Iraq":
         Iraq_money = int(money_get * 38)
         price = country()
      elif country_get == "Japan":
         Japan_money = int(money_get * 340)
         price = country()
      elif country_get == "Kuwait":
         Kuwai_money = int(money_get * 160_000)
         price = country()
      elif country_get == "Mexico":
         Mexico_money = (money_get * 2_900)   
         price = country()
      elif country_get == "Oman":
         Oman_money = int(money_get * 129_000)
         price = country()
      elif country_get == "Turkey":
         Turkey_money = int(money_get * 1_900)
         price = country()
         
      image2 = photo2()
        
    elif btn == "exit":
        root.destroy()

def buycurrency(btn):
    global country_cb,second_label_ftame,money_entry,window,password_entry2,password_entry3,country_cb2
    if btn == "one":
      password1_get = int(password_Entry.get())
      password2_get = int(password_entry.get())
      if password1_get != password2_get:
         showerror(title="Error",message="Your password is incorrect!")  
      elif password1_get == password2_get: 
        
        rate.iconify()
        window = Toplevel()
        window.title("Chavosh_Exchange")
        window["bg"] = "black" 
        time = strftime("%H:%M")
        Hi_text = (f"Currency price today,July 4 at {time}")
        Hi_label = Label(master=window,text=Hi_text,bg="#f79102",fg="#fafaf5",font=("Arial",18))
  
        first_label_frame = LabelFrame(master=window,text="Chavosh_Exchange",font=("Arial",7), bg="#0f0f0e",fg="#fafaf5")
        password_label2 = Label(master=first_label_frame,text="Password: ",cnf=black_cnf)
        country_label = Label(master=first_label_frame,text="Country: ",cnf=black_cnf)
        currency_label = Label(master=first_label_frame,text="Currency: ",cnf=black_cnf)
        money_label = Label(master=first_label_frame,text="How much: ",cnf=black_cnf)
        guestion_label = Label(master=first_label_frame,text="Did you buy from us: ",cnf=black_cnf)
    
        second_label_ftame = LabelFrame(master=window,text="Info",bg="#0f0f0e",fg="#fafaf5")
        password_entry2 = Entry(master=second_label_ftame,cnf=orange_cnf)
        country_cb2 = Combobox(master=second_label_ftame,values=country_list,font=("Arial",16))
        currency_cb = Combobox(master=second_label_ftame,font=("Arial",16))
        money_entry = Entry(master=second_label_ftame,cnf=orange_cnf)
        guestion_sp = Spinbox(master=second_label_ftame,wrap=True,values=question_list,cnf=orange_cnf)
    
        third_label_frame = LabelFrame(master=window,text="Save Info",bg="#0f0f0e",fg="#fafaf5")
        refresh_btn = Button(master=third_label_frame,text="Refresh",cnf=orange_cnf,command=lambda:refresh())
        save_btn = Button(master=third_label_frame,text="Save",cnf=orange_cnf,command=lambda:saveinfo("save1"))
        exit_btn = Button(master=third_label_frame,text="Exit",cnf=orange_cnf,command=lambda:saveinfo("exit"))
        
        Hi_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
        
        first_label_frame.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
        second_label_ftame.grid(row=1,column=1,sticky="nsew",padx=10,pady=10)
        third_label_frame.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
        third_label_frame.columnconfigure(0,weight=2)
        third_label_frame.columnconfigure(1,weight=2)
    
        password_label2.pack(anchor="w",padx=10,pady=10)
        country_label.pack(anchor="w",padx=10,pady=10)
        currency_label.pack(anchor="w",padx=10,pady=10)
        money_label.pack(anchor="w",padx=10,pady=10)
        guestion_label.pack(anchor="w",padx=10,pady=10)
        
        password_entry2.grid(row=0 , column=0 ,padx=10,pady=10,sticky="nsew")
        country_cb2.grid(row=1 , column=0 ,padx=10,pady=10,sticky="nsew") 
        currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")
        money_entry.grid(row=3 , column=0 ,padx=10,pady=10,sticky="nsew")
        guestion_sp.grid(row=4 , column=0 ,padx=10,pady=10,sticky="nsew")
        
        refresh_btn.grid(row=0 , column=0,columnspan=2,sticky="nsew")
        save_btn.grid(row=1 , column=1 ,sticky="nsew")
        exit_btn.grid(row=1 , column=0 ,sticky="nsew")
    
        window.mainloop()

    elif btn == "two":
       second_page.iconify()
       window = Toplevel()
       window.title("Chavosh_Exchange")
       window["bg"] = "black" 
       time = strftime("%H:%M")
       Hi_text = (f"Currency price today,July 4 at {time}")
       Hi_label = Label(master=window,text=Hi_text,bg="#f79102",fg="#fafaf5",font=("Arial",18))
 
       first_label_frame = LabelFrame(master=window,text="Chavosh_Exchange",font=("Arial",7), bg="#0f0f0e",fg="#fafaf5")
       password_label3 = Label(master=first_label_frame,text="Password: ",cnf=black_cnf)
       country_label = Label(master=first_label_frame,text="Country: ",cnf=black_cnf)
       currency_label = Label(master=first_label_frame,text="Currency: ",cnf=black_cnf)
       money_label = Label(master=first_label_frame,text="How much: ",cnf=black_cnf)
       guestion_label = Label(master=first_label_frame,text="Did you buy from us: ",cnf=black_cnf)
    
       second_label_ftame = LabelFrame(master=window,text="Info",bg="#0f0f0e",fg="#fafaf5")
       password_entry3 = Entry(master=second_label_ftame,cnf=orange_cnf)
       country_cb2 = Combobox(master=second_label_ftame,values=country_list,font=("Arial",16))
       currency_cb = Combobox(master=second_label_ftame,font=("Arial",16))
       money_entry = Entry(master=second_label_ftame,cnf=orange_cnf)
       guestion_sp = Spinbox(master=second_label_ftame,wrap=True,values=question_list,cnf=orange_cnf)
    
       third_label_frame = LabelFrame(master=window,text="Save Info",bg="#0f0f0e",fg="#fafaf5")
       refresh_btn = Button(master=third_label_frame,text="Refresh",cnf=orange_cnf,command=lambda:refresh())
       save_btn = Button(master=third_label_frame,text="Save",cnf=orange_cnf,command=lambda:saveinfo("save2"))
       exit_btn = Button(master=third_label_frame,text="Exit",cnf=orange_cnf,command=lambda:saveinfo("exit"))
       
       Hi_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
       
       first_label_frame.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
       second_label_ftame.grid(row=1,column=1,sticky="nsew",padx=10,pady=10)
       third_label_frame.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
       third_label_frame.columnconfigure(0,weight=2)
       third_label_frame.columnconfigure(1,weight=2)
    
       password_label3.pack(anchor="w",padx=10,pady=10)
       country_label.pack(anchor="w",padx=10,pady=10)
       currency_label.pack(anchor="w",padx=10,pady=10)
       money_label.pack(anchor="w",padx=10,pady=10)
       guestion_label.pack(anchor="w",padx=10,pady=10)
       
       password_entry3.grid(row=0 , column=0 ,padx=10,pady=10,sticky="nsew")
       country_cb2.grid(row=1 , column=0 ,padx=10,pady=10,sticky="nsew") 
       currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")
       money_entry.grid(row=3 , column=0 ,padx=10,pady=10,sticky="nsew")
       guestion_sp.grid(row=4 , column=0 ,padx=10,pady=10,sticky="nsew")
       
       refresh_btn.grid(row=0 , column=0,columnspan=2,sticky="nsew")
       save_btn.grid(row=1 , column=1 ,sticky="nsew")
       exit_btn.grid(row=1 , column=0 ,sticky="nsew")
    
       window.mainloop()

def rate():
   global country_cb1 ,second_label_ftame_one,price_label1,currency_cb,rate,password_entry
   second_page.iconify()
   rate = Toplevel()
   rate.title("Chavosh_Exchange")
   rate.config(background="#0f0f0e")
   time = strftime("%H:%M")
   Hi_text = (f"Currency price today,July 4 at {time}")
   Hi_label = Label(master=rate,text=Hi_text,bg="#f79102",fg="#fafaf5",font=("Arial",18))

   first_label_frame = LabelFrame(master=rate,text="Chavosh_Exchange",font=("Arial",7), bg="#0f0f0e",fg="#fafaf5")
   password_label1 = Label(master=first_label_frame,text="Password: ",cnf=black_cnf)
   country_label = Label(master=first_label_frame,text="Country: ",cnf=black_cnf)
   currency_label = Label(master=first_label_frame,text="Currency: ",cnf=black_cnf)
   price_label = Label(master=first_label_frame,text="Price: ",cnf=black_cnf)
   guestion_label = Label(master=first_label_frame,text="Did you buy from us: ",cnf=black_cnf)
   
   second_label_ftame_one = LabelFrame(master=rate,text="Info",font=("Arial",7), bg="#0f0f0e",fg="#fafaf5")
   password_entry = Entry(master=second_label_ftame_one,cnf=orange_cnf)
   country_cb1 = Combobox(master=second_label_ftame_one,values=country_list,font=("Arial",16))
   currency_cb = Label(master=second_label_ftame_one,cnf=orange_cnf)
   price_label1 = Label(master=second_label_ftame_one,cnf=orange_cnf)
   guestion_sp = Spinbox(master=second_label_ftame_one,wrap=True,values=question_list,cnf=orange_cnf)
   
   third_label_frame = LabelFrame(master=rate,text="Saving",font=("Arial",7), bg="#0f0f0e",fg="#fafaf5")
   refresh_btn = Button(master=third_label_frame,text="Refresh",cnf=orange_cnf,command=lambda:refresh2())
   exit_btn = Button(master=third_label_frame,text="Exit",cnf=orange_cnf,command=lambda:saveinfo("exit"))
   buy_btn = Button(master=third_label_frame,text="Buy Currency",cnf=orange_cnf,command=lambda:buycurrency("one"))

   Hi_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
   
   first_label_frame.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
   second_label_ftame_one.grid(row=1 ,column=1 ,sticky="nsew",padx=10,pady=10)
   third_label_frame.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
   third_label_frame.columnconfigure(0,weight=2)
   third_label_frame.columnconfigure(1,weight=2)
   
   password_label1.pack(anchor="w",padx=10,pady=10)  
   country_label.pack(anchor="w",padx=10,pady=10)
   currency_label.pack(anchor="w",padx=10,pady=10)
   price_label.pack(anchor="w",padx=10,pady=10)  
   guestion_label.pack(anchor="w",padx=10,pady=10)

   password_entry.grid(row=0 ,column=0 ,sticky="nsew",padx=10,pady=10) 
   country_cb1.grid(row=1 ,column=0 ,sticky="nsew",padx=10,pady=10)
   currency_cb.grid(row=2 ,column=0 ,sticky="nsew",padx=10,pady=10)
   price_label1.grid(row=3 ,column=0 ,sticky="nsew",padx=10,pady=10)
   guestion_sp.grid(row=4 ,column=0 ,sticky="nsew",padx=10,pady=10)

   refresh_btn.grid(row=0 ,column=0 ,columnspan=2,sticky="nsew")
   exit_btn.grid(row=1 ,column=0 ,sticky="nsew")
   buy_btn.grid(row=1 ,column=1 ,sticky="nsew")

   rate.mainloop 

def secondpage():
   global second_page
   code_get = int(code_Entry.get())
   if code_file != code_get :
      showerror(title="Error",message="The code is incorrect!")  
   elif code_file == code_get:
      showinfo(title="Save!",message="Thanks!❤️")
      root.iconify()
      second_page = Toplevel()
      second_page ["bg"] = "black" 
      username_get = username_Entry.get()
      Hi_text = (f"Hi {username_get}! Choose one of them!")
      Hi_label = Label(master=second_page,text=Hi_text,bg="#0bd934",fg="#fafaf5",font=("Arial",18))
      price_button = Button(master=second_page,text="Exchange rate",cnf=orange_cnf,command=lambda:rate())
      buy_button = Button(master=second_page,text="Buy Currency",cnf=orange_cnf,command=lambda:buycurrency("two"))
      
      Hi_label.grid(row=0 ,column=0 ,sticky="nsew",padx=10,pady=10)
      price_button.grid(row=1 ,column=0 ,sticky="nsew",padx=10,pady=10)
      buy_button .grid(row=2 ,column=0 ,sticky="nsew",padx=10,pady=10)
      second_page.mainloop()

def code():
   global code_file 
   code_file = randint(1000,10000)
   codetime = strftime("%H:%M")
   recipt = open("code.txt","a")
   recipt.write(f"\n")
   recipt.write(30*".__.")
   recipt.write(f"\nTime: {codetime}")
   recipt.write(f"\nYour code: {code_file}")
   recipt.close()

def show(): 
    password_Entry.config(show="",bg="#f79102",fg="#fafaf5",font=("Arial",14))

welcome_label = Label(master=root,text="Welcome to Chavosh_Exchange!",bg="#f79102",fg="#fafaf5",font=("Arial",16))
username_label = Label(master=root,text="Username: ",cnf=black_cnf,font=("Arial",14))
username_Entry = Entry(master=root,bg="#f79102",fg="#fafaf5",font=("Arial",14))

password_label = Label(master=root,cnf=black_cnf,text="Password: ",font=("Arial",14))
password_Entry = Entry(master=root,bg="#f79102",fg="#fafaf5",show="*",font=("Arial",14))

code_label = Label(master=root,cnf=black_cnf,text="Code: ",font=("Arial",14))
code_Entry = Entry(master=root,bg="#f79102",fg="#fafaf5",font=("Arial",14))

verify_label = Label(master=root,text="Verify: ",cnf=black_cnf,font=("Arial",14))
verify_check = Checkbutton(master=root,text="I am not robot!",fg="black",bg="#1459c7",font=("Arial",14))

next_button = Button(master=root,text="Next",bg="#f79102",fg="#fafaf5",font=("Arial",16),command=lambda:secondpage())
code_button = Button(master=root,text="Code",cnf=orange_cnf,command=lambda:code())
show_btn = Button(master=root,text="Show",cnf=orange_cnf,command=lambda:show())

welcome_label.grid(row=0 ,columnspan=2,column=0,sticky="nsew")
username_label.grid(row=1 ,column=0,sticky="nsew")

username_Entry.grid(row=1 ,column=1,pady=10,padx=10,sticky="nsew")
password_label.grid(row=2 ,column=0,sticky="nsew")
password_Entry.grid(row=2 ,column=1,pady=10,padx=10,sticky="nsew")

code_label.grid(row=3 ,column=0,sticky="nsew")
code_Entry.grid(row=3 ,column=1,pady=10,padx=10,sticky="nsew")

verify_label.grid(row=4 ,column=0,pady=10,padx=10,sticky="nsew")
verify_check.grid(row=4,column=1)

show_btn.grid(row=5,column=0,sticky="nsew")
code_button.grid(row=5,column=1,sticky="nsew")
next_button.grid(row=6,column=0,columnspan=2,sticky="nsew")

root.mainloop()
