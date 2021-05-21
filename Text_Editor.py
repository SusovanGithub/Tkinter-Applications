from tkinter import *
from tkinter import filedialog as fd


### Functions ######################################################################

# * Function to enable the 'Save' and 'Save As' options of File Menu
def enable_save_file():
    file_menu.entryconfig('Save File', state=NORMAL)
    file_menu.entryconfig('Save As File...', state=NORMAL)


# * Function to create a New File
def create_new_file():
    root.title('New File')
    editor_box.configure(state=NORMAL,      # Enable the writing into the editor box 
                         bg="#DCE0E1")
    enable_save_file()                      # Enable the 'Save' and 'Save As' options in file menu

# * Function to Open a File
def open_file():
    global file_name                            # ! using of Global Variable
    # Getting the file Location
    root.option_add('*foreground', '#00A6BD')
    file_name = fd.askopenfilename(master=root, initialdir = "./",
                                   title = "Select a File",
                                   filetypes = (("TEXT files","*.txt"),
                                               ("All files","*.*")))
    # Opening the file
    try:    # Dealing with the Exception
        with open(file_name,'r') as file:
            file_content = file.read()
    except Exception:
        print("Can't open this file")
    else:
        root.title(file_name)                   # Display the name on the title bar
        enable_save_file()                      # Enable the 'Save' and 'Save As' options in file menu
        editor_box.configure(state=NORMAL,      # Enable the writing into the editor box
                             bg="#DCE0E1")
        editor_box.delete(1.0,END)              # Clearing the Previous Content
        editor_box.insert(1.0,file_content)     # Adding the new content

# * Function to Save a File
def save_file():
    global file_name                                # ! using of Global Variable
    # selecting the file name and location
    if file_name is None:
        root.option_add('*foreground', '#00A6BD')
        file_name = fd.asksaveasfilename(master=root, initialdir = "./",
                                         title = "Save the File",
                                         filetypes = (("TEXT files","*.txt"),
                                                      ("All files","*.*")))
    # Saving the file
    with open(file_name,'w') as file:
        file_content = editor_box.get(1.0,END)
        file.write(file_content[:-1])
    # todo show a Massage box

# * Function to Save As a File
def save_as_file():
    global file_name                                # ! using of Global Variable
    # selecting the file name and location
    root.option_add('*foreground', '#00A6BD')
    file_name = fd.asksaveasfilename(master=root, initialdir = "./",
                                     title = "Save the File",
                                     filetypes = (("TEXT files","*.txt"),
                                                  ("All files","*.*")))
    # Saving the file
    with open(file_name,'w') as file:
        file_content = editor_box.get(1.0,END)
        file.write(file_content[:-1])
    # todo show a Massage box

# * Function to exit from the text editor
def exit_editor():
    exit()

### root ###########################################################################
# ! Global Variables
file_name = None

root = Tk()
root.title('Text Editor')
root.geometry('400x400')

### Creating the Menu Bar ##########################################################
root_menu = Menu(root)                  # Creating the Menu Bar
root.config(menu=root_menu)             # Adding to the root

# * Creating the File Menu
file_menu = Menu(root_menu,tearoff=False)
root_menu.add_cascade(label='File', menu=file_menu)
# File Menu contents declaring
file_menu.add_command(label='New File', command=create_new_file)
file_menu.add_command(label='Open File...', command=open_file)
file_menu.add_command(label='Save File', command=save_file, state=DISABLED)
file_menu.add_command(label='Save As File...', command=save_as_file, state=DISABLED)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_editor)

# * Creating the Edit Menu
edit_menu = Menu(root_menu)

# * Creating the Theme Menu
theme_menu= Menu(root_menu)


### Read Write Frame ###############################################################
# * Frame for holding all components in reading writing process
frame = Frame(root)
frame.pack(fill=BOTH,expand=True)

# * Scroll Bar
scrollbar = Scrollbar(frame, orient=VERTICAL, bg='#111212')
scrollbar.pack(side=RIGHT, fill = Y)

# * Editor Box
editor_box = Text(frame, state=DISABLED,
                  bg="#5E5F5F", fg='#111212',
                  yscrollcommand=scrollbar.set)
editor_box.pack(side=LEFT,fill=BOTH,expand=True)
# configuring the scrollbar 
scrollbar.config(command=editor_box.yview)


### Main Loop ######################################################################
root.mainloop()
