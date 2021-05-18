from tkinter import *

def click(arg):
    text = display.get() + str(arg)
    display.delete(0,END)
    display.insert(0,text)

def evaluate():
    ans = eval(display.get())
    display.delete(0,END)
    display.insert(0,ans)

def clear():
    display.delete(0,END)

# * Creating the root
root = Tk()
root.title('Calculator')

# * Creating the Entry box (Display Box)
display = Entry(root,width=30)
display.grid(row=0,column=0,columnspan=4)

# * Number buttons
button = Button(root,text=7,padx=20,pady=20,command=lambda: click(7))
button.grid(row=1,column=0)

button = Button(root,text=8,padx=20,pady=20,command=lambda: click(8))
button.grid(row=1,column=1)

button = Button(root,text=9,padx=20,pady=20,command=lambda: click(9))
button.grid(row=1,column=2)

button = Button(root,text=4,padx=20,pady=20,command=lambda: click(4))
button.grid(row=2,column=0)

button = Button(root,text=5,padx=20,pady=20,command=lambda: click(5))
button.grid(row=2,column=1)

button = Button(root,text=6,padx=20,pady=20,command=lambda: click(6))
button.grid(row=2,column=2)

button = Button(root,text=1,padx=20,pady=20,command=lambda: click(1))
button.grid(row=3,column=0)

button = Button(root,text=2,padx=20,pady=20,command=lambda: click(2))
button.grid(row=3,column=1)

button = Button(root,text=3,padx=20,pady=20,command=lambda: click(3))
button.grid(row=3,column=2)

button = Button(root,text=0,padx=20,pady=20,command=lambda: click(0))
button.grid(row=4,column=1)

# * decimal button
button = Button(root,text='.',padx=21,pady=20,command=lambda: click('.'))
button.grid(row=4,column=0)

# * Math Operation buttons
# '/' operator
button = Button(root,text='/',padx=36,pady=20,command=lambda: click('/'))
button.grid(row=2,column=3)
# '*' operator
button = Button(root,text='*',padx=35,pady=20,command=lambda: click('*'))
button.grid(row=3,column=3)
# '-' operator
button = Button(root,text='-',padx=36,pady=20,command=lambda: click('-'))
button.grid(row=4,column=3)
# '+' operator
button = Button(root,text='+',padx=34,pady=20,command=lambda: click('+'))
button.grid(row=5,column=3)
# '%' operator
button = Button(root,text='%',padx=19,pady=20,command=lambda: click('%'))
button.grid(row=4,column=2)

# * Clear button 
button = Button(root,text='Clear',padx=23,pady=20,command=clear)
button.grid(row=1,column=3)

# * Equal(evaluate) button
button = Button(root,text='=',padx=75,pady=20,command=evaluate)
button.grid(row=5,column=0,columnspan=3)

root.mainloop()