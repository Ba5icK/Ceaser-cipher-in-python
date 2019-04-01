import tkinter
from tkinter import *

root=Tk()
root.geometry("600x500")
root.title("BA5ICK ENCRYPTION")
root.config(bg="Light Blue")

inp1=StringVar()
inp2=StringVar()
out1=StringVar()
out2=StringVar()

#Function to Encrypt
def encode1():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    key=3
    newmessage=''

    message=inp1.get()
    for character in message:
        if character in alphabet:
            position=alphabet.find(character)
            newposition=(position + key)%26
            newcharacter=alphabet[newposition]
            newmessage+=newcharacter
    print(newmessage)
    out1.set(newmessage)

def decode1():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    key=3
    newmessage=''

    message=inp2.get()
    for character in message:
        if character in alphabet:
            position=alphabet.find(character)
            newposition=(position - key)%26
            newcharacter=alphabet[newposition]
            newmessage+=newcharacter
    print(newmessage)
    out2.set(newmessage)

#ENCODE
label11=Label(root,text="Encode",bg="Light Blue",font=(20))
label11.pack()
label11.place(x=50,y=20)

label1=Label(root,text="Input",bg="Light Blue")
label1.pack()
label1.place(x=50,y=50)

label2=Label(root,text="Encoded",bg="Light Blue")
label2.pack()
label2.place(x=300,y=50)

button1=Button(root,text="Encode",command=encode1)
button1.pack()
button1.place(x=50,y=75)

e1=Entry(root,textvariable=inp1)
e1.pack()
e1.place(x=100,y=50)

e2=Entry(root,textvariable=out1)
e2.pack()
e2.place(x=380,y=50)

#DECODE
label21=Label(root,text="Decode",bg="Light Blue",font=(20))
label21.pack()
label21.place(x=50,y=120)

label3=Label(root,text="Input",bg="Light Blue")
label3.pack()
label3.place(x=50,y=150)

label4=Label(root,text="Decoded",bg="Light Blue")
label4.pack()
label4.place(x=300,y=150)

button2=Button(root,text="Decode",command=decode1)
button2.pack()
button2.place(x=50,y=175)

e3=Entry(root,textvariable=inp2)
e3.pack()
e3.place(x=100,y=150)

e4=Entry(root,textvariable=out2)
e4.pack()
e4.place(x=380,y=150)




root.mainloop()

