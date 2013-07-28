# -*- coding: utf-8 -*-
#Initialize the program - Import all dependancies
from Gui import *
import math
import random
import os
import tkMessageBox
import tkFileDialog
#Set the globals to 0
memory = 0 #Memory button
errordel = 0 #Was the last result on the screen an error?
memprevpress = 0 #Was the last button pressed MRC? (for clearing the memory)
dmode = 'RAD' #Default advanced calculator mode (RAD or DEG)

####################### MENU FUNCTIONS #######################

### File Menus ###
def exitProgram(): #Exit Program
    window.destroy()

def radMode(): #Radian Mode (Advanced)
    global dmode
    dmode = 'RAD'
    advCalc()

def degMode(): #Degree Mode (Advanced)
    global dmode
    dmode = 'DEG'
    advCalc()

def saveTape(): #Save Paper Tape - Paper Tape
    try:
        fout = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        contents = str(tapetext.get(0.0,END))
        fout.write(contents)
        fout.close()
    except:
        error = True

def saveTable(): #Save Table - Table Mode
    try:
        fout = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        contents = str(tabletext.get(0.0,END))
        fout.write(contents)
        fout.close()
    except:
        error = True

### Edit Menus ###
def cutButton(event=None): #Cut - Calculator
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    window.clipboard_clear()
    window.clipboard_append(str(eqn))

def copyButton(event=None): #Copy - Calculator
    eqn = display.get(0.0,END)
    window.clipboard_clear()
    window.clipboard_append(str(eqn))

def copyButtonp(event=None): #Copy - Paper Tape
    eqn = tapetext.get(0.0,END)
    window.clipboard_clear()
    window.clipboard_append(str(eqn))

def copyButtont(event=None): #Copy - Table Mode
    eqn = tabletext.get(0.0,END)
    window.clipboard_clear()
    window.clipboard_append(str(eqn))

def pasteButton(event=None): #Paste - Calculator
    eqn = window.selection_get(selection='CLIPBOARD')
    display.insert(END,eqn)

def selectallButton(event=None): #Select All - Calculator
    display.tag_add("sel","1.0","end")

def selectallButtonp(event=None): #Select All - Paper Tape
    tapetext.tag_add("sel","1.0","end")

def selectallButtont(event=None): #Select All - Table Mode
    tabletext.tag_add("sel","1.0","end")

def undoButton(event=None): #Undo - Calculator
    display.delete(0.0,END)
    prevAns()

def clearButton(event=None): #Clear Screen - Calculator
    display.delete(0.0,END)

def clearButtonp(event=None): #Clear Screen - Paper Tape
    tapetext.delete(0.0,END)

def clearButtont(event=None): #Clear Screen - Table Mode
    tabletext.delete(0.0,END)

### Help Menus ###
def basicDialog(): #Basic Calculator Help
    os.startfile("http://www.ehow.com/how_2083458_use-calculator.html")

def advDialog(): #Advanced Calculator Help
    os.startfile("http://www.ehow.com/how_7272430_use-scientific-calculators.html")

def aboutDialog(): #About WinCalc Dialog
    tkMessageBox.showinfo(title="About WinCalc...", message="WinCalc v1.0\nBuild Date: Jan 13th, 2013\nCopyright (c)2013 Justin Paulin\n\nSupport URL: http://justinpaulin.com/\nSupport Email: wincalc@justinpaulin.com")

###################### /MENU FUNCTIONS #######################

#################### CALCULATOR FUNCTIONS ####################

### Basic Button Functions ###
def buttonPress(thing): #Basic Button Press
    global errordel
    global memprevpress
    memprevpress = 0
    if errordel == 1:
        display.delete(0.0,END)
        errordel = 0
    thing = str(thing)
    display.insert(END,thing)

def plusMinus(): #Plus/Minus Button
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = eqn*-1
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def percentButton(): #Percentage Button
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = eqn*0.01
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def squareRoot(): #Square Root Button
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = math.sqrt(eqn)
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def factorial(num): #Factorial Button (Advanced Mode)
    b = 1
    for i in range(num):
        i = i+1
        b = b*i
    return b

def radians(num): #Degrees to Radians (Advanced Mode)
    num = float(num)*((3.14159265359)/180)
    return num

def degrees(num): #Radians to Degrees (Advanced Mode)
    num = float(num)*(180/(3.14159265359))
    return num

### Modification Functions ###
def delButton(): #Backspace Button
    global errordel
    global memprevpress
    memprevpress = 0
    if errordel == 1:
        display.delete(0.0,END)
        errordel = 0
    eqn = display.get(0.0,END)
    eqn = eqn[0:-2]
    display.delete(0.0,END)
    display.insert(END,eqn)

def clearDisplay(): #AC Button
    global errordel
    global memprevpress
    memprevpress = 0
    display.delete(0.0,END)
    errordel = 0

### Memory Functions ###
def memRc(): #Memory Recall/Clear Button
    global memprevpress
    global memory
    if memprevpress == 1:
        memory = 0
        memprevpress = 0
        mrc.config(font='Arial 9')
    else :
        if memory == 0:
            memprevpress = 0
        else:
            display.insert(END,memory)
            memprevpress = 1

def memPlus(): #M+ Button (Basic)
    global memprevpress
    global memory
    global prevans
    global errordel
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        display.insert(0.0,eqn)
        prevans = eqn
        memory = memory+eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1
    if memory == 0:
        mrc.config(font='Arial 9')
    else:
        mrc.config(font='Arial 9 bold')

def memMinus(): #M- Button (Basic)
    global memprevpress
    global memory
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        display.insert(0.0,eqn)
        prevans = eqn
        memory = memory-eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1
    if memory == 0:
        mrc.config(font='Arial 9')
    else:
        mrc.config(font='Arial 9 bold')

def amemPlus(): #M+ Button (Advanced)
    global memprevpress
    global memory
    global prevans
    global errordel
    memprevpress = 0
    solveAdv()
    eqn = display.get(0.0,END)
    try:
        eqn = eval(eqn)
        memory = memory+eqn
    except:
        errordel = 1
    if memory == 0:
        mrc.config(font='Arial 9')
    else:
        mrc.config(font='Arial 9 bold')

def amemMinus(): #M- Button (Advanced)
    global memprevpress
    global memory
    global prevans
    global errordel
    memprevpress = 0
    solveAdv()
    eqn = display.get(0.0,END)
    try:
        eqn = eval(eqn)
        memory = memory-eqn
    except:
        errordel = 1
    if memory == 0:
        mrc.config(font='Arial 9')
    else:
        mrc.config(font='Arial 9 bold')

### Misc Button Functions ###
def prevAns(): #Ans Button (Previous Answer)
    global memprevpress
    global errordel
    errordel = 0
    memprevpress = 0
    try:
        int(prevans)
    except:
        display.delete(0.0,END)
    display.insert(END,str(prevans))

def diceRoll(): #DICE Button (Random Dice Roll)
    buttonPress(random.randint(1,6))

def binConvert(): #D->BIN Button (Binary Converter)
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = str(bin(eqn)).replace("0b", "")
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def hexConvert(): #D->HEX Button (Hexadecimal Converter)
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = str(hex(eqn)).replace("0x", "")
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def octConvert(): #D->OCT Button (Octlet Converter)
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    display.delete(0.0,END)
    try:
        eqn = eval(eqn)
        eqn = str(oct(eqn)).replace("0o", "")
        display.insert(0.0,eqn)
        prevans = eqn
    except:
        eqn = str(eqn)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

### Solve Functions ###
def solveEqn(event=None): #Equals Button (Basic)
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    eqnb = eqn
    display.delete(0.0,END)
    eqn = '1.0*'+eqn
    try:
        display.insert(0.0,eval(eqn))
        prevans = eval(eqn)
        tapeText(str(str(eqnb)+"="+str(prevans)+"\n\n"))
    except:
        eqn = str(eqnb)
        prevans = eqn.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1

def solveAdv(event=None): #Equals Button (Advanced)
    global prevans
    global errordel
    global memprevpress
    memprevpress = 0
    eqn = display.get(0.0,END)
    eqnb = eqn
    if dmode == 'RAD':
        eqn = eqn.replace("\n", "")
        eqn = eqn.replace("sin(", "math.sin(")
        eqn = eqn.replace("cos(", "math.cos(")
        eqn = eqn.replace("tan(", "math.tan(")
        eqn = eqn.replace("sin^-1(", "math.asin(")
        eqn = eqn.replace("cos^-1(", "math.acos(")
        eqn = eqn.replace("tan^-1(", "math.atan(")
        eqn = eqn.replace("sinh(", "math.sinh(")
        eqn = eqn.replace("cosh(", "math.cosh(")
        eqn = eqn.replace("tanh(", "math.tanh(")
        eqn = eqn.replace("sinh^-1", "math.asinh(")
        eqn = eqn.replace("cosh^-1", "math.acosh(")
        eqn = eqn.replace("tanh^-1", "math.atanh(")
        eqn = eqn.replace("Ran#", str(random.random()))
        eqn = eqn.replace("!(", "factorial(")
        eqn = eqn.replace("sqrt(", "math.sqrt(")
        eqn = eqn.replace("ln(", "math.log(")
    else:
        eqn = eqn.replace("\n", "")
        eqn = eqn.replace("sin(", "math.sin(radians(")
        eqn = eqn.replace("cos(", "math.cos(radians(")
        eqn = eqn.replace("tan(", "math.tan(radians(")
        eqn = eqn.replace("sin^-1(", "math.asin(radians(")
        eqn = eqn.replace("cos^-1(", "math.acos(radians(")
        eqn = eqn.replace("tan^-1(", "math.atan(radians(")
        eqn = eqn.replace("sinh(", "math.sinh(radians(")
        eqn = eqn.replace("cosh(", "math.cosh(radians(")
        eqn = eqn.replace("tanh(", "math.tanh(radians(")
        eqn = eqn.replace("sinh^-1", "math.asinh(radians(")
        eqn = eqn.replace("cosh^-1", "math.acosh(radians(")
        eqn = eqn.replace("tanh^-1", "math.atanh(radians(")
        eqn = eqn.replace("Ran#", str(random.random()))
        eqn = eqn.replace("!(", "factorial(")
        eqn = eqn.replace("sqrt(", "math.sqrt(")
        eqn = eqn.replace("ln(", "math.log(")
    display.delete(0.0,END)
    eqn = '1.0*'+eqn
    for i in range(11):
        try:
            eqntest = str(eqn) + ')'*i
            eval(eqntest)
            eqn = eqntest
            break
        except SyntaxError:
            error = True #print 'DEBUG - Brackets'
        except ValueError:
            break
        except:
            break
    try:
        display.insert(0.0,eval(eqn))
        prevans = eval(eqn)
        tapeText(str(str(eqnb)+"="+str(prevans)+"\n\n"))
    except SyntaxError:
        eqn = str(eqn)
        prevans = eqnb.replace("\n", "")
        display.insert(0.0,'Syntax Error!\nPress "Ans" to retry.')
        errordel = 1
    except ValueError:
        eqn = str(eqn)
        prevans = eqnb.replace("\n", "")
        display.insert(0.0,'Math Error!\nPress "Ans" to retry.')
        errordel = 1
    except OverflowError:
        eqn = str(eqn)
        prevans = eqnb.replace("\n", "")
        display.insert(0.0,'Overflow Error!\nPress "Ans" to retry.')
        errordel = 1
    except:
        eqn = str(eqn)
        prevans = eqnb.replace("\n", "")
        display.insert(0.0,'Calculation Error!\nPress "Ans" to retry.')
        errordel = 1

#################### /CALCULATOR FUNCTIONS ###################

#################### TABLE MODE FUNCTIONS ####################
### Window Rendering ###
def tableMode(): #Build the Table Mode Window
    global tableentry
    global tableentrymin
    global tableentrymax
    global tableentrystep
    global tabletext
    global tablemode
    try:
        tablemode.destroy()
    except:
        error = True #print "DEBUG - NO TABLE ENABLED"
    tablemode = Gui()
    tablemode.option_add( "*font", "Arial 9" )
    tablemode.minsize(300,420)
    tablemode.maxsize(300,420)
    tablemode.iconbitmap('icon.ico')
    tablemode.title("WinCalc (Table Mode)")
    menubar = Menu(tablemode)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save to File", command=saveTable)
    filemenu.add_separator()
    filemenu.add_command(label="Close", command=tablemode.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Copy All", command=copyButtont)
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=selectallButtont)
    editmenu.add_command(label="Clear Table", command=clearButtont)
    menubar.add_cascade(label="Edit", menu=editmenu)
    tablemode.config(menu=menubar)
    tablemode.gr(cols=2)
    tablemode.la(text="f(x)=")
    tableentry = tablemode.te(width=20,height=1,font=("Courier New", 16))
    tablemode.la(text="MIN=")
    tableentrymin = tablemode.te(width=20,height=1,font=("Courier New", 16))
    tablemode.la(text="MAX=")
    tableentrymax = tablemode.te(width=20,height=1,font=("Courier New", 16))
    tablemode.la(text="STEP")
    tableentrystep = tablemode.te(width=20,height=1,font=("Courier New", 16))
    tablemode.endgr()
    tablemode.gr(cols=1)
    tablemode.bu("Get Table of Values",command=tableIt)
    tablemode.endgr()
    tabletext = tablemode.te(width=280, height=390, padx=2, pady=2, ipadx=2, ipady=2, borderwidth = 1, relief = SUNKEN)
    tkMessageBox.showinfo(title="WinCalc Table Mode - Instructions", message="The table of values generator uses the same syntax as the advanced calculator. Radian mode only.")
    tablemode.mainloop()
    
### Processing Functions ###
def tableIt(): #Calculate Table
    try:
        eqn = tableentry.get(0.0, END)
        mini = float(tableentrymin.get(0.0, END))
        maxi = float(tableentrymax.get(0.0, END))
        step = float(tableentrystep.get(0.0, END))
        tabletext.delete(0.0,END)
        tabletext.insert(END,"Equation: f(x)="+str(eqn))
        tabletext.insert(END,"STEP: "+str(step)+", MIN: "+str(mini)+", MAX: "+str(maxi)+"\n\n")
        eqn = eqn.replace("x", "mini")
        eqn = eqn.replace("sin(", "math.sin(")
        eqn = eqn.replace("cos(", "math.cos(")
        eqn = eqn.replace("tan(", "math.tan(")
        eqn = eqn.replace("sin^-1(", "math.asin(")
        eqn = eqn.replace("cos^-1(", "math.acos(")
        eqn = eqn.replace("tan^-1(", "math.atan(")
        eqn = eqn.replace("sinh(", "math.sinh(")
        eqn = eqn.replace("cosh(", "math.cosh(")
        eqn = eqn.replace("tanh(", "math.tanh(")
        eqn = eqn.replace("sinh^-1", "math.asinh(")
        eqn = eqn.replace("cosh^-1", "math.acosh(")
        eqn = eqn.replace("tanh^-1", "math.atanh(")
        eqn = eqn.replace("degrees(", "math.degrees(")
        eqn = eqn.replace("radians(", "math.radians(")
        eqn = eqn.replace("Ran#", str(random.random()))
        eqn = eqn.replace("!(", "factorial(")
        eqn = eqn.replace("sqrt(", "math.sqrt(")
        eqn = eqn.replace("ln(", "math.log(")
        tabletext.insert(END,"-----------------------------------------\n")
        while mini < maxi:
            try:
                ans = eval(eqn)
                tabletext.insert(END,"x="+str(mini)+" | f(x)="+str(ans)+"\n")
                tabletext.insert(END,"-----------------------------------------\n")
                mini = mini + step
            except:
                tabletext.insert(END,"x="+str(mini)+" | f(x)=ERROR\n")
                tabletext.insert(END,"-----------------------------------------\n")
                mini = mini + step
    except:
        tabletext.delete(0.0,END)
        tabletext.insert(END,"INPUT ERROR")

#################### /TABLE MODE FUNCTIONS ###################

#################### PAPER TAPE FUNCTIONS ####################
### Window Rendering ###
def paperTape(): #Build the Paper Tape Window
    global tapetext
    global papertape
    try:
        papertape.destroy()
    except:
        error = True #print "DEBUG - NO PAPER TAPE"
    papertape = Gui()
    papertape.option_add( "*font", "Arial 9" )
    papertape.minsize(300,400)
    papertape.maxsize(300,400)
    papertape.iconbitmap('icon.ico')
    papertape.title("WinCalc (Paper Tape)")
    menubar = Menu(papertape)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save to File", command=saveTape)
    filemenu.add_separator()
    filemenu.add_command(label="Close", command=papertape.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Copy All", command=copyButtonp)
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=selectallButtonp)
    editmenu.add_command(label="Clear Paper Tape", command=clearButtonp)
    menubar.add_cascade(label="Edit", menu=editmenu)
    papertape.config(menu=menubar)
    tapetext = papertape.te(width=280, height=390, padx=2, pady=2, ipadx=2, ipady=2, borderwidth = 1, relief = SUNKEN)
    papertape.mainloop()
    
### Processing Functions ###
def tapeText(text): #Add to the Paper Tape Roll
    try:
        tapetext.insert(END,text)
        tapetext.yview(END)
    except:
        error = True #print "DEBUG - NO PAPER TAPE"
        
#################### /PAPER TAPE FUNCTIONS ###################

##################### GRAPHING FUNCTIONS #####################
### Window Rendering ###
def grapherCalc(): #Build the Graph Window
    global entry
    global grapher
    global canvas
    try:
        grapher.destroy()
    except:
        error = True #print "DEBUG - NO GRAPHER ENABLED"
    grapher = Gui()
    grapher.minsize(500,550)
    grapher.maxsize(500,550)
    grapher.iconbitmap('icon.ico')
    grapher.title("WinCalc (Equation Grapher)")
    grapher.bind ('<Return>', graphIt)
    grapher.gr(cols=3)
    grapher.la(text="f(x)=")
    entry = grapher.te(width=30,height=1,font=("Courier New", 16))
    entry.insert(0.0,"x**2")
    grapher.bu("Graph It",command=graphIt)
    grapher.endgr()
    canvas = grapher.ca(width=500, height=500, bg='white')
    graphIt()
    tkMessageBox.showinfo(title="WinCalc Equation Grapher - Instructions", message="The equation grapher uses the same syntax as the advanced calculator.\nSyntax errors will result in a blank graph. Radian mode only.")
    entry.focus_set()
    grapher.mainloop()
    
### Graph Rendering ###
def graphIt(event=None): #Calculate the Points & Render the Graph
    lasti = 'UNSET'
    lasty = 'UNSET'
    eqn = entry.get(0.0,END)
    eqnb = eqn
    entry.delete(0.0,END)
    eqnb = eqnb.replace("\n", "")
    entry.insert(0.0,eqnb)
    eqn = eqn.replace("x", "i")
    eqn = eqn.replace("sin(", "math.sin(")
    eqn = eqn.replace("cos(", "math.cos(")
    eqn = eqn.replace("tan(", "math.tan(")
    eqn = eqn.replace("sin^-1(", "math.asin(")
    eqn = eqn.replace("cos^-1(", "math.acos(")
    eqn = eqn.replace("tan^-1(", "math.atan(")
    eqn = eqn.replace("sinh(", "math.sinh(")
    eqn = eqn.replace("cosh(", "math.cosh(")
    eqn = eqn.replace("tanh(", "math.tanh(")
    eqn = eqn.replace("sinh^-1", "math.asinh(")
    eqn = eqn.replace("cosh^-1", "math.acosh(")
    eqn = eqn.replace("tanh^-1", "math.atanh(")
    eqn = eqn.replace("degrees(", "math.degrees(")
    eqn = eqn.replace("radians(", "math.radians(")
    eqn = eqn.replace("Ran#", str(random.random()))
    eqn = eqn.replace("!(", "factorial(")
    eqn = eqn.replace("sqrt(", "math.sqrt(")
    eqn = eqn.replace("ln(", "math.log(")
    canvas.delete(ALL)
    ## Gridlines ##
    for i in range(51): #Horizontal
        i = i*10
        canvas.create_line(0,i,500,i, width=1, fill="gray")
    for i in range(51): #Vertical
        i = i*10
        canvas.create_line(i,0,i,500, width=1, fill="gray")
    ## Axis ##
    canvas.create_line(0,250,500,250, width=2, fill="black")
    canvas.create_line(250,0,250,500, width=2, fill="black")
    ## Scales ##
    for i in range(11): #Horizontal
        i = i*50
        canvas.create_line(250,i,260,i, width=2, fill="black")
        i = i - 250
        canvas.create_text(i+250,263, text='%d'% (0.1*i), anchor=N)
    for i in range(11): #Vertical
        i = i*50
        canvas.create_line(i,260,i,250, width=2, fill="black")
        i = i - 250
        canvas.create_text(270,i+245, text='%d'% (-0.1*i), anchor=N)

    lasti = 'UNSET' #Last variables (i = x) for use in connecting points
    lasty = 'UNSET'
    for i in range(501): #for each pixel (x value), do the calculation
        i = i-250
        i = i/float(10)
        try:
            y = eval(eqn)
            #DATA MANIPULATIONS
            y = -1*y
            y = y*10
            i = i*10
            y = y+250
            i = i+250
            canvas.create_oval(i-1,y-1,i+1,y+1,width=1,fill="red",outline="red")
            if lasti == 'UNSET':
                lasti = i
                lasty = y
            else:
                if distance(i,y,lasti,lasty) < 100:
                    fillcol = "red"
                    canvas.create_line(i,y,lasti,lasty, width=2, fill=fillcol)
                lasti = i
                lasty = y
        except:
            error = True #print "DEBUG - INVALID EQUATION"
            
### Math Functions ###
def distance(x1, y1, x2, y2): #Distance Formula (For Assymptotes)
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

##################### /GRAPHING FUNCTIONS ####################

##################### CALCULATOR WINDOWS #####################
def basicCalc(): #Basic Calculator
    global window
    global display
    global prevans
    global mrc
    prevans = ''
    window.destroy()
    window = Gui()
    window.option_add( "*font", "Arial 9" ) 
    window.minsize(300,240)
    window.maxsize(300,240)
    window.iconbitmap('icon.ico')
    window.title("WinCalc (Basic Mode)")
    window.bind('<Return>', solveEqn)
    window.bind('<Control-a>', selectallButton)
    window.bind('<Control-A>', selectallButton)
    window.bind('<Control-v>', pasteButton)
    window.bind('<Control-V>', pasteButton)
    window.bind('<Control-e>', copyButton)
    window.bind('<Control-E>', copyButton)
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Advanced Mode", command=advCalc)
    filemenu.add_command(label="Reset Calculator", command=basicCalc)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exitProgram)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=undoButton)
    editmenu.add_separator()
    editmenu.add_command(label="Cut Equation", command=cutButton)
    editmenu.add_command(label="Copy Equation (Ctrl-E)", command=copyButton)
    editmenu.add_command(label="Paste Equation (Ctrl-V)", command=pasteButton)
    editmenu.add_separator()
    editmenu.add_command(label="Select All (Ctrl-A)", command=selectallButton)
    editmenu.add_command(label="Clear Equation", command=clearButton)
    menubar.add_cascade(label="Edit", menu=editmenu)
    goodies = Menu(menubar, tearoff=0)
    goodies.add_command(label="Equation Grapher", command=grapherCalc)
    goodies.add_command(label="Table of Values Generator", command=tableMode)
    goodies.add_separator()
    goodies.add_command(label="Show Paper Tape", command=paperTape)
    menubar.add_cascade(label="Goodies", menu=goodies)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instructions - Basic Mode", command=basicDialog)
    helpmenu.add_command(label="Instructions - Advanced Mode", command=advDialog)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=aboutDialog)
    menubar.add_cascade(label="Help", menu=helpmenu)
    window.config(menu=menubar)
    window.row()
    display = window.te(width=10, height=2, padx=2, pady=2, ipadx=2, ipady=2, borderwidth = 1, relief = SUNKEN, font=("Courier New", 16))
    window.endrow()
    window.row(pady=5,padx=5)
    window.gr(cols=5)
    mrc = window.bu(text='MRC',width=5,command=memRc)
    window.bu(text='M+',width=5,command=memPlus)
    window.bu(text='M-',width=5,command=memMinus)
    window.bu(text='DEL',width=5,command=delButton)
    window.bu(text='AC',width=5,command=clearDisplay)
    window.bu(text='7',width=5,command=Callable(buttonPress,7))
    window.bu(text='8',width=5,command=Callable(buttonPress,8))
    window.bu(text='9',width=5,command=Callable(buttonPress,9))
    window.bu(text='%',width=5,command=percentButton)
    window.bu(text='+/-',width=5,command=plusMinus)
    window.bu(text='4',width=5,command=Callable(buttonPress,4))
    window.bu(text='5',width=5,command=Callable(buttonPress,5))
    window.bu(text='6',width=5,command=Callable(buttonPress,6))
    window.bu(text='×',width=5,command=Callable(buttonPress,'*'))
    window.bu(text='÷',width=5,command=Callable(buttonPress,'/'))
    window.bu(text='1',width=5,command=Callable(buttonPress,1))
    window.bu(text='2',width=5,command=Callable(buttonPress,2))
    window.bu(text='3',width=5,command=Callable(buttonPress,3))
    window.bu(text='+',width=5,command=Callable(buttonPress,'+'))
    window.bu(text='−',width=5,command=Callable(buttonPress,'-'))
    window.bu(text='0',width=5,command=Callable(buttonPress,0))
    window.bu(text='.',width=5,command=Callable(buttonPress,'.'))
    window.bu(text='Ans',width=5,command=prevAns)
    window.bu(text='√',width=5,command=squareRoot)
    window.bu(text='=',width=5,command=solveEqn)
    window.endgr()
    window.endrow()
    display.focus_set()
    window.mainloop()
    try:
        papertape.destroy()
    except:
        error = True #print "DEBUG - NO PAPER TAPE ENABLED"
    try:
        grapher.destroy()
    except:
        error = True #print "DEBUG - NO GRAPHER ENABLED"

def advCalc(): #Advanced Calculator
    global window
    global display
    global prevans
    global mrc
    prevans = ''
    window.destroy()
    window = Gui()
    window.option_add( "*font", "Arial 9" ) 
    window.minsize(300,400)
    window.maxsize(300,400)
    window.iconbitmap('icon.ico')
    window.title("WinCalc (Advanced Mode)")
    window.bind('<Return>', solveAdv)
    window.bind('<Control-a>', selectallButton)
    window.bind('<Control-A>', selectallButton)
    window.bind('<Control-v>', pasteButton)
    window.bind('<Control-V>', pasteButton)
    window.bind('<Control-e>', copyButton)
    window.bind('<Control-E>', copyButton)
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Basic Mode", command=basicCalc)
    filemenu.add_command(label="Reset Calculator", command=advCalc)
    filemenu.add_separator()
    filemenu.add_command(label="Radian Mode", command=radMode)
    filemenu.add_command(label="Degree Mode", command=degMode)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exitProgram)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=undoButton)
    editmenu.add_separator()
    editmenu.add_command(label="Cut Equation", command=cutButton)
    editmenu.add_command(label="Copy Equation (Ctrl-E)", command=copyButton)
    editmenu.add_command(label="Paste Equation (Ctrl-V)", command=pasteButton)
    editmenu.add_separator()
    editmenu.add_command(label="Select All (Ctrl-A)", command=selectallButton)
    editmenu.add_command(label="Clear Equation", command=clearButton)
    menubar.add_cascade(label="Edit", menu=editmenu)
    goodies = Menu(menubar, tearoff=0)
    goodies.add_command(label="Equation Grapher", command=grapherCalc)
    goodies.add_command(label="Table of Values Generator", command=tableMode)
    goodies.add_separator()
    goodies.add_command(label="Show Paper Tape", command=paperTape)
    menubar.add_cascade(label="Goodies", menu=goodies)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instructions - Basic Mode", command=basicDialog)
    helpmenu.add_command(label="Instructions - Advanced Mode", command=advDialog)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=aboutDialog)
    menubar.add_cascade(label="Help", menu=helpmenu)
    window.config(menu=menubar)
    window.row()
    display = window.te(width=10, height=2, padx=2, pady=2, ipadx=2, ipady=2, borderwidth = 1, relief = SUNKEN, font=("Courier New", 16))
    window.endrow()
    window.row(pady=5,padx=5)
    window.gr(cols=5)
    ###BEGIN BUTTONS###
    mrc = window.bu(text='MRC',width=5,command=memRc)
    window.bu(text='M+',width=5,command=amemPlus)
    window.bu(text='M-',width=5,command=amemMinus)
    window.bu(text='DEL',width=5,command=delButton)
    window.bu(text='AC',width=5,command=clearDisplay)
    ######BEGIN ADVANCED FUNCTIONS#######
    window.la(dmode)
    window.bu(text='1/x',width=5,command=Callable(buttonPress,'1/('))
    window.bu(text='x^x',width=5,command=Callable(buttonPress,'**'))
    window.bu(text='x^2',width=5,command=Callable(buttonPress,'**2'))
    window.bu(text='π',width=5,command=Callable(buttonPress,'(3.14159265359)'))
    ##
    window.bu(text='sin^-1',width=5,command=Callable(buttonPress,'sin^-1('))
    window.bu(text='cos^-1',width=5,command=Callable(buttonPress,'cos^-1('))
    window.bu(text='tan^-1',width=5,command=Callable(buttonPress,'tan^-1('))
    window.bu(text='sinh',width=5,command=Callable(buttonPress,'sinh('))
    window.bu(text='sinh^-1',width=5,command=Callable(buttonPress,'sinh^-1('))
    ##
    window.bu(text='sin',width=5,command=Callable(buttonPress,'sin('))
    window.bu(text='cos',width=5,command=Callable(buttonPress,'cos('))
    window.bu(text='tan',width=5,command=Callable(buttonPress,'tan('))
    window.bu(text='cosh',width=5,command=Callable(buttonPress,'cosh('))
    window.bu(text='cosh^-1',width=5,command=Callable(buttonPress,'cosh^-1('))
    ##
    window.bu(text='DEG(x)',width=5,command=Callable(buttonPress,'degrees('))
    window.bu(text='RAD(x)',width=5,command=Callable(buttonPress,'radians('))
    window.bu(text='Ran#',width=5,command=Callable(buttonPress,'Ran#'))
    window.bu(text='tanh',width=5,command=Callable(buttonPress,'tanh('))
    window.bu(text='tanh^-1',width=5,command=Callable(buttonPress,'tanh^-1('))
    ##
    window.bu(text='DICE',width=5,command=diceRoll)
    window.bu(text='D->BIN',width=5,command=binConvert)
    window.bu(text='D->OCT',width=5,command=octConvert)
    window.bu(text='D->HEX',width=5,command=hexConvert)
    window.bu(text='x(2)√x(1)',width=5,command=Callable(buttonPress,'**(1.0/'))
    ##
    window.bu(text='(',width=5,command=Callable(buttonPress,'('))
    window.bu(text=')',width=5,command=Callable(buttonPress,')'))
    window.bu(text='x!',width=5,command=Callable(buttonPress,'!('))
    window.bu(text='ln(x)',width=5,command=Callable(buttonPress,'ln('))
    window.bu(text='e^x',width=5,command=Callable(buttonPress,'(2.71828182846)**'))
    ###END ADVANCED FUNCTIONS###
    window.bu(text='7',width=5,command=Callable(buttonPress,7))
    window.bu(text='8',width=5,command=Callable(buttonPress,8))
    window.bu(text='9',width=5,command=Callable(buttonPress,9))
    window.bu(text='%',width=5,command=Callable(buttonPress,'*0.01'))
    window.bu(text='+/-',width=5,command=Callable(buttonPress,'*-1'))
    ##
    window.bu(text='4',width=5,command=Callable(buttonPress,4))
    window.bu(text='5',width=5,command=Callable(buttonPress,5))
    window.bu(text='6',width=5,command=Callable(buttonPress,6))
    window.bu(text='×',width=5,command=Callable(buttonPress,'*'))
    window.bu(text='÷',width=5,command=Callable(buttonPress,'/'))
    ##
    window.bu(text='1',width=5,command=Callable(buttonPress,1))
    window.bu(text='2',width=5,command=Callable(buttonPress,2))
    window.bu(text='3',width=5,command=Callable(buttonPress,3))
    window.bu(text='+',width=5,command=Callable(buttonPress,'+'))
    window.bu(text='−',width=5,command=Callable(buttonPress,'-'))
    ##
    window.bu(text='0',width=5,command=Callable(buttonPress,0))
    window.bu(text='.',width=5,command=Callable(buttonPress,'.'))
    window.bu(text='Ans',width=5,command=prevAns)
    window.bu(text='√',width=5,command=Callable(buttonPress,'sqrt('))
    window.bu(text='=',width=5,command=solveAdv)
    ###END BUTTONS###
    window.endgr()
    window.endrow()
    display.focus_set()
    window.mainloop()
    try:
        papertape.destroy()
    except:
        error = True #print "DEBUG - NO PAPER TAPE ENABLED"
    try:
        grapher.destroy()
    except:
        error = True #print "DEBUG - NO GRAPHER ENABLED"
        
##################### /CALCULATOR WINDOWS ####################

### Start Program ###
window = Gui()
basicCalc()
