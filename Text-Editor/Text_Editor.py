from tkinter import Tk,Menu,Frame,Scrollbar,Text
from tkinter import NORMAL,DISABLED,INSERT,SEL_FIRST,SEL_LAST
from tkinter import END,BOTH,NONE,LEFT,RIGHT,BOTTOM,VERTICAL,HORIZONTAL,X,Y
from tkinter import filedialog as fd
from tkinter import font


### Functions ######################################################################

# * Function to enable the 'Save' and 'Save As' options of File Menu
def enable_save_file():
    file_menu.entryconfig('Save File', state=NORMAL)
    file_menu.entryconfig('Save As File...', state=NORMAL)


# * Function to create a New File
def create_new_file(event=False):
    global file_loc                            # ! using of Global Variable
    file_loc = None
    root.title('New File')
    editor_box.configure(state=NORMAL,      # Enable the writing into the editor box
                             bg="#DCE0E1")
    editor_box.delete(1.0,END)              # Clearing the Previous Content

    enable_save_file()                      # Enable the 'Save' and 'Save As' options in file menu

# * Function to Open a File
def open_file(event=False):
    global file_loc                            # ! using of Global Variable
    # Getting the file Location
    root.option_add('*foreground', '#00A6BD')
    file_loc = fd.askopenfilename(master=root, initialdir = "./",
                                   title = "Select a File",
                                   filetypes = (("TEXT files","*.txt"),
                                               ("All files","*.*")))
    # Opening the file
    try:    # Dealing with the Exception
        with open(file_loc,'r') as file:
            file_content = file.read()
    except Exception:
        print("Can't open this file")
    else:
        title = file_loc.split('/')[-1]         # fetching the only file name
        root.title(title + ' - Text Editor')    # Display the name on the title bar
        editor_box.configure(state=NORMAL,      # Enable the writing into the editor box
                             bg="#DCE0E1")
        editor_box.delete(1.0,END)              # Clearing the Previous Content
        editor_box.insert(1.0,file_content)     # Adding the new content
        enable_save_file()                      # Enable the 'Save' and 'Save As' options in file menu

# * Function to Save a File
def save_file(event=False):
    global file_loc                             # ! using of Global Variable
    # selecting the file name and location
    if file_loc is None:
        root.option_add('*foreground', '#00A6BD')
        file_loc = fd.asksaveasfilename(master=root, initialdir = "./",
                                         title = "Save the File",
                                         filetypes = (("TEXT files","*.txt"),
                                                      ("All files","*.*")))
    # Saving the file
    with open(file_loc,'w') as file:
        file_content = editor_box.get(1.0,END)
        file.write(file_content[:-1])
    
    title = file_loc.split('/')[-1]             # fetching the only file name
    root.title(title + ' - Text Editor')        # Display the name on the title bar

# * Function to Save As a File
def save_as_file(event=False):
    global file_loc                             # ! using of Global Variable
    # selecting the file name and location
    root.option_add('*foreground', '#00A6BD')
    file_loc = fd.asksaveasfilename(master=root, initialdir = "./",
                                     title = "Save the File As",
                                     filetypes = (("TEXT files","*.txt"),
                                                  ("All files","*.*")))
    # Saving the file
    with open(file_loc,'w') as file:
        file_content = editor_box.get(1.0,END)
        file.write(file_content[:-1])

# * Function to exit from the text editor
def exit_editor(event=False):
    exit()

# * Function for Undo Method
def undo_text():
    editor_box.edit_undo()

# * Function for Redo Method
def redo_text():
    editor_box.edit_redo()

# * Function for Cut Method
def cut_text(event=False):
    if not event:
        root.clipboard_clear()
        root.clipboard_append(editor_box.selection_get())
        editor_box.delete('sel.first','sel.last')

# * Function for Copy Method
def copy_text(event=False):
    if not event:
        root.clipboard_clear()
        root.clipboard_append(editor_box.selection_get())

# * Function for Paste Method
def paste_text(event=False):
    if not event:
        cursor_position = editor_box.index(INSERT)
        editor_box.insert(cursor_position,root.clipboard_get())

# * Function for Selecting all text
def select_all_text(event=False):
    editor_box.tag_add('sel',1.0,END)

# * Function to clear all text
def clear_all_text(event=False):
    editor_box.delete(1.0,END)



# * Function to change the text weight to Bold
def bold_text(event=False):
    bold_font = font.Font(editor_box,editor_box.cget('font'))
    bold_font.config(weight='bold')
    editor_box.tag_configure('bold',font=bold_font)
    
    current_tags = editor_box.tag_names('sel.first')
    if 'bold' in current_tags:
        editor_box.tag_remove('bold', SEL_FIRST, SEL_LAST)
    else:
        editor_box.tag_add('bold', SEL_FIRST, SEL_LAST)

# * Function to change the text slant to Italic
def italic_text(event=False):
    italic_font = font.Font(editor_box,editor_box.cget('font'))
    italic_font.config(slant='italic')
    editor_box.tag_configure('italic',font=italic_font)
    
    current_tags = editor_box.tag_names('sel.first')
    if 'italic' in current_tags:
        editor_box.tag_remove('italic', SEL_FIRST, SEL_LAST)
    else:
        editor_box.tag_add('italic', SEL_FIRST, SEL_LAST)


### root ###########################################################################
# ! Global Variables
file_loc = None

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
file_menu.add_command(label='New File', command=create_new_file,            # New File
                        accelerator='(Ctrl + n)')        
file_menu.add_command(label='Open File...', command=open_file,              # Open File
                        accelerator='(Ctrl + o)')          
file_menu.add_command(label='Save File', command=save_file,                 # Save File
                        state=DISABLED, accelerator='(Ctrl + s)')
file_menu.add_command(label='Save As File...', command=save_as_file,        # Save As File
                        state=DISABLED, accelerator='(Ctrl+Shift+S)')    
file_menu.add_separator()                                                   # (Separator)
file_menu.add_command(label='Exit', command=exit_editor,                    # Exit
                        accelerator='(Ctrl + q)')                

# Key bindings for File Menu
root.bind('<Control-n>',create_new_file)
root.bind('<Control-o>',open_file)
root.bind('<Control-s>',save_file)
root.bind('<Control-Shift-S>',save_as_file)
root.bind('<Control-q>',exit_editor)


# * Creating the Edit Menu
edit_menu = Menu(root_menu, tearoff=False)
root_menu.add_cascade(label='Edit', menu=edit_menu)
# Edit Menu contents declaring
edit_menu.add_command(label='Undo', command=undo_text,                      # Undo Text
                        accelerator='(Ctrl + z)')        
edit_menu.add_command(label='Redo', command=redo_text,                      # Redo Text
                        accelerator='(Ctrl + y)')        
edit_menu.add_separator()                                                   # (Separator)
edit_menu.add_command(label='Cut', command=cut_text,                        # Cut Text
                        accelerator='(Ctrl + x)')
edit_menu.add_command(label='Copy', command=copy_text,                      # Copy Text
                        accelerator='(Ctrl + c)')                           
edit_menu.add_command(label='Paste     ', command=paste_text,               # Paste Text
                        accelerator='(Ctrl + v)')
edit_menu.add_separator()                                                   # (Separator)
edit_menu.add_command(label='Select All', command=select_all_text,          # Select All Text 
                        accelerator='(Ctrl + a)')
edit_menu.add_command(label='Clear All', command=clear_all_text,            # Clear All Text
                        accelerator='(Ctrl + del)')
# Key bindings for Edit Menu
root.bind('<Control-x>',cut_text)
root.bind('<Control-c>',copy_text)
root.bind('<Control-v>',paste_text)
root.bind('<Control-a>',select_all_text)
root.bind('<Control-Delete>',clear_all_text)

# * Creating the View Menu
view_menu= Menu(root_menu, tearoff=False)
root_menu.add_cascade(label='View', menu=view_menu)
# View Menu contents declaring
view_menu.add_command(label='Font Style',command=None)                  # Font Style
view_menu.add_command(label='Font Size',command=None)                   # Font Size
edit_menu.add_separator()
view_menu.add_command(label='Bold', command=bold_text,                      # Bold
                        accelerator='(Ctrl + b)')
view_menu.add_command(label='Italic', command=italic_text,                  # Italic
                        accelerator='(Ctrl + i)')

# * Creating the Theme Menu
theme_menu= Menu(root_menu, tearoff=False)
root_menu.add_cascade(label='Theme', menu=theme_menu)
# Theme Menu contents declaring
theme_menu.add_command(label='Theme 1',command=None)                    
theme_menu.add_command(label='Theme 2',command=None)


### Read Write Frame ###############################################################
# * Frame for holding all components in reading writing process
frame = Frame(root)
frame.pack(fill=BOTH,expand=True)

# * Scroll Bars
# Vertical Scroll Bar
vscrollbar = Scrollbar(frame, orient=VERTICAL, bg='#111212')
vscrollbar.pack(side=RIGHT, fill = Y)

# Horizontal Scroll Bar
hscrollbar = Scrollbar(frame, orient=HORIZONTAL, bg='#111212')
hscrollbar.pack(side=BOTTOM, fill = X)

# * Editor Box
editor_box = Text(frame, state=DISABLED, undo=True,
                  bg="#5E5F5F", fg='#111212',
                  wrap=NONE,
                  yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
editor_box.pack(side=LEFT,fill=BOTH,expand=True)
# configuring the Scroll Bars
vscrollbar.config(command=editor_box.yview)
hscrollbar.config(command=editor_box.xview)

### Main Loop ######################################################################
root.mainloop()