from tkinter import *
import os
from PIL import ImageTk, Image

# MAIN SCREEN

master = Tk()
master.title('Banking App')
master.configure(bg='White')


#  FUNCTIONS

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="Please fill all the Required fields")
    else:
        for name_check in all_accounts:
            if name == name_check:
                notif.config(fg='red', text='Account Already exists')
                break
        else:
            new_file = open(name, "w")
            new_file.write(name + '\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg='green',text='Account Has Been Created')





def register():
    # VARIABLES
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #  REGISTER SCREEN
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen.geometry("300x280")

    # LABELS

    Label(register_screen, text='Please Enter Your Details Below', font=('Calibri', 12)).grid(row=0, columnspan=2,
                                                                                              sticky=N, pady=10)
    Label(register_screen, text='Name', font=('Calibri', 12)).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Label(register_screen, text='Age', font=('Calibri', 12)).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Label(register_screen, text='Gender', font=('Calibri', 12)).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Label(register_screen, text='Password', font=('Calibri', 12)).grid(row=4, column=0, sticky=W, padx=10, pady=5)

    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=11, columnspan=2)

    Entry(register_screen, textvariable=temp_name).grid(row=1, column=1, padx=5, pady=5)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=1, padx=5, pady=5)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=1, padx=5, pady=5)
    Entry(register_screen, textvariable=temp_password, show='*').grid(row=4, column=1, padx=5, pady=5)

    Button(register_screen, text="Register", command=finish_reg, bg='#749BC2',font=('Calibri', 12)).grid(row=5, columnspan=2,sticky=N, pady=11)

def login_session():
    global login_name


    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    account_exists = False

    for name in all_accounts:
        if name == login_name:
            print("Account exists")
            account_exists = True

            file_path = os.path.join(name)
            with open(file_path, "r") as file:
                file_data = file.read()
                file_data = file_data.split('\n')
                password = file_data[3]

                # Account Dashboard
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title("Dashboard")
                    #LABELS
                    Label(account_dashboard, text='Account DashBoard',font=('Calibri', 12)).grid(row=0, columnspan=2, sticky=N, pady=10)
                    Label(account_dashboard, text='Welcome '+name, font=('Calibri', 12)).grid(row=1, columnspan=2,sticky=N, pady=7)
                    #Buttons
                    Button(account_dashboard, text="Personal Details",font=('Calibri', 12),bg='#749BC2',width=30,command=personal_details).grid(row=2,sticky=N,padx=10,pady=5)
                    Button(account_dashboard, text="Deposit", font=('Calibri', 12),bg='#749BC2', width=30,command=deposit).grid(row=3, sticky=N, padx=10,pady=5)
                    Button(account_dashboard, text="Withdraw", font=('Calibri', 12), bg='#749BC2',width=30,command=withdraw).grid(row=4, sticky=N,padx=10,pady=5)
                    Label(account_dashboard).grid(row=5,sticky=N,pady=10)


                else:
                    login_notif.config(fg='red', text='Incorrect Password !')

    if not account_exists:
        login_notif.config(fg='red', text='No Account Found in This Name')

    login_notif.grid(row=4, columnspan=2, sticky='n', pady=10, padx=5)

def deposit():
# Variables
    global amount
    global deposit_notif
    global current_balance
    amount = StringVar()
    file = open(login_name,'r')
    file_data= file.read()
    user_details = file_data.split('\n')
    details_balance =user_details[4]

    #  Deposit Screen


    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")

#  Label
    Label(deposit_screen, text="Deposit", font=('Calibri', 12)).grid(row=0, columnspan=2, sticky=N, pady=10)
    current_balance = Label(deposit_screen, text="Current Balance: $" + details_balance, font=('Calibri', 12))
    current_balance.grid(row=1, columnspan=2, sticky=W, padx=10, pady=5)
    Label(deposit_screen, text="Amount:", font=('Calibri', 12)).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    deposit_notif = Label(deposit_screen, font=('Calibri', 12))
    deposit_notif.grid(row=4, columnspan=2, sticky=N, pady=5)

#  Entry
    Entry(deposit_screen, textvariable=amount, font=('Calibri', 12)).grid(row=2, column=1, padx=10, pady=5)

#  Button
    Button(deposit_screen, text="Finish", font=('Calibri', 12), bg='#749BC2',command=finish_deposit).grid(row=3, columnspan=2, sticky='n', pady=10)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is Required', fg='red')
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text='Negative Currency is not accepted', fg='red')
        return

    file_name = login_name  # Assuming login_name is a StringVar
    file_path = os.path.join(file_name)

    with open(file_path, 'r+') as file:
        file_data = file.read()
        details = file_data.split('\n')
        account_balance = float(details[4])
        updated_balance = account_balance + float(amount.get())
        updated_balance = round(updated_balance, 2)  # Round off to 2 decimals

        # Update the balance in the file_data
        details[4] = str(updated_balance)
        file_data = '\n'.join(details)

        file.seek(0)
        file.truncate(0)
        file.write(file_data)

    current_balance.config(text='Current Balance: $' + str(updated_balance), fg='green')
    deposit_notif.config(text='Balance Updated', fg='green')


def withdraw():
    global w_amount
    global w_notif
    global current_balance
    w_amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    #  Deposit Screen

    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")

    #  Label
    Label(withdraw_screen, text="Deposit", font=('Calibri', 12)).grid(row=0, columnspan=2, sticky=N, pady=10)
    current_balance = Label(withdraw_screen, text="Current Balance: $" + details_balance, font=('Calibri', 12))
    current_balance.grid(row=1, columnspan=2, sticky=W, padx=10, pady=5)
    Label(withdraw_screen, text="Amount:", font=('Calibri', 12)).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    w_notif = Label(withdraw_screen, font=('Calibri', 12))
    w_notif.grid(row=4, columnspan=2, sticky=N, pady=5)

    #  Entry
    Entry(withdraw_screen, textvariable=w_amount, font=('Calibri', 12)).grid(row=2, column=1, padx=10, pady=5)

    #  Button
    Button(withdraw_screen, text="Finish", font=('Calibri', 12), bg='#749BC2', command=finish_withdraw).grid(row=3, columnspan=2, sticky='n',pady=10)
def finish_withdraw():
    if w_amount.get() == "":
        w_notif.config(text='Amount is Required', fg='red')
        return
    if float(w_amount.get()) <= 0:
        w_notif.config(text='Negative Currency is not accepted', fg='red')
        return

    file_name = login_name  # Assuming login_name is a StringVar
    file_path = os.path.join(file_name)

    with open(file_path, 'r+') as file:
        file_data = file.read()
        details = file_data.split('\n')
        account_balance = float(details[4])
        if float(w_amount.get()) > float(account_balance):
            w_notif.config(text='Insufficient Funds!', fg='red')
            return

        updated_balance = account_balance - float(w_amount.get())
        updated_balance = round(updated_balance, 2)  # Round off to 2 decimals

        # Update the balance in the file_data
        details[4] = str(updated_balance)
        file_data = '\n'.join(details)

        file.seek(0)
        file.truncate(0)
        file.write(file_data)

    current_balance.config(text='Current Balance: $' + str(updated_balance), fg='green')
    w_notif.config(text='Balance Updated', fg='green')

def personal_details():
    # Variables
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details [1]
    details_gender = user_details[2]
    details_balance = user_details[4]

    #  PERSONAL DETAILS SCREEN

    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")

    #  Labels

    Label(personal_details_screen, text= ' Your Personal Details',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text='Name: '+details_name, font=('Calibri', 12)).grid(row=1, sticky=W, pady=1)
    Label(personal_details_screen, text='Age: '+details_age, font=('Calibri', 12)).grid(row=2, sticky=W, pady=1)
    Label(personal_details_screen, text='Gender: '+details_gender, font=('Calibri', 12)).grid(row=3, sticky=W, pady=1)
    Label(personal_details_screen, text='Your Account Balance: $'+details_balance, font=('Calibri', 12)).grid(row=4, sticky=W, pady=1)



def login():
    #Variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

# LOGIN SCREEN
    login_screen = Toplevel(master)
    login_screen.title("Login")

    # LABELS
    Label(login_screen, text="Login into Your Account", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10, padx=5)
    Label(login_screen, text="Username", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=('Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)

    #  Entries
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password,show='*').grid(row=2, column=1, padx=5)

    #  Buttons
    Button(login_screen, text='Login', command=login_session, width=15,bg='#749BC2', font=('Calibri', 12)).grid(row=3, columnspan=2,
                                                                                                   sticky='n', pady=20,
                                                                                                   padx=5)


# IMAGE IMPORT
img = Image.open('image.png')
img = img.resize((250, 150))
img = ImageTk.PhotoImage(img)

# LABELS
Label(master, text="Customer Banking Beta", font=('Calibri', 14), bg='White').grid(row=0, sticky=N, pady=10)
Label(master, text="The Most Secure Bank You have possibly Used!", font=('Calibri', 12), bg='White').grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

# BUTTONS
Button(master, text="Register", font=('Calibri', 12), width=20,bg='#749BC2',command=register).grid(row=3, sticky=N)
Button(master, text="Login", font=('Calibri', 12), width=20,bg='#749BC2',command=login).grid(row=4, sticky=N,pady=11)

master.mainloop()
