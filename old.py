from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox

def on_printtext(en3):
    messagebox.showinfo("Window Title",en3 )




base = Tk()  
base.geometry("900x500")  
base.title("Movie Booking")  


img = ImageTk.PhotoImage(Image.open("F:\\t.jpg"))
  
panel = Label(base, image = img)
  
panel.pack(side = "right", fill = "both",
          )
  
lb3= Label(base, text="Seat type:", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)
lb4= Label(base, text="No of Seat", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  
  
lb5= Label(base, text="Time", width=15, font=("arial",12))  
lb5.place(x=5, y=240)  
vars = IntVar()  
Radiobutton(base, text="Moring Show", padx=15,variable=vars, value=1).place(x=180, y=240)  
Radiobutton(base, text="Evening Show", padx =10,variable=vars, value=2).place(x=280,y=240)  
Radiobutton(base, text="Night Show", padx=15, variable=vars, value=3).place(x=370,y=240)  
  
movie_name = ("The Shawshank Redemption (1994)", "2. The Godfather (1972) ", "3. The Dark Knight (2008) ", "4.The Godfather Part II (1974) ")  
cv = StringVar()  
drplist= OptionMenu(base, cv, *movie_name)  
drplist.config(width=15)  
cv.set("Enter Movie Name")  
lb2= Label(base, text="Movie Name", width=13,font=("arial",12))  
lb2.place(x=14,y=280)  
drplist.place(x=200, y=275)  
  
lb6= Label(base, text="Total Seat:", width=13,font=("arial",12))  
lb6.place(x=19, y=320)  
en6= Entry(base ,text="$")  
en6.place(x=200, y=320)  

Button(base, text="Booking", width=10 ,command = on_printtext(en3)).place(x=200,y=400)

base.mainloop()  
