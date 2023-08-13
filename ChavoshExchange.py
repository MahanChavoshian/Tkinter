# Chavosh_Exchange : You can buy currency.
# Designed and created by Mahan Chavoshian!
#Pip install customtkinter!

from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,CTkToplevel,CTkComboBox,CTkOptionMenu,CTkCheckBox,CTkRadioButton,CTkTabview,StringVar
from tkinter import Label,LabelFrame
from tkinter.messagebox import showinfo,showerror
from time import strftime
from random import randint
from PIL import Image,ImageTk
from turtle import write,hideturtle,done
from os import system
from platform import system as sys

def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")

terminal_cleaner()

root = CTk()
root.title("Chavosh_Exchange 3.0")
root.configure(fg_color="#0f0f0e")



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
    "font" : ("Arial",20)
}

orange_cnf = {
    "bg" : "#f79102",
    "fg" : "#fafaf5",
    "font" : ("Arial",20)
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
    currency_cb.configure(text=f"{currency}")
    currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")
    price = price_dict[country_get] 
    price_label1.configure(text=f"{price}Toman")
    price_label1.grid(row=3 , column=0 ,padx=10,pady=10,sticky="nsew")

def refresh():
    global country_get
    country_get = country_cb2.get()
    currency = country_dict[country_get]
    currency_cb = CTkLabel(master=second_label_ftame,text=currency,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
    currency_cb.grid(row=2 , column=0 ,padx=10,pady=10,sticky="nsew")

def send():
  showerror(title="Follow!",message="Follow me in GitHub!\nDesigned by: Mahan Chavoshian")
  showinfo(title="Send!",message="Your comment has been recorded!")
  final_window.iconify()
  username_turtle = username_Entry.get()
  hideturtle()
  write(f"Thanks {username_turtle}!❤️\nChavosh_Exchange", align="center", font=("Cooper Black", 25, "italic"))
  done()

def opinion():
   global final_window
   photo_window.iconify()
   final_window = CTkToplevel()
   final_window.title("Chavosh_Exchange 3.0")
   alaki_var = StringVar()
   rate_label = CTkLabel(master=final_window,text="Send your rate!",fg_color="darkblue",font=("Arial",20))
   five_rb = CTkRadioButton(master=final_window,text="*****",variable=alaki_var,font=("Arial",20))
   four_rb = CTkRadioButton(master=final_window,text="****",variable=alaki_var,font=("Arial",20))
   three_rb = CTkRadioButton(master=final_window,text="***",variable=alaki_var,font=("Arial",20))
   two_rb = CTkRadioButton(master=final_window,text="**",variable=alaki_var,font=("Arial",20))
   one_rb = CTkRadioButton(master=final_window,text="*",variable=alaki_var,font=("Arial",20))
   send_button = CTkButton(master=final_window,text="Send",fg_color="darkblue",font=("Arial",20),command=lambda:send())
    
   rate_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=10,pady=10)
   five_rb.grid(row=1 ,column=0 ,sticky="nsew",padx=10,pady=10)
   four_rb.grid(row=2 ,column=0 ,sticky="nsew",padx=10,pady=10)
   three_rb.grid(row=3 ,column=0 ,sticky="nsew",padx=10,pady=10)
   two_rb.grid(row=4 ,column=0 ,sticky="nsew",padx=10,pady=10) 
   one_rb.grid(row=5 ,column=0 ,sticky="nsew",padx=10,pady=10) 
   send_button.grid(row=6 ,column=0 ,sticky="nsew",padx=10,pady=10)
   
   final_window.mainloop()

def photo():
   global photo_window
   window.iconify()
   country_get = country_cb2.get()
   photo_window = CTkToplevel()
   if country_get == "Argentina":
      photo = ImageTk.PhotoImage(Image.open("peso.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Australia":
      photo = ImageTk.PhotoImage(Image.open("Australian_dollar.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Azerbaijan":
      photo = ImageTk.PhotoImage(Image.open("Manat.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Brazil":
      photo = ImageTk.PhotoImage(Image.open("real.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Canada":
       photo = ImageTk.PhotoImage(Image.open("Canada_dollar.png"))
       real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "China":
      photo = ImageTk.PhotoImage(Image.open("yuan.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "USA":
      photo = ImageTk.PhotoImage(Image.open("dollar.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Russia":
      photo = ImageTk.PhotoImage(Image.open("Ruble.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Bahrain":
      photo = ImageTk.PhotoImage(Image.open("bahrain-currency.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Denmark":
      photo = ImageTk.PhotoImage(Image.open("Danish_Krone.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Egypt":
      photo = ImageTk.PhotoImage(Image.open("Egyptian_pound.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Finland":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "France":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Georgia":
       photo = ImageTk.PhotoImage(Image.open("Lari.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "India":
      photo = ImageTk.PhotoImage(Image.open("Indian_Rupee.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Iraq":
       photo = ImageTk.PhotoImage(Image.open("Iraqi_Dinar.jpg"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "Japan":
      photo = ImageTk.PhotoImage(Image.open("Yen.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Kuwait":
      photo = ImageTk.PhotoImage(Image.open("Kuwaiti.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Mexico":
      photo = ImageTk.PhotoImage(Image.open("Mexican_peso.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Oman":
      photo = ImageTk.PhotoImage(Image.open("Omani_rial.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Turkey":
      photo = ImageTk.PhotoImage(Image.open("Turkish_lira.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
def photo2():
   global photo_window
   window.iconify()
   country_get = country_cb2.get()
   photo_window = CTkToplevel()
   if country_get == "Argentina":
      photo = ImageTk.PhotoImage(Image.open("peso.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Australia":
      photo = ImageTk.PhotoImage(Image.open("Australian_dollar.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Azerbaijan":
      photo = ImageTk.PhotoImage(Image.open("Manat.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Brazil":
      photo = ImageTk.PhotoImage(Image.open("real.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Canada":
       photo = ImageTk.PhotoImage(Image.open("Canada_dollar.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "China":
      photo = ImageTk.PhotoImage(Image.open("yuan.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "USA":
      photo = ImageTk.PhotoImage(Image.open("dollar.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Russia":
      photo = ImageTk.PhotoImage(Image.open("Ruble.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Bahrain":
      photo = ImageTk.PhotoImage(Image.open("bahrain-currency.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Denmark":
      photo = ImageTk.PhotoImage(Image.open("Danish_Krone.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Egypt":
      photo = ImageTk.PhotoImage(Image.open("Egyptian_pound.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Finland":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=200,height=200,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "France":
      photo = ImageTk.PhotoImage(Image.open("Euro.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Georgia":
       photo = ImageTk.PhotoImage(Image.open("Lari.png"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "India":
      photo = ImageTk.PhotoImage(Image.open("Indian_Rupee.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Iraq":
       photo = ImageTk.PhotoImage(Image.open("Iraqi_Dinar.jpg"))
       real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
       Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
               
       real_photo1.grid(row=0 ,column=0)
       Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
       photo_window.mainloop()
   elif country_get == "Japan":
      photo = ImageTk.PhotoImage(Image.open("Yen.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Kuwait":
      photo = ImageTk.PhotoImage(Image.open("Kuwaiti.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Mexico":
      photo = ImageTk.PhotoImage(Image.open("Mexican_peso.jpg"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Oman":
      photo = ImageTk.PhotoImage(Image.open("Omani_rial.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
      real_photo1.grid(row=0 ,column=0)
      Opinion_btn.grid(row=1 ,column=0,sticky="nsew")
      photo_window.mainloop()
   elif country_get == "Turkey":
      photo = ImageTk.PhotoImage(Image.open("Turkish_lira.png"))
      real_photo1 = Label(master=photo_window,width=300,height=300,image=photo,relief="raised",border=30)
      Opinion_btn = CTkButton(master=photo_window,text="Opinion",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:opinion())
              
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

def cryptoprice():
   second_page.iconify()
   crypto_page = CTkToplevel()
   first_labelframe_crypto = LabelFrame(master=crypto_page,) 

   crypto_page.mainloop()

def buycurrency(btn):
    global country_cb,second_label_ftame,money_entry,window,password_entry2,password_entry3,country_cb2
    if btn == "one":
      password1_get = int(password_Entry.get())
      password2_get = int(password_entry.get())
      if password1_get != password2_get:
         showerror(title="Error",message="Your password is incorrect!")  
      elif password1_get == password2_get: 
        
        rate.iconify()
        window = CTkToplevel()
        window.title("Chavosh_Exchange 3.0")
        window.configure(fg_color="black")
        time = strftime("%H:%M") 
        date = strftime(" %a, %b %d")
        Hi_text = (f"Currency price today : {date} at {time}")
        Hi_label = CTkLabel(master=window,text=Hi_text,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
  
        first_label_frame = LabelFrame(master=window,text="Chavosh_Exchange",font=("Arial",12), bg="#0f0f0e",fg="#fafaf5")
        password_label2 = CTkLabel(master=first_label_frame,text="Password: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
        country_label = CTkLabel(master=first_label_frame,text="Country: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
        currency_label = CTkLabel(master=first_label_frame,text="Currency: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
        money_label = CTkLabel(master=first_label_frame,text="How much: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
        guestion_label = CTkLabel(master=first_label_frame,text="Did you buy from us: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
    
        second_label_ftame = LabelFrame(master=window,text="Info",bg="#0f0f0e",fg="#fafaf5")
        password_entry2 = CTkEntry(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
        country_cb2 = CTkComboBox(master=second_label_ftame,values=country_list,font=("Arial",20))
        currency_cb = CTkLabel(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
        money_entry = CTkEntry(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
        guestion_sp = CTkOptionMenu(master=second_label_ftame,values=question_list,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
    
        third_label_frame = LabelFrame(master=window,text="Save Info",bg="#0f0f0e",fg="#fafaf5")
        refresh_btn = CTkButton(master=third_label_frame,text="Refresh",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:refresh())
        save_btn = CTkButton(master=third_label_frame,text="Save",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:saveinfo("save1"))
        exit_btn = CTkButton(master=third_label_frame,text="Exit",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:saveinfo("exit"))
        
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
       window = CTkToplevel()
       window.title("Chavosh_Exchange 3.0")
       window.configure(fg_color="black") 
       time = strftime("%H:%M")
       date = strftime(" %a, %b %d")
       Hi_text = (f"Currency price today : {date} at {time}")
       Hi_label = CTkLabel(master=window,text=Hi_text,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
 
       first_label_frame = LabelFrame(master=window,text="Chavosh_Exchange",font=("Arial",12), bg="#0f0f0e",fg="#fafaf5")
       password_label3 = CTkLabel(master=first_label_frame,text="Password: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
       country_label = CTkLabel(master=first_label_frame,text="Country: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
       currency_label = CTkLabel(master=first_label_frame,text="Currency: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
       money_label = CTkLabel(master=first_label_frame,text="How much: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
       guestion_label = CTkLabel(master=first_label_frame,text="Did you buy from us: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
    
       second_label_ftame = LabelFrame(master=window,text="Info",bg="#0f0f0e",fg="#fafaf5")
       password_entry3 = CTkEntry(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
       country_cb2 = CTkComboBox(master=second_label_ftame,values=country_list,font=("Arial",20))
       currency_cb = CTkLabel(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
       money_entry = CTkEntry(master=second_label_ftame,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
       guestion_sp = CTkOptionMenu(master=second_label_ftame,values=question_list,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
    
       third_label_frame = LabelFrame(master=window,text="Save Info",bg="#0f0f0e",fg="#fafaf5")
       refresh_btn = CTkButton(master=third_label_frame,text="Refresh",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:refresh())
       save_btn = CTkButton(master=third_label_frame,text="Save",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:saveinfo("save2"))
       exit_btn = CTkButton(master=third_label_frame,text="Exit",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:saveinfo("exit"))
       
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
   rate = CTkToplevel()
   rate.title("Chavosh_Exchange 3.0")
   rate.configure(fg_color="#0f0f0e")
   time = strftime("%H:%M")
   date = strftime(" %a, %b %d")
   Hi_text = (f"Currency price today : {date} at {time}")
   Hi_label = CTkLabel(master=rate,text=Hi_text,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))

   first_label_frame = LabelFrame(master=rate,text="Chavosh_Exchange",font=("Arial",12), bg="#0f0f0e",fg="#fafaf5")
   password_label1 = CTkLabel(master=first_label_frame,text="Password: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
   country_label = CTkLabel(master=first_label_frame,text="Country: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
   currency_label = CTkLabel(master=first_label_frame,text="Currency: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
   price_label = CTkLabel(master=first_label_frame,text="Price: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
   guestion_label = CTkLabel(master=first_label_frame,text="Did you buy from us: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
   
   second_label_ftame_one = LabelFrame(master=rate,text="Info",font=("Arial",12), bg="#0f0f0e",fg="#fafaf5")
   password_entry = CTkEntry(master=second_label_ftame_one,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
   country_cb1 = CTkComboBox(master=second_label_ftame_one,values=country_list,font=("Arial",20))
   currency_cb = CTkLabel(master=second_label_ftame_one,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
   price_label1 = CTkLabel(master=second_label_ftame_one,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
   guestion_sp = CTkOptionMenu(master=second_label_ftame_one,values=question_list,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
   
   third_label_frame = LabelFrame(master=rate,text="Saving",font=("Arial",12), bg="#0f0f0e",fg="#fafaf5")
   refresh_btn = CTkButton(master=third_label_frame,text="Refresh",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:refresh2())
   exit_btn = CTkButton(master=third_label_frame,text="Exit",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:saveinfo("exit"))
   buy_btn = CTkButton(master=third_label_frame,text="Buy Currency",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:buycurrency("one"))

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
   elif code_file == code_get and verify_var.get() == "No":
      showinfo(title="Save!",message="Thanks!❤️")
      root.iconify()
      second_page = CTkToplevel(root)
      second_page.title("Chavosh_Exchange 3.0")
      second_page.configure(fg_color="black")
      
      username_get = username_Entry.get()
      Hi_text = (f"Hi {username_get}! Choose one of them!")
      Hi_label = CTkLabel(master=second_page,text=Hi_text,fg_color="#0bd934",text_color="#fafaf5",font=("Arial",20))
      tabview = CTkTabview(master=second_page)
      tabview.grid(row=1,column=0)
      
      tabview.add("Currency") 
      tabview.add("Cryptocurrency") 
      tabview.set("Currency") 
      price_button = CTkButton(master=tabview.tab("Currency"),text="Exchange rate",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:rate())
      buy_button = CTkButton(master=tabview.tab("Currency"),text="Buy Currency",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20),command=lambda:buycurrency("two"))
      price_crypto = CTkButton(master=tabview.tab("Cryptocurrency"),text="Cryptocurrency price",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
      buy_crypto = CTkButton(master=tabview.tab("Cryptocurrency"),text="Buy Cryptocurrency",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))

      Hi_label.grid(row=0 ,column=0 ,sticky="nsew",padx=10,pady=10)
      price_button.pack(padx=15,pady=15)
      buy_button .pack(padx=15,pady=15)
      price_crypto.pack(padx=15,pady=15)
      buy_crypto.pack(padx=15,pady=15) 
      second_page.mainloop()
   elif verify_var.get() == "Yes":
      showerror(title="Verify!",message="Are you a robot?")

def code():
   global code_file 
   code_file = randint(1000,10000)
   codetime = strftime("%H:%M")
   showinfo(title="Code",message=f"Time: {codetime}\nYour Chavosh_Exchange code: {code_file}\nDon't Share it!")
   
def show(): 
    password_Entry.configure(show="")

verify_var = StringVar()
welcome_label = CTkLabel(master=root,text="Welcome to Chavosh_Exchange!",fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))
username_label = CTkLabel(master=root,text="Username: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
username_Entry = CTkEntry(master=root,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))

password_label = CTkLabel(master=root,fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20),text="Password: ")
password_Entry = CTkEntry(master=root,fg_color="#f79102",text_color="#fafaf5",show="*",font=("Arial",20))

code_label = CTkLabel(master=root,fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20),text="Code: ")
code_Entry = CTkEntry(master=root,fg_color="#f79102",text_color="#fafaf5",font=("Arial",20))

verify_label = CTkLabel(master=root,text="Verify: ",fg_color="#0f0f0e",text_color="#fafaf5",font=("Arial",20))
verify_check = CTkCheckBox(master=root,text="I am not robot!",fg_color="#1459c7",variable=verify_var,onvalue="No",offvalue="Yes",font=("Arial",18))

next_button = CTkButton(master=root,text="Next",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:secondpage())
code_button = CTkButton(master=root,text="Code",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:code())
show_btn = CTkButton(master=root,text="Show",fg_color="#f79102",text_color="#fafaf5",font=("Arial",18),command=lambda:show())

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
