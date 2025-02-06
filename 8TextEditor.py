from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to open a file and load its content into the text area
def openFile():
    print("Open")
    filepath = askopenfilename(filetypes=[("Text files(.txt)",".txt"),("All Files", "*.*")])
    if not filepath:
        return
    txtEdit.delete(1.0, END)
    with open(filepath , "r") as input_file:
        text= input_file.read()
        txtEdit.insert(1.0, text)
        screen.title(f"Simple text editor - {filepath}")

# Function to save the content of the text editor to a file
def saveFile():
    print("Save")
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text files(.txt)",".txt"),("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txtEdit.get(1.0, END)
        output_file.write(text)
        screen.title(f"Simple text editor - {filepath}")

# Remove all text from the editor
def clearFile():
    print("Clear")
    txtEdit.delete(1.0, END)


def exitFile():
    print("Exit")
    screen.destroy()

# Function to toggle between dark and light modes
def darkmode():
    darkset = darkView.get()
    if  darkset== 1:
        txtEdit.config(bg='Black',fg='White')
    elif darkset==0:
        txtEdit.config(bg='White', fg='Black')
    else:
        print("Wrong Value!!,Only 1 and O.")
        messagebox.showerror()


def aboutHelp():
    messagebox.showinfo("Help", "to give or provide what is necessary to accomplish a task or satisfy a need; contribute strength or means to; render assistance to; cooperate effectively with; aid; assist")



screen = Tk() #creates window
screen.title("Text Editor") # Title
screen.rowconfigure(0, minsize=800, weight=1)
screen.columnconfigure(1, minsize=800, weight=1)
screen.geometry('1000x700')
screen.resizable(height=False, width=False)

# File menu with options
menubar = Menu(screen)
file = Menu(menubar)
file.add_command(label = "Open", command=openFile)
file.add_command(label = "Save As", command=saveFile)
file.add_command(label = "Clear", command=clearFile)
file.add_command(label = "Exit", command=exitFile)
menubar.add_cascade(label="File", menu=file)


darkView = BooleanVar()
darkView.set(False)



view = Menu(menubar)
view.add_checkbutton(label = "Dark Mode", onvalue=1 , offvalue=0,variable=darkView, command= darkmode)
menubar.add_cascade(label="View", menu=view)


help = Menu(menubar)
help.add_command(label = "About", command=aboutHelp)
menubar.add_cascade(label="Help",menu=help)


txtEdit = Text(screen)
txtEdit.grid(row=0,column=1,sticky="nsew")




screen.config(menu= menubar)
screen.mainloop() #klenei programma