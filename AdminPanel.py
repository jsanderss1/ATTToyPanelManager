"""
Author: Sanders Lopez Quiroz
Date started: Mon,  09 Nov 2020
Version: 3.7
Purposes:
    - Create a basic GUI
    - Create the display loop.
    - Add a text box.
    - Add a button.
    - Add a check box.
    - Explain about pack().
    Reference: https://www.python-course.eu/python_tkinter.php
               https://www.youtube.com/watch?v=qwBZMUM9L_E
               https://www.w3schools.com/
               https://www.delftstack.com/howto/python-tkinter/how-to-clear-tkinter-text-box-widget/
               https://www.python.com/3
               https://www.doc.python.com/tkinter
               Andy Wicks videos
"""

import tkinter as tk                 # This has all the code library for GUIs.
import tkinter.font as font          # This is the fonts library.
from tkinter import messagebox       # This has the code for the message box.
from tkinter import ttk              # This the library I extracted the tree function from.
from Database import Database                   # This is database linking code is located.


class FirstWindow:

    def __init__(self, root, *args, **kwargs):

        self.root = root  # Main window for login
        self.var = tk.IntVar  # This is for tickbox.
        width = 490  # Global width size of the window.
        height = 300  # Global height size of the window.
        screen_width = self.root.winfo_screenwidth()  # Is for getting the screen width.
        screen_height = self.root.winfo_screenheight()  # Is for getting the screen height.
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(False, False)    # To prevent the resizability of the window.
        self.root.config(bg='white')    # This is for my white background.
        self.root.title("AAT Ltd Admin - Login")  # This is for naming the title of the window.
        self.root.iconphoto(True, tk.PhotoImage(file='Images/info.png'))  # This is for putting a
        # icon in the title bar.

        # Frame and Widgets
        self.frame = tk.Frame(root, bg='white',  width=450, height=290)

        self.lbl_font = font.Font(family='Sans', size='30',
                                  weight='bold')  # This is variable for the font that I used for
        # my fonts.

        self.image2 = tk.PhotoImage(file="Images/info1.png")
        self.lbl_text1 = tk.Label(self.frame, text='Login', font=self.lbl_font, fg='Black',
                                  bg='white')  # This is the title name label.
        self.lbl_text1.grid(row=0, column=1, columnspan=1, sticky=tk.N)
        self.lbl_text1["compound"] = tk.LEFT
        self.lbl_text1["image"] = self.image2

        self.lbl_text2 = tk.Label(self.frame, text='Username:', bg='white')  # These are
        # the label and textbox for the username.
        self.lbl_text2.grid(row=1, column=0, columnspan=1)

        self.entry_box_1 = tk.Entry(self.frame, width=25)
        self.entry_box_1.grid(row=1, column=1, columnspan=1)

        self.lbl_text3 = tk.Label(self.frame, text='Password:', bg='white')  # These are the
        # label and textbox for password.
        self.lbl_text3.grid(row=2, column=0, columnspan=1)

        self.entry_box_2 = tk.Entry(self.frame, width=25, show='*')
        self.entry_box_2.grid(row=2, column=1, columnspan=1)

        self.checkbutton1 = tk.Checkbutton(self.frame, text="Keep me signed in.",
                                           bg='white', relief=tk.FLAT)  # This is code for the checkbox.
        self.checkbutton1.grid(row=3, column=1)

        # This is my login button.
        self.button1 = tk.Button(self.frame, text="Login", fg='black', bg='lightgray',
                                 cursor='question_arrow', command=self.Authentication)
        self.button1.grid(row=4, column=0, columnspan=2, pady=10, padx=10 )

        # This is my clear button.
        self.button3 = tk.Button(self.frame, text="Clear", fg='black', bg='lightgray',
                                 cursor='question_arrow', command=self.Erase)
        self.button3.grid(row=4, column=1, columnspan=20, pady=10, padx=10)

        self.lbl_text4 = tk.Label(self.frame, text="© Copyright AAT Ltd Login Screen 2020", fg="Blue",
                                  bg="white")  # This is the copyright label.
        self.lbl_text4.grid(row=5, column=0, columnspan=10, pady=10)

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Erase(self):  # This is the function for clearing the text in the textbox.
        self.entry_box_1.delete(0, "end")
        self.entry_box_2.delete(0, "end")

    def Authentication(self):  # This is the function for credentials verification.

        username = self.entry_box_1.get()
        password = self.entry_box_2.get()

        if username == "" and password == "":
            messagebox.showinfo("AAT Ltd Info", "Not typing anything is not allowed.")

        elif username == "john" and password == "":
            messagebox.showinfo("ATT Ltd Info", "You did not input any password! Please enter password.")

        elif username == "john" and password == "123":
            self.display_new_window = tk.Toplevel(self.root)
            self.display_this = SecondWindow(self.display_new_window)
            self.hide_old_window = self.root.withdraw()

        else:
            messagebox.showinfo("ATT Ltd Info", "Username and Password are not correct.")


class SecondWindow:

    def __init__(self, root, *args, **kwargs):

        self.root = root   # Second window.
        self.root.title('AAT Ltd Management System')  # This is for my title of the program.

        # Navigation bar
        self.menu_bar1 = tk.Menu(self.root, bg='lightgray')
        # File menu bar
        function_menu1 = tk.Menu(self.menu_bar1, tearoff=0)
        function_menu1.add_command(label="Product", command=self.Swap2)
        function_menu1.add_command(label="Category", command=self.Swap1)
        function_menu1.add_separator()
        function_menu1.add_command(label="Logout", command=quit)
        self.menu_bar1.add_cascade(label="File", menu=function_menu1)

        # Help menu bar
        help_menu1 = tk.Menu(self.menu_bar1, tearoff=0)
        help_menu1.add_command(label="Help", command=self.Help)
        self.menu_bar1.add_cascade(label="Help", menu=help_menu1)

        # Quit menu bar
        quit_menu1 = tk.Menu(self.menu_bar1, tearoff=0)
        quit_menu1.add_command(label='Quit', command=self.Close)
        self.menu_bar1.add_cascade(label="Quit", menu=quit_menu1)
        self.root.config(menu=self.menu_bar1)

        width = 960  # Global width size of the window.
        height = 425  # Global height size of the window.
        screen_width = root.winfo_screenwidth()  # Is for getting the screen width.
        screen_height = root.winfo_screenheight()  # Is for getting the screen height.
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

       # self.Stock()

        # Database
        self.data = Database('Database/Database.db')

        # First window frame for Category
        self.main_frame1 = tk.Frame(self.root, bg='white')
        self.main_frame1.pack(fill='both', expand=1)

        self.frame2 = tk.Frame(self.main_frame1, bg='white', relief=tk.FLAT, padx=25, pady=10)
        self.frame2.pack()

        lbl_title1 = tk.Label(self.frame2, bg='white', text='Toy Category Management', font=('arial', 35, 'bold'))
        lbl_title1.pack()

        self.frame7 = tk.Frame(self.main_frame1, pady=50, bg='white', relief=tk.FLAT)
        self.frame7.pack(side=tk.BOTTOM)

        self.frame3 = tk.Frame(self.main_frame1, bg='white', relief=tk.FLAT)
        self.frame3.pack(side=tk.TOP)

        # Label frames
        label_frame1 = tk.LabelFrame(self.frame3, font=('arial', 11, 'bold'), text="Category List:", bg='white', bd=2, padx=10, pady=5)
        label_frame1.pack(padx=20, pady=10, side=tk.RIGHT)

        label_frame2 = tk.LabelFrame(self.frame3, font=('arial', 11, 'bold'), text="Maintain Category:", bg='white', bd=2, padx=10, pady=5)
        label_frame2.pack(padx=20, pady=10, side=tk.LEFT)

        # Scrollbar for category list box
        scrollbar = tk.Scrollbar(label_frame1)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Listbox for Category
        self.list1 = tk.Listbox(label_frame1, height=8, width=50, border=0, yscrollcommand=scrollbar.set)
        self.list1.grid(row=0, column=0)
        self.list1.bind('<<ListboxSelect>>', self.SelectedItem)
        scrollbar.config(command=self.list1.yview)

        # Entry boxes and labels for ID
        self.CategoryID2 = tk.StringVar()
        self.lbl_text19 = tk.Label(label_frame2, text='ID:', bg='white', )
        self.lbl_text19.grid(row=1, column=0, columnspan=1)
        self.entry_box_20 = tk.Entry(label_frame2, width=25, textvariable=self.CategoryID2)
        self.entry_box_20.grid(row=1, column=1, columnspan=1)

        # Entry boxes and labels for Name
        self.CategoryName = tk.StringVar()
        self.lbl_text21 = tk.Label(label_frame2, text='Name:', bg='white')
        self.lbl_text21.grid(row=2, column=0, columnspan=1)
        self.entry_box_22 = tk.Entry(label_frame2, width=25, textvariable=self.CategoryName)
        self.entry_box_22.grid(row=2, column=1, columnspan=1)

        # Entry boxes and labels for Hardness
        self.CategoryHardness = tk.StringVar()
        self.lbl_text23 = tk.Label(label_frame2, text='Toy Hardness:', bg='white')
        self.lbl_text23.grid(row=3, column=0, columnspan=1)
        self.entry_box_24 = tk.Entry(label_frame2, width=25, textvariable=self.CategoryHardness)
        self.entry_box_24.grid(row=3, column=1, columnspan=1)

        button_add2 = tk.Button(self.frame7, text='Save', command=self.Insert2, bg='lightgray',
                                 cursor='question_arrow')
        button_add2.grid(row=4, column=1, columnspan=1, padx=10)

        button_edit = tk.Button(self.frame7, text='Update', command=self.ListBoxUpdate, bg='lightgray',
                                   cursor='question_arrow')
        button_edit.grid(row=4, column=2, columnspan=1, padx=10)

        button_delete = tk.Button(self.frame7, text='Delete', command=self.DeleteListBox, bg='lightgray',
                                   cursor='question_arrow')
        button_delete.grid(row=4, column=3, columnspan=1, padx=10)

        button_clear = tk.Button(self.frame7, text='Clear', command=self.Erase2, bg='lightgray',
                                   cursor='question_arrow')
        button_clear.grid(row=4, column=4, columnspan=1, padx=10)

        button_product = tk.Button(self.frame7, text='Product', command=self.Swap2, bg='lightgray',
                                   cursor='question_arrow')
        button_product.grid(row=4, column=5, columnspan=1, padx=10)

        # Second window frame for Product
        self.main_frame4 = tk.Frame(self.root, bg='white')

        self.frame5 = tk.Frame(self.main_frame4, pady=1, bg='white', relief=tk.FLAT)
        self.frame5.pack()

        lbl_title2 = tk.Label(self.frame5, bg='white', text='Product Management', font=('arial', 35, 'bold'))
        lbl_title2.pack(side=tk.TOP)

        self.frame8 = tk.Frame(self.main_frame4, pady=40, bg='white', relief=tk.FLAT)
        self.frame8.pack(side=tk.BOTTOM)

        self.frame6 = tk.Frame(self.main_frame4, bg='white', relief=tk.FLAT)
        self.frame6.pack(side=tk.TOP)

        # Label frames
        label_frame4 = tk.LabelFrame(self.frame6, text="Product Table:", bg='white', font=('arial', 11, 'bold'), bd=2, padx=5, pady=5)
        label_frame4.pack(padx=15, pady=10, side=tk.RIGHT)

        label_frame5 = tk.LabelFrame(self.frame6, text="Maintain Product:", bg='white', font=('arial', 11, 'bold'), bd=2, padx=5, pady=5)
        label_frame5.pack(padx=15, pady=10, side=tk.LEFT)

        # Scrollbar for category list box
        scrollbar2 = tk.Scrollbar(label_frame4)
        scrollbar2.grid(row=0, column=1, sticky=tk.NS)

        # TreeView for Product
        self.tree2 = ttk.Treeview(label_frame4, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=7, yscrollcommand=scrollbar2.set)
        self.tree2.grid(row=0, column=0)

        scrollbar2.config(command=self.list1.yview)

        self.tree2.heading(1, text='ID')
        self.tree2.column(1, width=70)
        self.tree2.heading(2, text='Name')
        self.tree2.column(2, width=70)
        self.tree2.heading(3, text='CategoryID')
        self.tree2.column(3, width=85)
        self.tree2.heading(4, text='Weight')
        self.tree2.column(4, width=70)
        self.tree2.heading(5, text='ShippingPrice')
        self.tree2.column(5, width=70)
        self.tree2.heading(6, text='Price')
        self.tree2.column(6, width=100)
        self.tree2.heading(7, text='StockAmount')
        self.tree2.column(7, width=95)

        # Entry boxes and labels for ID
        self.ProductID = tk.StringVar()
        self.lbl_text7 = tk.Label(label_frame5, text='ID:', bg='white')
        self.lbl_text7.grid(row=1, column=0, columnspan=1)
        self.entry_box_8 = tk.Entry(label_frame5, width=25, textvariable=self.ProductID)
        self.entry_box_8.grid(row=1, padx=5, column=1, columnspan=1)

        # Entry boxes and labels for Name
        self.ProductName = tk.StringVar()
        self.lbl_text9 = tk.Label(label_frame5, text='Name:', bg='white')
        self.lbl_text9.grid(row=2, column=0, columnspan=1)
        self.entry_box_10 = tk.Entry(label_frame5, width=25, textvariable=self.ProductName)
        self.entry_box_10.grid(row=2, column=1, columnspan=1)

        # Entry boxes and labels for Category
        self.CategoryID1 = tk.StringVar()
        self.lbl_text11 = tk.Label(label_frame5, text='Category ID:', bg='white')
        self.lbl_text11.grid(row=3, column=0, columnspan=1)
        self.entry_box_12 = tk.Entry(label_frame5, width=25, textvariable=self.CategoryID1)
        self.entry_box_12.grid(row=3, column=1, columnspan=1)

        # Entry boxes and labels for weight
        self.ProductWeight = tk.StringVar()
        self.lbl_text13 = tk.Label(label_frame5, text='Weight:', bg='white')
        self.lbl_text13.grid(row=4, column=0, columnspan=1)
        self.entry_box_14 = tk.Entry(label_frame5, width=25, textvariable=self.ProductWeight)
        self.entry_box_14.grid(row=4, column=1, columnspan=1)

        # Entry boxes and labels for shipping price
        self.ProductShippingCharge = tk.StringVar()
        self.lbl_text17 = tk.Label(label_frame5, text='Shipping Price:', bg='white')
        self.lbl_text17.grid(row=5, column=0, columnspan=1)
        self.entry_box_18 = tk.Entry(label_frame5, width=25, textvariable=self.ProductShippingCharge)
        self.entry_box_18.grid(row=5, column=1, columnspan=1)

        # Entry boxes and labels for price
        self.ProductPrice = tk.StringVar()
        self.lbl_text15 = tk.Label(label_frame5, text='Price:', bg='white')
        self.lbl_text15.grid(row=6, column=0, columnspan=1)
        self.entry_box_16 = tk.Entry(label_frame5, width=25, textvariable=self.ProductPrice)
        self.entry_box_16.grid(row=6, column=1, columnspan=1)

        # Entry boxes and labels for stock amount
        self.ProductStockAmount = tk.StringVar()
        self.lbl_text25 = tk.Label(label_frame5, text='Stock Amount:', bg='white')
        self.lbl_text25.grid(row=7, column=0, columnspan=1)
        self.entry_box_26 = tk.Entry(label_frame5, width=25, textvariable=self.ProductStockAmount)
        self.entry_box_26.grid(row=7, column=1, columnspan=1)

        # Buttons for product management
        button_add = tk.Button(self.frame8, text='Save', bg='lightgray',
                                 cursor='question_arrow', command=self.Insert1)
        button_add.grid(row=8, column=1, columnspan=1, padx=10)

        button_edit = tk.Button(self.frame8, text='Edit Selected', bg='lightgray',
                                 cursor='question_arrow', command=self.getrow)
        button_edit.grid(row=8, column=2, columnspan=1, padx=10)

        button_delete = tk.Button(self.frame8, text='Delete', bg='lightgray',
                                 cursor='question_arrow', command=self.DeleteTreeViewData)
        button_delete.grid(row=8, column=3, columnspan=1, padx=10)

        button_clear = tk.Button(self.frame8, text='Clear', bg='lightgray',
                                 cursor='question_arrow', command=self.Erase3)
        button_clear.grid(row=8, column=4, columnspan=1, padx=10)

        button_category = tk.Button(self.frame8, text='Category', bg='lightgray',
                                   cursor='question_arrow', command=self.Swap1)
        button_category.grid(row=8, column=6, columnspan=1, padx=10)

        button_display2 = tk.Button(self.frame8, text='Show', bg='lightgray',
                                    cursor='question_arrow', command=self.PopulateTreeView)
        button_display2.grid(row=8, column=5, columnspan=1, padx=10)

        button_export = tk.Button(self.frame8, text='Save File', bg='lightgray',
                                    cursor='question_arrow',)
        button_export.grid(row=8, column=7, columnspan=1, padx=10)

        self.PopulateListBox()

        self.PopulateTreeView()

    # This swaping my frame to category management page
    def Swap1(self):
        self.main_frame4.forget()
        self.main_frame1.pack(fill='both', expand=1)

    # This swaping my frame to product management page
    def Swap2(self):
        self.main_frame1.forget()
        self.main_frame4.pack(fill='both', expand=1)

    def Erase2(self):  # This is the function for clearing the text in the textbox.
        self.entry_box_20.delete(0, "end")
        self.entry_box_22.delete(0, "end")
        self.entry_box_24.delete(0, "end")

    def Erase3(self):  # This is the function for clearing the text in the textbox.
        self.entry_box_8.delete(0, "end")
        self.entry_box_10.delete(0, "end")
        self.entry_box_12.delete(0, "end")
        self.entry_box_14.delete(0, "end")
        self.entry_box_16.delete(0, "end")
        self.entry_box_18.delete(0, "end")
        self.entry_box_26.delete(0, "end")

    # This for inserting data to database for product_category table
    def Insert2(self):

        self.data.insert2(self.CategoryName.get(), self.CategoryHardness.get())

        self.list1.delete(0, tk.END)
        display = self.data.fetch()

        for row in display:
            self.list1.insert(tk.END, row)
            self.PopulateListBox()

    # This for inserting data to database for category table
    def Insert1(self):
        self.data.insert(self.ProductName.get(), self.CategoryID1.get(), self.ProductWeight.get(), self.ProductPrice.get(), self.ProductShippingCharge.get(), self.ProductStockAmount.get())

        # for item in self.tree2.selection():
        #     self.tree2.set(item, "")
        #     self.tree2.delete(item)
        #     self.PopulateTreeView()

    # This for showing data from the database to the treeview
    def PopulateTreeView(self):
        #self.tree2.delete(0, tk.END)
        display = self.data.fetch()

        for row in display:
            self.tree2.insert("", tk.END, values=row)

    # This for showing data from the database to the treeview
    def PopulateListBox(self):
        self.list1.delete(0, tk.END)

        for row in self.data.fetch2():
            self.list1.insert(tk.END, row, str(""))

    def DeleteListBox(self):
        if (len(self.CategoryID2.get()) !=0):
            self.data.remove2(selected_item[0])
            self.Erase3()
            self.PopulateListBox()

    # This is for deleting data from my product table
    def DeleteTreeViewData(self):
        erase = self.tree2.selection()

        for item in erase:
            self.data.remove(self.tree2.set(item, "#1"), )
            self.tree2.delete(item)

    def getrow(self):
        content_row = self.tree2.focus()
        contents = self.tree2.item(content_row)
        row = contents['values']
        self.ProductID.set(row[0])
        self.ProductName.set(row[1])
        self.CategoryID1.set(row[2])
        self.ProductWeight.set(row[3])
        self.ProductShippingCharge.set(row[4])
        self.ProductPrice.set(row[5])
        self.ProductStockAmount.set(row[6])

    # This for selecting rows from the listbox to display in the entry boxes
    def SelectedItem(self, event):
        global selected_item

        index = self.list1.curselection()[0]
        selected_item = self.list1.get(index)

        self.entry_box_20.delete(0, tk.END)
        self.entry_box_20.insert(tk.END, selected_item[0])

        self.entry_box_22.delete(0, tk.END)
        self.entry_box_22.insert(tk.END, selected_item[1])

        self.entry_box_24.delete(0, tk.END)
        self.entry_box_24.insert(tk.END, selected_item[2])

    # This for updateing list box for category
    def ListBoxUpdate(self):
        if (len(self.CategoryID2.get()) !=0):
            #print("selected_item[0]", selected_item[self.data])
            self.data.remove2(selected_item[0])

        if (len(self.CategoryID2.get()) != 0):
            self.data.insert2(self.CategoryName.get(), self.CategoryHardness.get())
            self.list1.delete(0, tk.END)
            self.list1.insert(tk.END, (self.CategoryID2.get(), self.CategoryName.get(), self.CategoryHardness.get()))
            self.PopulateListBox()

    # This function is popping a message box where is ask you to close it or not
    def Close(self, *args):

        close = tk.messagebox.askyesno("Product Management System", "Are you sure. Do you want to close this window?")
        if close > 0:
            self.root.destroy()
        return

    def Help(self):
        tk.messagebox.askokcancel("Help", "This is the help page.")

   # def Stock(self):
      #  for ro in self.data.stock():
      #      messagebox.showinfo("Stock", f"self.ProductID{ro[0]}, \n self.ProductName{ro[1]}, \n are low in stock")

    #def SaveFile(self):
        #for item in self.data.save():
            #row = item[0], item[1], item[2], item[3], item[5], item[6]

            #with open('AATManagementSystemLog.csv', 'a') as f:
                #w=csv.writer(f, dialet='exel')
                #w.writerow(row)


if __name__ == "__main__":
    root = tk.Tk()
    program = FirstWindow(root)
    root.mainloop()
