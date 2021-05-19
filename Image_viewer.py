from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk,Image

def browse():
    root.option_add('*foreground', '#00A6BD')
    ask = fd.askopenfilename(master=root, initialdir = "./",
                              title = "Select file",
                              filetypes = (("all files","*.*"),("python files","*.py")))
    searchbar.delete(0,END)
    searchbar.insert(0,ask)

def openImg():
    img=ImageTk.PhotoImage(Image.open(searchbar.get()))
    l1.config(image=img, width =660, height = 500)
    l1.image=img


    



root = Tk()
root.geometry("673x600")

# upper frame
upperFrame = LabelFrame(root)
upperFrame.pack(anchor='center')

searchbar = Entry(upperFrame,width=63)
searchbar.grid(row=0,column=0,sticky=E)

Button(upperFrame,text='Browse File',command=browse).grid(row=0,column=1,sticky='n')

Button(upperFrame,text='OPEN',command=openImg).grid(row=0,column=2,sticky='n')


# Image frame
imageFrame = LabelFrame(root)
imageFrame.pack(anchor='center')

l1 = Label(imageFrame, text='No image is selected',padx=285,pady=254)
l1.grid()

# tarck frame
trackFrame = LabelFrame(root)
trackFrame.pack(anchor='center')

forward = Button(trackFrame,text='FORWARD',command=openImg).grid(row=0,column=0)
Label(trackFrame, padx=85).grid(row=0,column=1)
backward = Button(trackFrame,text='BACKWARD',command=openImg).grid(row=0,column=2)

root.mainloop()