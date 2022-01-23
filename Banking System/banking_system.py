import json
import tkinter as tk
from tkinter import *


class BankingSystem:
    def __init__(self):
        # Do not add any parameter to this method.
        # Delete "pass" after adding code into this method.
        try:
            with open("data.txt") as f:
                data = f.read()
            js = json.loads(data)
            self.system = js
        except:
            print("Can not Open File")
            print("Exiting...")
            exit()

    def run_app(self):
        print("Welcome to the banking system, please log in first.\n")
        self.login()

    def login(self):
        counter = 3
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if username in self.system and self.system[username][0] == password:
            print("\nYou have now logged in, ", username)
            if self.system[username][1] == "customer":
                self.CustomerDriver(username)
            elif self.system[username][1] == "admin":
                self.AdminDriver()
            else:
                exit()
        else:
            print("Login incorrect")
            if counter > 0:
                counter -= 1
                print("Try Again! " + str(counter) + " tries Remaining")
                self.login()
            else:
                print("Out of Tries")
                exit()

    def AdminDriver(self):
        print("\n\nPlease Select an option :")
        print("  1- Customer Summary")
        print("  2- Financial Forecast")
        print("  3- Transfer Money - GUI")
        print("  4- Account Management - GUI")
        print("  0- Exit")
        try:
            option = int(input("\nEnter a number to select your option : "))
        except:
            print("Input Integer Only...")
            self.AdminDriver()
        if option == 1:
            self.CustomerSummary()
            self.AdminDriver()
        elif option == 2:
            self.FinancialForecast()
            self.AdminDriver()
        elif option == 3:
            self.TransferMoney()
            self.AdminDriver()
        elif option == 4:
            self.AccountManagement()
            self.AdminDriver()
        elif option == 0:
            exit()
        else:
            print("Invalid Input !")
            self.AdminDriver()

    def CustomerSummary(self):
        accounts = self.system
        for data in accounts:
            if accounts[data][1] == "customer":
                user = accounts[data][3]
                print("\nName : ", data)
                print("Address : ", accounts[data][2])
                print("---Accounts---")
                count = 1
                for acc in user:
                    if acc.startswith("C"):
                        print(count, "-", " Current account")
                        print("Balance : £" + str(user[acc][1]))
                        print("Overdraft Limit : £" + str(user[acc][0]))
                    elif acc.startswith("S"):
                        print(count, "-", " Saving account")
                        print("Balance : £" + str(user[acc][1]))
                        print("Interest Rate : " + str(user[acc][0]) + "%")
                    count += 1

    def FinancialForecast(self):
        accounts = self.system
        for data in accounts:
            if accounts[data][1] == "customer":
                user = accounts[data][3]
                print("\nName : ", data)
                total_amount = 0
                total_accounts = 0
                for acc in user:
                    Projected = 0
                    total_amount += user[acc][1]
                    total_accounts += 1
                    if acc.startswith("C"):
                        Projected = user[acc][1]
                    elif acc.startswith("S"):
                        Interest = ((user[acc][0]) / 100) * user[acc][1]
                        Interest *= 12
                        Projected = user[acc][1] + Interest
                print("Total Accounts : ", total_accounts)
                print("Total Amount : £"+ str(total_amount))
                print("Forecast : £" + str(Projected))

    def TransferMoney(self):
        Data = self.system
        accounts = Data
        Acc = {}
        for data in accounts:
            if accounts[data][1] == "customer":
                user = accounts[data][3]
                name = data
                temp_list = {}
                count = 1
                for acc in user:
                    if acc.startswith("C"):
                        temp_list[acc] = user[acc][1]
                    elif acc.startswith("S"):
                        temp_list[acc] = user[acc][1]
                    count += 1
                Acc[name] = temp_list
        print(Acc)

        def btn_clicked():
            try:
                amount = int(Amount.get())
                sendname = SenderName.get()
                sendtype = SenderType.get()
                sendindex = int(SenderIndex.get())
                rname = ReceiverName.get()
                rtype = ReceiverType.get()
                rindex = int(ReceiverIndex.get())
            except:
                print("Invalid Inputs")
                window.destroy()
                self.TransferMoney()

            if sendname in Acc and rname in Acc:
                sendtype1 = sendtype + str(sendindex)
                rtype1 = rtype + str(rindex)
                if sendtype1 in Acc[sendname] and rtype1 in Acc[rname]:
                    if Acc[sendname][sendtype1] >= amount:
                        (Acc[sendname][sendtype1]) -= amount
                        (Acc[rname][rtype1]) += amount
                        print(Acc)
                    else:
                        print("Not Possible, Not enough Funds Available")
            for name in Acc:
                if sendname in self.system:
                    if sendtype1 in self.system[sendname][3]:
                        self.system[sendname][3][sendtype1][1] = Acc[sendname][
                            sendtype1
                        ]
                        self.update_file()
                if rname in self.system:
                    if rtype1 in self.system[rname][3]:
                        self.system[rname][3][sendtype1][1] = Acc[rname][sendtype1]
                        self.update_file()

        window = tk.Tk()

        window.geometry("500x375")
        window.configure(bg="#d1ffec")
        canvas = Canvas(
            window,
            bg="#d1ffec",
            height=375,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"TransferPics/background.png")
        background = canvas.create_image(235.0, 148.0, image=background_img)

        entry0_img = PhotoImage(file=f"TransferPics/img_textBox0.png")
        entry0_bg = canvas.create_image(250.0, 287.5, image=entry0_img)

        Amount = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        Amount.place(x=180.0, y=275, width=140.0, height=23)

        entry1_img = PhotoImage(file=f"TransferPics/img_textBox1.png")
        entry1_bg = canvas.create_image(125.0, 112.5, image=entry1_img)

        SenderName = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        SenderName.place(x=30.0, y=100, width=190.0, height=23)

        entry2_img = PhotoImage(file=f"TransferPics/img_textBox2.png")
        entry2_bg = canvas.create_image(125.0, 162.5, image=entry2_img)

        SenderType = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        SenderType.place(x=30.0, y=150, width=190.0, height=23)

        entry3_img = PhotoImage(file=f"TransferPics/img_textBox3.png")
        entry3_bg = canvas.create_image(125.0, 212.5, image=entry3_img)

        SenderIndex = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        SenderIndex.place(x=30.0, y=200, width=190.0, height=23)

        entry4_img = PhotoImage(file=f"TransferPics/img_textBox4.png")
        entry4_bg = canvas.create_image(375.0, 112.5, image=entry4_img)

        ReceiverName = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        ReceiverName.place(x=280.0, y=100, width=190.0, height=23)

        entry5_img = PhotoImage(file=f"TransferPics/img_textBox5.png")
        entry5_bg = canvas.create_image(375.0, 162.5, image=entry5_img)

        ReceiverType = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        ReceiverType.place(x=280.0, y=150, width=190.0, height=23)

        entry6_img = PhotoImage(file=f"TransferPics/img_textBox6.png")
        entry6_bg = canvas.create_image(375.0, 212.5, image=entry6_img)

        ReceiverIndex = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        ReceiverIndex.place(x=280.0, y=200, width=190.0, height=23)

        img0 = PhotoImage(file=f"TransferPics/img0.png")
        SubmitButton = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat",
        )

        SubmitButton.place(x=191, y=305, width=120, height=28)

        window.resizable(False, False)
        window.mainloop()

    def AccountManagement(self):
        def delete_clicked():
            window.destroy()
            self.DeleteAccount()

        def add_clicked():
            window.destroy()
            self.AddAccount()

        window = Tk()

        window.geometry("400x130")
        window.configure(bg="#f1d1d1")
        canvas = Canvas(
            window,
            bg="#f1d1d1",
            height=130,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"ManagementPics/background.png")
        background = canvas.create_image(200.0, 41.5, image=background_img)

        img0 = PhotoImage(file=f"ManagementPics/img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=delete_clicked,
            relief="flat",
        )

        b0.place(x=229, y=62, width=132, height=43)

        img1 = PhotoImage(file=f"ManagementPics/img1.png")
        b1 = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=add_clicked,
            relief="flat",
        )

        b1.place(x=39, y=62, width=132, height=43)

        window.resizable(False, False)
        window.mainloop()

    def AddAccount(self):
        def btn_clicked():
            try:
                aname = entry0.get()
                atype = entry1.get()
            except:
                window.destroy()
                self.AddAccount()
            c = 0
            s = 0
            for name in self.system:
                if self.system[name][1] == "customer":
                    if name == aname:
                        for a in self.system[name][3]:
                            if a.startswith("C"):
                                print("current")
                                c+=1
                            if a.startswith("S"):
                                print("saving")
                                s+=1
                        if atype.startswith("C"):
                            if c == 0:
                                atype = atype+ str(c+1)
                            else:
                                print("Can not have more than 1 Current Account")
                        elif atype.startswith("S"):
                            atype = atype+ str(s+1)
                        
                        try:
                            print(atype)
                            self.system[name][3][atype] = [0,0]
                            self.update_file()
                        except:
                            print("Invalid Input")
                            window.destroy()
                            self.AddAccount()
                            


        window = Tk()
        window.geometry("400x225")
        window.configure(bg="#d1ffec")
        canvas = Canvas(
            window,
            bg="#d1ffec",
            height=225,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"ManagementPics/AddPics/background.png")
        background = canvas.create_image(199.5, 69.0, image=background_img)

        entry0_img = PhotoImage(file=f"ManagementPics/AddPics/img_textBox0.png")
        entry0_bg = canvas.create_image(200.0, 87.5, image=entry0_img)

        entry0 = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        entry0.place(x=105.0, y=75, width=190.0, height=23)

        entry1_img = PhotoImage(file=f"ManagementPics/AddPics/img_textBox1.png")
        entry1_bg = canvas.create_image(200.0, 137.5, image=entry1_img)

        entry1 = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        entry1.place(x=105.0, y=125, width=190.0, height=23)

        img0 = PhotoImage(file=f"ManagementPics/AddPics/img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat",
        )

        b0.place(x=175, y=175, width=50, height=25)

        window.resizable(False, False)
        window.mainloop()

    def DeleteAccount(self):
        
        def btn_clicked():
            try:
                aname = entry0.get()
                atype = entry1.get()
                aindex = int(entry2.get())
            except:
                window.destroy()
                self.DeleteAccount()
            
            for name in self.system:
                typename = atype+str(aindex)
                if self.system[aname][1] == "customer":
                    if name == aname:
                        if  len(self.system[name][3]) > 1:
                            if typename in self.system[aname][3]:
                                print(self.system[name][3][typename])
                                self.system[name][3].pop(typename)
                                self.update_file()
                            else:
                                print("Account Does not exist")
                                window.destroy()
                                self.DeleteAccount()
                        else:
                            print("Can not delete Last Account")
                            window.destroy()
                            self.DeleteAccount()

        window = Tk()
        window.geometry("400x276")
        window.configure(bg="#d1ffec")
        canvas = Canvas(
            window,
            bg="#d1ffec",
            height=276,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"ManagementPics/DeletePics/background.png")
        background = canvas.create_image(197.5, 98.0, image=background_img)

        entry0_img = PhotoImage(file=f"ManagementPics/DeletePics/img_textBox0.png")
        entry0_bg = canvas.create_image(198.0, 91.5, image=entry0_img)

        entry0 = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        entry0.place(x=103.0, y=79, width=190.0, height=23)

        entry1_img = PhotoImage(file=f"ManagementPics/DeletePics/img_textBox1.png")
        entry1_bg = canvas.create_image(198.0, 141.5, image=entry1_img)

        entry1 = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        entry1.place(x=103.0, y=129, width=190.0, height=23)

        entry2_img = PhotoImage(file=f"ManagementPics/DeletePics/img_textBox2.png")
        entry2_bg = canvas.create_image(198.0, 191.5, image=entry2_img)

        entry2 = Entry(bd=0, bg="#8dc8b2", highlightthickness=0)

        entry2.place(x=103.0, y=179, width=190.0, height=23)

        img0 = PhotoImage(file=f"ManagementPics/DeletePics/img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat",
        )

        b0.place(x=173, y=229, width=50, height=25)

        window.resizable(False, False)
        window.mainloop()

    def CustomerDriver(self, username):
        print("\n\nPlease Select an option :")
        print("  1- View Account")
        print("  2- View Summary")
        print("  3- Exit")
        try:
            option = int(input("\nEnter a number to select your option : "))
        except:
            print("Input Integer Only...")
            self.CustomerDriver(username)
        if option == 1:
            self.ViewAccount(username)
            self.CustomerDriver(username)
        elif option == 2:
            self.ViewSummary(username)
            self.CustomerDriver(username)
        elif option == 3:
            exit()
        else:
            print("Invalid Input !")
            self.CustomerDriver(username)

    def ViewAccount(self, username):
        accounts = self.system[username][3]
        print("\n--Accounts List--")
        count = 1
        val = []
        for acc in accounts:
            if acc.startswith("C"):
                print(count, "-", " Current account: £" + str(accounts[acc][1]))
                val.append(acc)
            elif acc.startswith("S"):
                print(count, "-", " Saving account: £" + str(accounts[acc][1]))
                val.append(acc)
            count += 1
        print("0 -  Go Back")
        try:
            choice = int(input("Enter a number to select your option : "))
        except:
            print("Input Integer Only...")
            self.ViewAccount(username)
        if choice == 0:
            return
        print("You selected ", choice)
        print("\nPlease select an option : ")
        print("  1- Deposit")
        print("  2- Withdraw")
        print("  3- Go Back")
        try:
            choice1 = int(input("Enter a number to select your option : "))
        except:
            print("Input Integer Only...")
            self.ViewAccount(username)
        if choice1 == 1:
            deposit = int(input("Enter amount to Deposit :  £"))
            accounts[val[choice - 1]][1] += deposit
            self.system[username][3] = accounts
            self.update_file()
            self.ViewAccount(username)
        elif choice1 == 2:
            withdraw = int(input("Enter amount to Withdraw : £"))
            if accounts[val[choice - 1]][1] >= withdraw:
                accounts[val[choice - 1]][1] -= withdraw
            else:
                print("Not Enough Amount in Account to Withdraw!")
            self.system[username][3] = accounts
            self.update_file()
            self.ViewAccount(username)
        elif choice1 == 3:
            choice = 0
            self.ViewAccount(username)
        else:
            print("Invalid Input !")
            self.ViewAccount(username)

    def ViewSummary(self, username):
        print("\n--Accounts Summary--")
        accounts = self.system[username][3]
        total_amount = 0
        total_accounts = 0
        for acc in accounts:
            total_amount += accounts[acc][1]
            total_accounts += 1
        address = self.system[username][2]
        print("Total Accounts : ", total_accounts)
        print("Total Amount : £"+str(total_amount))
        print("Address : ", address)

    def update_file(self):
        with open("data.txt", "w") as data:
            json.dump(self.system, data)
