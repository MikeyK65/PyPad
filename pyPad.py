from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

from PIL import ImageTk, Image

root = Tk()
root.title ('PyPad!')
root.iconbitmap('')
root.geometry ("1200x680")

global currentFileName
currentFilename = False

global selectedText
selectedText = False

calcCurrent = 0
calcFirstNum = 0

# Menu functions
def newFile():
    myText.delete("1.0", END)       # Delete all existing
    root.title("New File")
    statusBar.config(text="New File    ")
    global currentFileName
    currentFilename = False

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

 # Common code for saving   
def saveFile():
    global currentFileName
    if currentFilename:
        Save (currentFilename)
        statusBar.config(text="File Saved  ")
        # Put a pop here if needed

        
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


def cutText (e):
    global selectedText

    if e:
        selectedText = root.clipboard_get()
    else:
        if myText.selection_get():
            selectedText = myText.selection_get()
            myText.delete("sel.first", "sel.last")
            # Clear clipboard
            root.clipboard_clear()
            root.clipboard_append(selectedText)




def copyText (e):
    global selectedText

    # Check if we used keyboard
    if e:
        selectedText = root.clipboard_get()

    if myText.selection_get():
        selectedText = myText.selection_get()

        # Clear clipboard
        root.clipboard_clear()
        root.clipboard_append(selectedText)

def pasteText (e):
    global selectedText

    if e:
        selectedText = root.clipboard_get()
    else:
        if selectedText:
            position = myText.index(INSERT)
            myText.insert(position, selectedText)



def boldText():
    boldFont = font.Font(myText, myText.cget("font"))
    boldFont.config(weight="bold")

    # configure tag
    myText.tag_configure("bold", font=boldFont)

    # see if we need to un-bold text
    current_tags = myText.tag_names("sel.first")
    if "bold" in current_tags:
        myText.tag_remove("bold", "sel.first","sel.last")
    else:
        myText.tag_add("bold", "sel.first","sel.last")


def italicsText():
    italicsFont = font.Font(myText, myText.cget("font"))
    italicsFont.config(slant="italic")

    # configure tag
    myText.tag_configure("italic", font=italicsFont)

    # see if we need to un-bold text
    current_tags = myText.tag_names("sel.first")
    if "italic" in current_tags:
        myText.tag_remove("italic", "sel.first","sel.last")
    else:
        myText.tag_add("italic", "sel.first","sel.last")    

def calcButtonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))



def addToCalc(symbol):
    global calcCurrent
    #calcCurrent += str(symbol)
    #textResult.delete(1.0,"end")


def buttonPlus():
    currentNumber = e.get()

    global calcFirstNum
    calcFirstNum = int(currentNumber)
    e.delete(0, END)

    

def buttonEquals():
    currentNum = e.get()
    e.delete(0,END)
    e.insert (0, str(int(calcFirstNum) + int(currentNum)))



def buttonClear():
    e.delete(0, END)


def toolCalculator():
    newWindow = Toplevel(root)
    newWindow.geometry("300x400")
    newWindow.title ("Calculator")
    global e

    e = Entry(newWindow, width=35, borderwidth=5)
    e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    calc1 = Button(newWindow, text="1", padx=40, pady=20, command=lambda: calcButtonClick(1))
    calc2 = Button(newWindow, text="2", padx=40, pady=20, command=lambda: calcButtonClick(2))
    calc3 = Button(newWindow, text="3", padx=40, pady=20, command=lambda: calcButtonClick(3))
    calc4 = Button(newWindow, text="4", padx=40, pady=20, command=lambda: calcButtonClick(4))
    calc5 = Button(newWindow, text="5", padx=40, pady=20, command=lambda: calcButtonClick(5))
    calc6 = Button(newWindow, text="6", padx=40, pady=20, command=lambda: calcButtonClick(6))
    calc7 = Button(newWindow, text="7", padx=40, pady=20, command=lambda: calcButtonClick(7))
    calc8 = Button(newWindow, text="8", padx=40, pady=20, command=lambda: calcButtonClick(8))
    calc9 = Button(newWindow, text="9", padx=40, pady=20, command=lambda: calcButtonClick(9))
    calc0 = Button(newWindow, text="0", padx=40, pady=20, command=lambda: calcButtonClick(0))

    calcAdd = Button(newWindow, text="+", padx=40, pady=20, command=buttonPlus)
    calcEquals = Button(newWindow, text="=", padx=40, pady=20, command=buttonEquals)
    calcClear = Button(newWindow, text="Clear", padx=40, pady=20, command=buttonClear)


    calc1.grid(row=3, column=0)
    calc2.grid(row=3, column=1)
    calc3.grid(row=3, column=2)

    calc4.grid(row=2, column=0)
    calc5.grid(row=2, column=1)
    calc6.grid(row=2, column=2)

    calc7.grid(row=1, column=0)
    calc8.grid(row=1, column=1)
    calc9.grid(row=1, column=2)

    calc0.grid(row=4, column=1)
    calcAdd.grid(row=5, column=0)
    calcEquals.grid(row=5, column=1)
    calcClear.grid(row=5, column=2)

    #global calcCurrent
    #calcCurrent = 0

    #textResult = Text(newWindow, height=2, width=16, font=("Arial", 24))
    #textResult.grid(columnspan=5)


def textColour():
    # Pick a colour
    myColour = colorchooser.askcolor()[1]

    if myColour:

        #statusBar.config(text="Colour: " + str(myColour))
        statusBar.config(text=myColour)

        textColourFont = font.Font(myText, myText.cget("font"))

        # configure tag
        myText.tag_configure("coloured", font=textColourFont, foreground=myColour)

        # see if we need to un-bold text
        current_tags = myText.tag_names("sel.first")
        if "coloured" in current_tags:
            myText.tag_remove("coloured", "sel.first","sel.last")
        else:
            myText.tag_add("coloured", "sel.first","sel.last")    


def bgColour():
    myColour = colorchooser.askcolor()[1]

    if myColour:
        myText.config(bg=myColour)

def allTextColour():
    myColour = colorchooser.askcolor()[1]

    if myColour:
        myText.config(fg=myColour)


toolBarFrame = Frame(root)
toolBarFrame.pack(fill=X)

# Create main frame
myFrame = Frame(root)
myFrame.pack (pady=15)

# horizontal scroll bar
horizonalScroll = Scrollbar(myFrame, orient="horizontal")
horizonalScroll.pack(side=BOTTOM, fill=X)

# Create scrollbar
text_scroll = Scrollbar(myFrame)
text_scroll.pack(side=RIGHT, fill=Y)

myText = Text(myFrame, width=97, height=25, font=("Helvetica",16),selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=horizonalScroll.set)
myText.pack()

text_scroll.config(command=myText.yview)
horizonalScroll.config(command=myText.xview)


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
editMenu.add_command(label="Cut", command=lambda:cutText(False), accelerator="(Ctrl+x)")
editMenu.add_command(label="Copy", command=lambda:copyText(False), accelerator="(Ctrl+c)")
editMenu.add_command(label="Paste", command=lambda:pasteText(False), accelerator="(Ctrl+v)")
editMenu.add_command(label="Undo", command=myText.edit_undo, accelerator="(Ctrl+z)")
editMenu.add_command(label="Redo", command=myText.edit_redo, accelerator="(Ctrl+y)")

toolsMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Tools", menu=toolsMenu)
toolsMenu.add_command(label="Calculator", command=toolCalculator)

colourMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Colours", menu=colourMenu)
colourMenu.add_command(label="Selected Text", command=textColour)
colourMenu.add_command(label="All Text", command=allTextColour)
colourMenu.add_command(label="Background", command=bgColour)


#add status bar to bottom
statusBar = Label(root, text="Ready   ", anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=15)

# Keyboard bindings
root.bind('<Control-Key-x>', cutText)
root.bind('<Control-Key-c>', copyText)
root.bind('<Control-Key-v>', pasteText)


# Create toolbar buttons
boldButton = Button(toolBarFrame, text="Bold", command=boldText)
boldButton.grid(row = 0, column=0, sticky=W, padx=5)

italicsButton = Button(toolBarFrame, text="Italics", command=italicsText)
italicsButton.grid(row = 0, column=1, sticky=W, padx=5)

undoButton = Button(toolBarFrame, text="Undo", command=myText.edit_undo)
undoButton.grid(row = 0, column=2, sticky=W, padx=5)

redoButton = Button(toolBarFrame, text="Redo", command=myText.edit_redo)
redoButton.grid(row = 0, column=3, sticky=W, padx=5)

colourTextButton = Button(toolBarFrame, text="Text Colour", command=textColour)
colourTextButton.grid (row=0, column = 4, padx=5)

root.mainloop()
