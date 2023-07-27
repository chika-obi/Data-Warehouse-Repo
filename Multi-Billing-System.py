from tkinter import *
from tkinter import PhotoImage
#========================================================================
window = Tk()
window.title("Ock Billing System")
window.resizable(0,0)
window.geometry("1303x700+60+0")
#========================================================================
rootFrame = Frame(window)
rootFrame.pack()
#========================================================================
containerFrame = Frame(rootFrame,bg="red",bd= 4,relief ="ridge",pady = 10)
containerFrame.grid(row= 0,column =0)

image = PhotoImage(file = "logo.png",width = 60,height = 60)
#========================================================================
lblCompanyLogo = Label(containerFrame,image=image)
lblCompanyLogo.grid(row = 0,column = 0)
#========================================================================
lblCustomersName = Label(containerFrame,text="Customer's Name ",bg="red")
lblCustomersName.grid(row = 0,column = 1)
lblCustomersNameEntry = Entry(containerFrame)
lblCustomersNameEntry.grid(row = 0,column = 2)
#========================================================================
lblPhoneNumber = Label(containerFrame,text="Phone Number",bg="red")
lblPhoneNumber.grid(row = 0,column = 3)
lblPhoneNumberEntry = Entry(containerFrame)
lblPhoneNumberEntry.grid(row = 0,column = 4)
#========================================================================
lblBillNumber = Label(containerFrame,text="Bill Number",bg="red")
lblBillNumber.grid(row = 0,column = 5)
lblBillNumberEntry = Entry(containerFrame)
lblBillNumberEntry.grid(row = 0,column = 6)
#========================================================================
btnSearch = Button(containerFrame,text="Search",bg="red",width = 8)
btnSearch.grid(row = 0,column = 7)
#========================================================================
for widget in containerFrame.winfo_children():
    widget.grid_configure(padx=7,pady = 7)
    widget.configure(font = ("Arial",13,"bold"),fg="#ccc")
#=============================CALCULATOR FUNCTIONS===========================================
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, result)
#===============================================================================================
subrootFrame = Frame(rootFrame)
subrootFrame.grid()
#===============================================================================================
lblStoreFrame = Frame(subrootFrame)
lblStoreFrame.grid(row =0,column = 0,padx=5)
#===============================================================================================

#lblStock = Label(lblStoreFrame,text = "STOCK")
#lblStock.grid(row = 0,column = 0,columnspan=6)
lblFood = Label(lblStoreFrame,text = "\t\tFOOD")
lblFood.grid(row = 1,column = 0)

lblDrinks = Label(lblStoreFrame,text = "\t\tDRINKS")
lblDrinks.grid(row = 1,column = 1)

lblBeverage = Label(lblStoreFrame,text = "\tBeverages")
lblBeverage.grid(row = 1,column = 2)

lblWater = Label(lblStoreFrame,text = "\tWater")
lblWater.grid(row = 1,column = 3)

lblElectronics = Label(lblStoreFrame,text = "\tElectronics")
lblElectronics.grid(row = 1,column = 4)

lblGroceries = Label(lblStoreFrame,text = "\tGroceries")
lblGroceries.grid(row = 1,column = 5)

#lbl1Stock = Label(lblStoreFrame,text = "STOCK")
#lbl1Stock.grid(row = 0,column = 0,columnspan=6)
lblFood1 = Label(lblStoreFrame,text = "\t\tFOOD")
lblFood1.grid(row = 2,column = 0)


lblDrinks1 = Label(lblStoreFrame,text = "\t\tDRINKS")
lblDrinks1.grid(row = 2,column = 1)

lblBeverage1 = Label(lblStoreFrame,text = "\tBeverages")
lblBeverage1.grid(row = 2,column = 2)

lblWater1 = Label(lblStoreFrame,text = "\tWater")
lblWater1.grid(row = 2,column = 3)

lblElectronics1 = Label(lblStoreFrame,text = "\tElectronics")
lblElectronics1.grid(row = 2,column = 4)

lblGroceries1 = Label(lblStoreFrame,text = "\tGroceries")
lblGroceries1.grid(row = 2,column = 5)




for widget in lblStoreFrame.winfo_children():
    widget.grid_configure(padx=1,pady=1)
    widget.configure(bd=3,bg="gray",fg="white",font=("Arial",12,"bold"))

#===============================================================================================
calculatorFrame = Frame(subrootFrame,relief = "flat",bd=4,pady=8,bg = "#ccc")
calculatorFrame.grid(row =0,column = 1)
#===============================================================================================
entry = Entry(calculatorFrame, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

button_1 = Button(calculatorFrame, text="1", command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(calculatorFrame, text="2", command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(calculatorFrame, text="3", command=lambda: button_click(3))
button_3.grid(row=3, column=2)
button_4 = Button(calculatorFrame, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(calculatorFrame, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(calculatorFrame, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(calculatorFrame, text="7", command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(calculatorFrame, text="8", command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(calculatorFrame, text="9", command=lambda: button_click(9))
button_9.grid(row=1, column=2)
button_0 = Button(calculatorFrame, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_add = Button(calculatorFrame, text="+", command=lambda: button_click("+"))
button_add.grid(row=1, column=3)

button_subtract = Button(calculatorFrame, text="-" , command=lambda: button_click("-"))
button_subtract.grid(row=2, column=3)

button_multiply = Button(calculatorFrame, text="*", command=lambda: button_click("*"))
button_multiply.grid(row=3, column=3)
button_divide = Button(calculatorFrame, text=chr(247), command=lambda: button_click("/"))
button_divide.grid(row=4, column=3)

button_equal = Button(calculatorFrame, text="=", command=button_equal)
button_equal.grid(row=4, column=1,columnspan = 3)

button_clear = Button(calculatorFrame, text="C", command=button_clear)

button_clear.grid(row=4, column=1)
#========================================================================
for widget in calculatorFrame.winfo_children():
    widget.grid_configure(padx=5,pady=5)
    widget.configure(bd=3,bg="gray",fg="white")
#========================================================================

#========================================================================
#========================================================================
#========================================================================




window.mainloop()
