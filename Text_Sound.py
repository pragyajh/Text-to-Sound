from tkinter import*
from gtts import gTTS
from playsound import playsound
import os
window=Tk()
window.title("Text to Sound converter")
window.geometry("500x500")
window.config(bg="yellow")
def exit():
    window.destroy()
def clear():
    msg.set(" ")
m_box=Message(window,text="Enter text to be converted",fg="black",relief=RAISED,width=400,bg="red")
msg=StringVar()
e_box=Entry(window,textv=msg,width=40,borderwidth=5,relief=RAISED)
def convert():
    message = e_box.get()
    speech = gTTS(text=message, lang='en', slow=False)
    speech.save('DataFlair.mp3')
    try:
        playsound('DataFlair.mp3')
    except Exception as e:
        print("Error:", e)
b1=Button(window,text="Convert",command=convert)
b2=Button(window,text="clear",command=clear)
b3=Button(window,text="Exit",command=exit)
m_box.place(x=200,y=50)
e_box.place(x=150,y=100)
b1.place(x=150,y=150)
b2.place(x=250,y=150)
b3.place(x=350,y=150)
mainloop()