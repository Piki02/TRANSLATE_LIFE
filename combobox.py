from os import link
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  
from googletrans import Translator
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.title('Translate Life ')
root.geometry('1280x720')
root.maxsize(1280,720)
root.minsize(1280,720)


def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('Translate Life','please fill the box')
        else:
                t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')

#img = ImageTk.PhotoImage(Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/fioondo.gif'))
#panel = tk.Label(root, image = img)
#panel.pack(fill = "both", expand = "yes")

img = ImageTk.PhotoImage(Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/azul.gif'))
panel = tk.Label(root, image = img)
panel.pack(fill = "both", expand = "yes")

#img2 = ImageTk.PhotoImage(Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/blabla.gif'))
#panel2 = tk.Label(root, image = img2).place(x=485, y=0)

a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 18, textvariable = a, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal'),) 

auto_detect['values'] = (
                          'Deteccion automatica', 
                          ) 
  
auto_detect.place(x=533,y=250)
auto_detect.current(0) 

l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 18, textvariable = l, state='readonly',font=('Bahnschrift SemiCondensed',16,'normal')) 
  
def link():
        webbrowser.open("http://127.0.0.1:8080/opiniones")
def es():
        webbrowser.open("http://127.0.0.1:8080/espanol")
def en():
        webbrowser.open("http://127.0.0.1:8080/ingles")
def ru():
        webbrowser.open("http://127.0.0.1:8080/ruso")
def ja():
        webbrowser.open("http://127.0.0.1:8080/japones")
def pag():
        webbrowser.open("http://127.0.0.1:8080/home")


choose_langauge['values'] = (
                        'Seleccione Idioma', 
                        'Afrikaans',
                        'Albanian',
                        'Arabic',
                        'Armenian',
                        'Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                        'Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese',
                        'Corsican',
                        'Croatian',
                        'Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Kinyarwanda',
                        'Korean',
                        'Kurdish',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Myanmar',
                        'Nepali',
                        'Norwegian'
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots Gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Tatar',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Turkmen',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa'
                        'Yiddish',
                        'Yoruba',
                        'Zulu',
                          ) 
  
choose_langauge.place(x=533,y=350)
choose_langauge.current(0) 


t1 = Text(root,width=50,height=30,borderwidth=7,relief=RIDGE)
t1.place(x=100,y=100)

t2 = Text(root,width=50,height=30,borderwidth=7,relief=RIDGE)
t2.place(x=745,y=100)


button = Button(root,text="Traducir",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=translate)
button.place(x=275,y=600)


clear = Button(root,text="Limpiar",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=clear)
clear.place(x=580,y=600)

link = Button(root,text="Opiniones",relief=RIDGE,borderwidth=3,font=('Bahnschrift SemiCondensed',20,'normal'),cursor="hand2",command=link)
link.place(x=855,y=600)

banner = Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/banner.gif')
banner = ImageTk.PhotoImage(banner)
es = Button(root,relief=RIDGE,image=banner,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=pag)
es.place(x=280,y=5)


img1 = Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/espanol.gif')
img1 = ImageTk.PhotoImage(img1)
es = Button(root,relief=RIDGE,image=img1,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=es)
es.place(x=5,y=675)

img2 = Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/ingles.gif')
img2 = ImageTk.PhotoImage(img2)
en = Button(root,relief=RIDGE,image=img2,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=es)
en.place(x=55,y=675)

img3 = Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/japon.gif')
img3 = ImageTk.PhotoImage(img3)
ja = Button(root,relief=RIDGE,image=img3,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=es)
ja.place(x=105,y=675)

img4 = Image.open('C:/Users/Fredy Garcia/Desktop/TRADUCTOR/ruso.gif')
img4 = ImageTk.PhotoImage(img4)
ru = Button(root,relief=RIDGE,image=img4,borderwidth=0,font=('Bahnschrift SemiCondensed',10,'normal'),cursor="hand2",command=es)
ru.place(x=155,y=675)

root.mainloop()