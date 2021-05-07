from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
# This module is used to copy the translated output to clipboard
import pyperclip


# WINDOW
root = Tk()
root.geometry('1080x400')
# resizable restrics the user to change window sizes
root.resizable()
root.config(bg = '#aacf32')
root.title("Translator")


### LABELS :
# Title
Title = Label(root, text = "TRANSLATOR", font = "sans-serif",fg = 'black', bg='#aacf32',pady = 20,padx =20,width=100)
Title.pack()

# wrap = WORD will break the line after the last word that will fit

# INPUT
Label(root,text = "Enter text", font='sans-serif',fg = 'white', bg='#053b7d').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)

# OUTPUT
Label(root,text ="Translation", font = 'sans-serif',fg = 'white', bg='#053b7d').place(x=750,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)



### Combobox = drop-down list for the user to choose from
#Combobox for input
language = LANGCODES = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=30,y=60)
src_lang.set('Choose Input Language')

#Combobox for output
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=877,y=60)
dest_lang.set('Choose Output Language')



### FUNCTIONS :
# The function to translate the Input to our desired language
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

# Copy Output to clipboard
def CopyText():
    pyperclip.copy(Output_text.get(1.0, END))

# Clearing Input and Output
def ClearBoxes():
    Output_text.delete(1.0, END)
    Input_text.delete(1.0, END)



### BUTTONS :

# activebackground − Background color for the widget when the widget is active
# Translate button
trans_button = Button(root, text = 'Translate',font = 'sans-serif',pady = 5,command = Translate ,fg = 'white', bg = '#053b7d', activebackground = 'sky blue')
trans_button.place(x = 484, y= 140 )

# Copy translation to clipboard
copy_button = Button(root, text = 'Copy translation',font = 'sans-serif',pady = 5,command = CopyText ,fg = 'white', bg = '#053b7d', activebackground = 'sky blue')
copy_button.place(x = 750, y= 300 )

# Clear button
clear_button = Button(root, text = 'Clear',font = 'sans-serif',pady = 5,command = ClearBoxes ,fg = 'white', bg = '#053b7d', activebackground = 'sky blue')
clear_button.place(x = 495, y= 210 )



root.mainloop()
