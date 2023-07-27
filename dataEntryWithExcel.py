import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Generate the code
generated_code = '''import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #course info
            registration_status = reg_status_var.get()
            newcourses = newcourses_spinbox.get()
            numsemesters =   numsemesters_spinbox.get()
            print("--------------------------------------------------------------------------------")
            print(f"My Firstname is :{firstname} and My Lastname is : {lastname}, I am {age} \
                  years Old and from {nationality} courses: \
                  {newcourses} semesters: {numsemesters}) \
                  and the Registration Status: {registration_status}")
            print("--------------------------------------------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First Name and Last Name are Required")
            
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not Accepted the Terms and Conditions")


window = tkinter.Tk()
window.title("Data Entry Form")
window.resizable(False, False)

# Set the window size
# window.geometry("700x400")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for centering the window
x = (screen_width // 4) - (window.winfo_width() // 4)
y = (screen_height // 4) - (window.winfo_height() // 4)

# Set the window's position
window.geometry(f"+{x}+{y}")
'''
frame = tkinter.Frame(window)  # reponsive
frame.pack()  # place and grid are other options

# saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame,
                              values=[" ", "Mr.", "Mrs.", "Ms.", "Miss", "Dr.", "Prof.", "Sen.", "Hon.", "Chief",
                                      "Hrm."])
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)

age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Afghan", "Albanian", "Algerian", "American",
                                                             "Andorran", "Angolan", "Antiguans", "Argentinean",
                                                             "Armenian", "Australian", "Austrian", "Azerbaijani",
                                                             "Bahamian", "Bahraini", "Bangladeshi", "Barbadian",
                                                             "Barbudans", "Batswana", "Belarusian", "Belgian",
                                                             "Belizean", "Beninese", "Bhutanese", "Bolivian",
                                                             "Bosnian", "Brazilian", "British", "Bruneian",
                                                             "Bulgarian", "Burkinabe", "Burmese", "Burundian",
                                                             "Cambodian", "Cameroonian", "Canadian", "Cape Verdean",
                                                             "Central African", "Chadian", "Chilean", "Chinese",
                                                             "Colombian", "Comoran", "Congolese", "Costa Rican",
                                                             "Croatian", "Cuban", "Cypriot", "Czech", "Danish",
                                                             "Djibouti", "Dominican", "Dutch", "East Timorese",
                                                             "Ecuadorean", "Egyptian", "Emirian", "Equatorial Guinean",
                                                             "Eritrean", "Estonian", "Ethiopian", "Fijian",
                                                             "Filipino", "Finnish", "French", "Gabonese", "Gambian",
                                                             "Georgian", "German", "Ghanaian", "Greek", "Grenadian",
                                                             "Guatemalan", "Guinea-Bissauan", "Guinean", "Guyanese",
                                                             "Haitian", "Herzegovinian", "Honduran", "Hungarian",
                                                             "I-Kiribati", "Icelander", "Indian", "Indonesian",
                                                             "Iranian", "Iraqi", "Irish", "Israeli", "Italian",
                                                             "Ivorian", "Jamaican", "Japanese", "Jordanian",
                                                             "Kazakhstani", "Kenyan", "Kittian and Nevisian",
                                                             "Kuwaiti", "Kyrgyz", "Laotian", "Latvian", "Lebanese",
                                                             "Liberian", "Libyan", "Liechtensteiner", "Lithuanian",
                                                             "Luxembourger", "Macedonian", "Malagasy", "Malawian",
                                                             "Malaysian", "Maldivian", "Malian", "Maltese",
                                                             "Marshallese", "Mauritanian", "Mauritian", "Mexican",
                                                             "Micronesian", "Moldovan", "Monacan", "Mongolian",
                                                             "Moroccan", "Mosotho", "Motswana", "Mozambican",
                                                             "Namibian", "Nauruan", "Nepalese", "New Zealander",
                                                             "Nicaraguan", "Nigerian", "Nigerien", "North Korean",
                                                             "Northern Irish", "Norwegian", "Omani", "Pakistani",
                                                             "Palauan", "Panamanian", "Papua New Guinean",
                                                             "Paraguayan", "Peruvian", "Polish", "Portuguese",
                                                             "Qatari", "Romanian", "Russian", "Rwandan",
                                                             "Saint Lucian", "Salvadoran", "Samoan", "San Marinese",
                                                             "Sao Tomean", "Saudi", "Scottish", "Senegalese",
                                                             "Serbian", "Seychellois", "Sierra Leonean",
                                                             "Singaporean", "Slovakian", "Slovenian",
                                                             "Solomon Islander", "Somali", "South African",
                                                             "South Korean", "Spanish", "Sri Lankan", "Sudanese",
                                                             "Surinamer", "Swazi", "Swedish", "Swiss", "Syrian",
                                                             "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese",
                                                             "Tongan", "Trinidadian or Tobagonian", "Tunisian",
                                                             "Turkish", "Tuvaluan", "Ugandan", "Ukrainian",
                                                             "Uruguayan", "Uzbekistani", "Venezuelan", "Vietnamese",
                                                             "Welsh", "Yemenite", "Zambian", "Zimbabwean"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registration_label1 = tkinter.Label(courses_frame, text="Registration Status")
registration_label1.grid(row=0, column=0)

reg_status_var = tkinter.StringVar(value="Not Registered")
registration_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var,
                                         onvalue="Registered", offvalue="Not Registered")
registration_check.grid(row=1, column=0)

newcourses_label1 = tkinter.Label(courses_frame, text="#Completed Courses")
newcourses_label1.grid(row=0, column=1)

newcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
newcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="#Semesters")
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I Accept the Terms and Conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

# Write the generated code to a cell in the Excel sheet
sheet["A1"] = generated_code

# Save the workbook to a file
workbook.save("generated_code.xlsx")
