from tkinter import Entry, Tk, Label, Scale, Frame, ttk, TOP, X, BOTH, Grid, Button,N,S,W,E, IntVar
from matrices import matrix

def refreshTable(noOfVar):
    global numsTotal
    numsTotal = {}
    for widget in frame1.winfo_children():
        widget.destroy()
    noOfVar = int(noOfVar)
    for row in range(noOfVar+1):
        if (row == 0):
            for column in range(noOfVar+2): 
                if (column == 0):
                    lbl1 = Label(frame1, text = "Eq No.", borderwidth = 3, relief="sunken")
                elif (column == noOfVar+1):
                    lbl1 = Label(frame1, text = "C", borderwidth = 3, relief="sunken")
                else:
                    lbl1 = Label(frame1, text = "x"+str(column), borderwidth = 3, relief="sunken")
                
                lbl1.grid(row=row, column=column, sticky=N+S+E+W)
                frame1.grid_columnconfigure(column, weight=1)

        else:
            nums = {}
            for i in range(1,noOfVar+2):
                nums["num"+str(row)+str(i)] = IntVar()
            numsTotal[row]= nums

            for column in range(noOfVar+2): 
                if (column == 0):
                    lbl1 = Label(frame1, text = str(row))
                    lbl1.grid(row=row, column=column)
                else:
                    for i in nums:
                        entryBox = Entry(frame1, width = 10, textvariable=nums["num"+str(row)+str(column)])
                        entryBox.grid(row=row, column=column)
                        
                frame1.grid_columnconfigure(column, weight=1)
                        

def refreshAnswerTable(answerMatrix):
    for widget in frame2.winfo_children():
        widget.destroy()
    noOfVar = int(noVarScale.get())
    for row in range(1, noOfVar+1):
        for column in range(2):
            if (column == 0):
                lbl1 = Label(frame2, text = "x"+str(row)+"=")
                lbl1.grid(row=row-1, column=column)
            else:
                lbl1 = Label(frame2, text = answerMatrix[row-1][0])
                lbl1.grid(row = row-1, column=column)


def solve():
    m1 = matrix(int(noVarScale.get()), int(noVarScale.get()))
    for i in range(int(noVarScale.get())):
        listOfRowNum = []
        for j in range(1, int(noVarScale.get())+1):
            #listOfRowNum.append("num"+str(i)+str(j))
            #print(i, j)
            num1 = numsTotal[i+1]["num"+str(i+1)+str(j)].get()
            listOfRowNum.append(num1)
        m1.insertRow(listOfRowNum)
    
    m2 = matrix(int(noVarScale.get()), 1)
    for i in range(int(noVarScale.get())):
        const1 = numsTotal[i+1]["num"+str(i+1)+str(int(noVarScale.get())+1)].get()
        m2.insertRow(const1)

    m1 = m1.inverse()
    answer1 = m1 ** m2

    refreshAnswerTable(answer1)

        
def start():
    global window
    window = Tk()
    window.geometry("800x400")
    window.iconbitmap("icon.ico")
    window.title("System of Linear Equations Solver")

    global noVarScale
    noVarScale = Scale(window, label = "Number of variables", from_= 2, to = 6, command = refreshTable, fg= "white", bg = "blue", activebackground = "red", troughcolor = "pink", orient = "horizontal")
    noVarScale.pack(fill = X)

    global frame1
    frame1 = Frame(window)
    frame1.pack(fill=X)
    refreshTable(2)

    btn1 = Button(window, text = "Click to reset", command = reset)
    btn1.pack()
    solveBtn = Button(window, text = "Solve!", command = solve)
    solveBtn.pack()

    global frame2
    frame2 = Frame(window)
    frame2.pack()

    window.mainloop()

def reset():
    window.destroy()
    start()


start()
