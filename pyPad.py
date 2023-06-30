from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title ('PyPad!')
root.iconbitmap('')
root.geometry ("1200x660")

global currentFileName
currentFilename = False


# Menu functions
def newFile():
    myText.delete("1.0", END)       # Delete all existing
    root.title("New File")
    statusBar.config(text="New File    ")

def openFile():
    myText.delete("1.0", END)       # Delete all existing
    textFile = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All files", "*.*")))

    if textFile:
        global currentFilename
        currentFilename = textFile
    
    name = textFile.split("/")
    statusBar.config(text="Opened File " + name[-1])
    root.title = (f'{name} - PyPad')
    
    textFile = open(textFile, "r")
    stuff = textFile.read()

    myText.insert(END, stuff)
    textFile.close()

def Save (file):
    textFile = open(file, "w")
    textFile.write(myText.get(1.0, E))
    textFile.close()

    
def saveFile():
    global currentFileName
    if currentFilename:
        Save (currentFilename)
        statusBar.config(text="File Saved  ")
    else:
        saveAsFile()

def saveAsFile():
    textFile = filedialog.asksaveasfilename(defaultextension=".*", initialdir="", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All files", "*.*")))
    if (textFile):
        name =(textFile.split("/"))[-1]
        root.title = (f'{name} - PyPad (Saved)')

        Save (textFile)
        #textFile = open(textFile, "w")
        #textFile.write(myText.get(1.0, E))
        #textFile.close()

        statusBar.config(text="File Saved  ")


# Create main frame
myFrame = Frame(root)
myFrame.pack (pady=5)

# Create scrollbar
text_scroll = Scrollbar(myFrame)
text_scroll.pack(side=RIGHT, fill=Y)

myText = Text(myFrame, width=97, height=25, font=("Helvetica",16),selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
myText.pack()

text_scroll.config(command=myText.yview)

# Create menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Add file menu
fileMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As", command=saveAsFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# Add edit menu
editMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

#add status bar to bottom
statusBar = Label(root, text="Ready   ", anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=5)
               

root.mainloop()
