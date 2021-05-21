from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showerror 
from PIL import ImageTk,Image,UnidentifiedImageError
from os import listdir

# ! Global Valiables
index = 0
imgList=[]
length=0

##############################  Functions  ##############################
# * Image Resizer
def resizeImg(img):
    w, h = img.size
    
    if w > 993 and h <= 611:
        img = img.resize((993, h), Image.BICUBIC)
    elif h > 611 and w <= 993:
        img = img.resize((w, 611), Image.BICUBIC)
    elif w > 993 and h > 611:
        img = img.resize((993, 611), Image.BICUBIC)
    
    return img

# * function for Filedialog 
def browse():
    root.option_add('*foreground', '#00A6BD')
    fileName = fd.askopenfilename(master=root, initialdir = "./",
                                  title = "Select file",
                                  filetypes = (("JPEG files","*.jpeg"),
                                               ("JPG files","*.jpg"),
                                               ("PNG files","*.png"),
                                               ("All files","*.*")))
    searchBox.delete(0,END)
    searchBox.insert(0,fileName)

# * Function for open Image
def openImg():
    global index, imgList, length       # ! Global Valiables
    counter = 0
    imgList=[]
    # setected Image Loading 
    path = searchBox.get()
    try:
        curImg = Image.open(path)
    except AttributeError:
        showerror("Error", "Please Enter the Image Address.")
    except UnidentifiedImageError:
        showerror("Error", "Selected file is not an Image.")
    except FileNotFoundError:
        showerror("Error", f"No such file or directory: '{path}'")
    else:
        curImg = resizeImg(curImg)
        curImg = ImageTk.PhotoImage(curImg)
        # Displaying
        imgScn.config(image=curImg, width =993, height = 611)
        imgScn.image=curImg
        # Loading all Images from the folder
        lst = path.split('/')
        curImgName = lst[-1]
        path = '/' + '/'.join(lst[1:-1])
        for name in listdir(path):
            try:
                img = Image.open(path+'/'+name)
            except Exception:
                continue
            else:
                if curImgName == name:
                    index = counter
                img = resizeImg(img)
                img = ImageTk.PhotoImage(img)
                imgList.append(img)
                counter += 1
        
        length = len(imgList)
        # update Status Bar
        statusBar.config(text=f'{index+1} of {length} images',width=101,anchor='e')
        # Buttons settings
        if index == 0:
            forwardBT['state'] = NORMAL
            backwardBT['state'] = DISABLED
        elif index == length - 1:
            backwardBT['state'] = NORMAL
            forwardBT['state'] = DISABLED
        else:
            forwardBT['state'] = NORMAL
            backwardBT['state'] = NORMAL
        
# * Function to move forward
def forward():
    global index                        # ! Global Valiables
    index += 1
    # Displaying
    imgScn.config(image=imgList[index], width =993, height = 611)
    imgScn.image=imgList[index]
    # Button checking
    if index == length - 1:
        forwardBT['state'] = DISABLED
    elif index == 1:
        backwardBT['state'] = NORMAL
    # update Status Bar
    statusBar.config(text=f'{index+1} of {length} images',width=101,anchor='e')

# * Function to move backward
def backward():
    global index                        # ! Global Valiables
    index -= 1
    # Displaying
    imgScn.config(image=imgList[index], width =993, height = 611)
    imgScn.image=imgList[index]
    # Button checking
    if index == 0:
        backwardBT['state'] = DISABLED
    elif index == length - 2:
        forwardBT['state'] = NORMAL
    # Update Status Bar
    statusBar.config(text=f'{index+1} of {length} images',width=101,anchor='e')
    

##############################  Root  ##############################
root = Tk()
root.title('Image Viewer')
root.geometry('1000x700')
##############################  Search Bar  ##############################
searchBar = Label(root)
searchBar.pack(anchor='center', fill=BOTH)

# * Entry Box
searchBox = Entry(searchBar)
searchBox.pack(anchor='center',fill=BOTH, side=LEFT ,expand=1)

# * Buttons for Search Bar
# browse Button
Button(searchBar,text='Browse File', width=23, command=browse).pack(anchor='center', side=LEFT, fill=BOTH)
# open Button
Button(searchBar,text='OPEN', width=23, command=openImg).pack(anchor='center', side=RIGHT, fill=BOTH)
##############################  Image Frame  ##############################
imageFrame = LabelFrame(root)
imageFrame.pack(anchor='center',fill=BOTH,expand=1)

# * Image Screen
imgScn = Label(imageFrame,text='No Iamge is Selected',pady=300)
imgScn.pack(anchor='center',fill=BOTH)
##############################  Tarck Bar  ##############################
trackBar = LabelFrame(root)
trackBar.pack(anchor='center',fill=BOTH)

# * Buttons for Track Bar
# Backward Button
backwardBT = Button(trackBar, state=DISABLED, text='BACKWARD', width=20, command=backward)
backwardBT.pack(side=LEFT)
# Forward Button
forwardBT = Button(trackBar, state=DISABLED, text='FORWARD', width=20, command=forward)
forwardBT.pack(side=RIGHT)
##############################  Status Bar  ##############################
# statusFrame = LabelFrame(root)
# statusFrame.pack(anchor='center')
statusBar = Label(root,width=100)
statusBar.pack(anchor='e')

##############################  Main Loop  ##############################
root.mainloop()