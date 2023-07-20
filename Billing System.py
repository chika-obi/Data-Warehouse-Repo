#===================================================================
from tkinter import *
#===================BOILER PLATE====================================
root = Tk()
root.title("OCK BILLING SYSTEM")
#root.resizable(False,False)
root.geometry("1400x800+100+100")
#==========================HEADER====================================
contaninerFrame=Frame(root)
contaninerFrame.pack(fill = X)
headerLabel = Label(contaninerFrame,text = "OCK BILLING SYSTEM"
                    ,bg="#0000ff",bd =40,relief="groove"
                    ,fg = "#cccccc",font=('Time New Roman',30,'bold'))
headerLabel.pack(fill=X)
#==========================CUSTOMER DETAILS======================================
customerDetails=LabelFrame(contaninerFrame,text = "Customer Details",bg = "#0000ff"
                           ,font=("Time New Roman",12,"normal"),bd=20,relief = "sunken")
customerDetails.pack(padx = 20,pady = 10,fill=X)
labelName = Label(customerDetails,text = "Name",font=("Time New Roman",12,"bold"))
labelName.grid(row=0,column = 0,padx = 20,pady = 10)
labelNameEntry = Entry(customerDetails)
labelNameEntry.grid(row=0,column = 1)

phoneNumber = Label(customerDetails,text = "Phone Number",font=("Time New Roman",12,"bold"))
phoneNumber.grid(row=0,column = 2)
phoneNumberEntry = Entry(customerDetails)
phoneNumberEntry.grid(row=0,column = 3)

billNumber = Label(customerDetails,text = "Bill Number",font=("Time New Roman",12,"bold"))
billNumber.grid(row=0,column = 4)
billNumberEntry = Entry(customerDetails)
billNumberEntry.grid(row=0,column = 5)

btnSearch = Button(customerDetails,text = "Search",font=("Time New Roman",12,"bold"),padx = 10,bd=4)
btnSearch.grid(row=0,column=6)
#Search 
root.mainloop()
