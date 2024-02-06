import customtkinter
from DatabaseHandler import DatabaseHandler
from components.MessageBox import (
    show_thanks,
    show_error,
)


def SearchUpdateTab(self, parentSecondFrame):
    tabview_2 = customtkinter.CTkTabview(parentSecondFrame, width=900)
    tabview_2.pack(pady=10, padx=10)
    searchTab = tabview_2.add("Search Transaction")
    updateTab = tabview_2.add("Update Transaction")

    # ?############################################################################################
    # ? Search Transaction Tab
    # ?############################################################################################
    self.SearchTabLabel = customtkinter.CTkLabel(
        searchTab,
        text="Search Transtions",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0, padx=50, pady=25)

    # ? Frame 1 - Search By Id
    self.SearchFrame1 = customtkinter.CTkScrollableFrame(
        searchTab,
        corner_radius=25,
        width=760,
        height=250,
        border_width=5,
    )
    self.SearchFrame1.grid(row=1, column=0, padx=30, pady=5, sticky="new")
    # inner Frame
    self.SearchbyIdLabel = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="Search Transtion by Id:",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0)
    self.SearchbyIdEntryLabel = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="Enter Product Id: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=1, column=0, padx=10, pady=5, sticky="new")

    self.SearchbyIdEntry = customtkinter.CTkEntry(
        self.SearchFrame1, placeholder_text="Product ID"
    )
    self.SearchbyIdEntry.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    self.SearchbyIdButton = customtkinter.CTkButton(
        self.SearchFrame1, text="Search", command=self.SearchByID1
    ).grid(row=1, column=2, padx=10, pady=5, sticky="new")

    # Configure Search Records
    # ID
    self.SearchedProductId0 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductId0.grid(row=2, column=0, padx=10, pady=5, sticky="new")
    self.SearchedProductId1 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductId1.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    # NAme
    self.SearchedProductName0 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductName0.grid(row=3, column=0, padx=10, pady=5, sticky="new")
    self.SearchedProductName1 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductName1.grid(row=3, column=1, padx=10, pady=5, sticky="new")

    # Price
    self.SearchedProductPrice0 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductPrice0.grid(row=4, column=0, padx=10, pady=5, sticky="new")
    self.SearchedProductPrice1 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductPrice1.grid(row=4, column=1, padx=10, pady=5, sticky="new")

    # Quantity
    self.SearchedProductQuantity0 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductQuantity0.grid(row=5, column=0, padx=10, pady=5, sticky="new")
    self.SearchedProductQuantity1 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductQuantity1.grid(row=5, column=1, padx=10, pady=5, sticky="new")

    # DateTime
    self.SearchedProductDateTime0 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductDateTime0.grid(row=6, column=0, padx=10, pady=5, sticky="new")
    self.SearchedProductDateTime1 = customtkinter.CTkLabel(
        self.SearchFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.SearchedProductDateTime1.grid(row=6, column=1, padx=10, pady=5, sticky="new")

    # ? Frame 2 - Search By Name
    self.SearchFrame2 = customtkinter.CTkScrollableFrame(
        searchTab,
        corner_radius=25,
        width=760,
        height=250,
        border_width=5,
    )
    self.SearchFrame2.grid(row=7, column=0, padx=30, pady=5, sticky="new")
    # inner Frame
    self.SearchbyNameLabel = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="Search Transtion by Name:",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0)
    self.SearchbyNameEntryLabel = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="Enter Product Name: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=1, column=0, padx=10, pady=5, sticky="new")

    self.SearchbyNameEntry = customtkinter.CTkEntry(
        self.SearchFrame2, placeholder_text="Product Name"
    )
    self.SearchbyNameEntry.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    self.SearchbyNameButton = customtkinter.CTkButton(
        self.SearchFrame2, text="Search", command=self.SearchByName1
    ).grid(row=1, column=2, padx=10, pady=5, sticky="new")

    # Configure Search Records
    # ID
    self.Searched1ProductId0 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductId0.grid(row=2, column=0, padx=10, pady=5, sticky="new")
    self.Searched1ProductId1 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductId1.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    # NAme
    self.Searched1ProductName0 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductName0.grid(row=3, column=0, padx=10, pady=5, sticky="new")
    self.Searched1ProductName1 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductName1.grid(row=3, column=1, padx=10, pady=5, sticky="new")

    # Price
    self.Searched1ProductPrice0 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductPrice0.grid(row=4, column=0, padx=10, pady=5, sticky="new")
    self.Searched1ProductPrice1 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductPrice1.grid(row=4, column=1, padx=10, pady=5, sticky="new")

    # Quantity
    self.Searched1ProductQuantity0 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductQuantity0.grid(row=5, column=0, padx=10, pady=5, sticky="new")
    self.Searched1ProductQuantity1 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductQuantity1.grid(row=5, column=1, padx=10, pady=5, sticky="new")

    # DateTime
    self.Searched1ProductDateTime0 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductDateTime0.grid(row=6, column=0, padx=10, pady=5, sticky="new")
    self.Searched1ProductDateTime1 = customtkinter.CTkLabel(
        self.SearchFrame2,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.Searched1ProductDateTime1.grid(row=6, column=1, padx=10, pady=5, sticky="new")

    # ?############################################################################################
    # ? Update Transaction Tab
    # ?############################################################################################
    self.UpdateTabLabel = customtkinter.CTkLabel(
        updateTab,
        text="Update Transtions",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0, padx=50, pady=25)

    # ? Frame 1 - Update By Id
    self.UpdateFrame1 = customtkinter.CTkScrollableFrame(
        updateTab,
        corner_radius=25,
        width=760,
        height=350,
        border_width=5,
    )
    self.UpdateFrame1.grid(row=1, column=0, padx=30, pady=5, sticky="new")
    # inner Frame
    self.UpdatebyIdLabel = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Update Transtion by Id:",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0)
    self.UpdatebyIdEntryLabel = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Enter Product Id: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=1, column=0, padx=10, pady=5, sticky="new")

    self.UpdatebyIdEntry = customtkinter.CTkEntry(
        self.UpdateFrame1,
        placeholder_text="Product ID",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatebyIdEntry.grid(row=1, column=1, padx=10, pady=5, sticky="new")

    # search
    self.UpdatebyIdButton = customtkinter.CTkButton(
        self.UpdateFrame1, text="Search", command=self.UpdateByID1
    ).grid(row=1, column=2, padx=10, pady=5, sticky="new")

    # Configure Update Records
    # ID
    self.UpdatedProductId0 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Product ID: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductId0.grid(row=2, column=0, padx=10, pady=5, sticky="new")
    self.UpdatedProductId1 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductId1.grid(row=2, column=1, padx=10, pady=5, sticky="new")

    # NAme
    self.UpdatedProductName0 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Product Name: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductName0.grid(row=3, column=0, padx=10, pady=5, sticky="new")
    self.UpdatedProductName1 = customtkinter.CTkEntry(
        self.UpdateFrame1,
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductName1.grid(row=3, column=1, padx=10, pady=5, sticky="new")

    # Price
    self.UpdatedProductPrice0 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Product Price: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductPrice0.grid(row=4, column=0, padx=10, pady=5, sticky="new")
    self.UpdatedProductPrice1 = customtkinter.CTkEntry(
        self.UpdateFrame1,
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductPrice1.grid(row=4, column=1, padx=10, pady=5, sticky="new")

    # Quantity
    self.UpdatedProductQuantity0 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Product Quantity: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductQuantity0.grid(row=5, column=0, padx=10, pady=5, sticky="new")
    self.UpdatedProductQuantity1 = customtkinter.CTkEntry(
        self.UpdateFrame1,
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductQuantity1.grid(row=5, column=1, padx=10, pady=5, sticky="new")

    # DateTime
    self.UpdatedProductDateTime0 = customtkinter.CTkLabel(
        self.UpdateFrame1,
        text="Product DateTime: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductDateTime0.grid(row=6, column=0, padx=10, pady=5, sticky="new")
    self.UpdatedProductDateTime1 = customtkinter.CTkEntry(
        self.UpdateFrame1,
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.UpdatedProductDateTime1.grid(row=6, column=1, padx=10, pady=5, sticky="new")

    # Update
    self.UpdateButton = customtkinter.CTkButton(
        self.UpdateFrame1, text="Update", command=self.Update
    ).grid(row=7, column=2, padx=10, pady=5, sticky="new")

    # Cancel
    self.UpdateCancelButton = customtkinter.CTkButton(
        self.UpdateFrame1, text="Cancel", command=self.UpdateCancel
    ).grid(row=7, column=3, padx=10, pady=5, sticky="new")


def UpdatingData(self):
    id = self.UpdatedProductId1.cget("text")
    name = self.UpdatedProductName1.get()
    price = self.UpdatedProductPrice1.get()
    quantity = self.UpdatedProductQuantity1.get()
    dt = self.UpdatedProductDateTime1.get()
    data_list = [id, name, price, quantity, dt]
    if not (
        self.validate_String(name)
        and self.validate_Number(price)
        and self.validate_Number(quantity)
    ):
        show_error("Error!", "Enter valid data in Product Name, Price, and Quantity!")
        return

    updatingDataFlag = DatabaseHandler.updateTransactionbyID(
        self.dbConnection, data_list
    )
    if updatingDataFlag:
        show_thanks("Done", "Record Updated Successfully!")
    else:
        show_error(
            "Database Error!",
            "Record updating failed, Please try again later!!!",
        )


def UpdateByID(self):
    id = self.UpdatebyIdEntry.get()
    # self.UpdatebyIdEntry.configure(state="disabled")
    # checking entry data
    if not id:
        show_error("Error!", "Enter valid Product Id to Search.")
        return
    searchedRecord = DatabaseHandler.viewTransactionbyID(self.dbConnection, id)

    if not searchedRecord:
        show_error("Done", "No Record Found!")
        return

    # clear existing data
    self.UpdatedProductName1.delete(0, customtkinter.END)
    self.UpdatedProductPrice1.delete(0, customtkinter.END)
    self.UpdatedProductQuantity1.delete(0, customtkinter.END)
    self.UpdatedProductDateTime1.delete(0, customtkinter.END)

    # Configure
    searchedRecord = searchedRecord[0]
    # ID
    # self.UpdatedProductId0.configure(text="")
    self.UpdatedProductId1.configure(text=searchedRecord[0])
    # Name
    # self.UpdatedProductName0.configure(text="")
    self.UpdatedProductName1.insert(0, f"{searchedRecord[1]}")
    # Price
    # self.UpdatedProductPrice0.configure(text="")
    self.UpdatedProductPrice1.insert(0, f"{searchedRecord[2]}")
    # Quantity
    # self.UpdatedProductQuantity0.configure(text="")
    self.UpdatedProductQuantity1.insert(0, f"{searchedRecord[3]}")
    # DateTime
    # self.UpdatedProductDateTime0.configure(text="")
    self.UpdatedProductDateTime1.insert(0, f"{searchedRecord[4]}")

    show_thanks("Done", "Record Found Successfully!")


def SearchByID(self):
    id = self.SearchbyIdEntry.get()
    # checking entry data
    if not id:
        show_error("Error!", "Enter valid Product Id to Search.")
        return
    searchedRecord = DatabaseHandler.viewTransactionbyID(self.dbConnection, id)

    if not searchedRecord:
        show_error("Done", "No Record Found!")
        return

    # Configure
    searchedRecord = searchedRecord[0]
    # ID
    self.SearchedProductId0.configure(text="Product ID: ")
    self.SearchedProductId1.configure(text=searchedRecord[0])
    # Name
    self.SearchedProductName0.configure(text="Product Name: ")
    self.SearchedProductName1.configure(text=searchedRecord[1])
    # Price
    self.SearchedProductPrice0.configure(text="Product Price: ")
    self.SearchedProductPrice1.configure(text=searchedRecord[2])
    # Quantity
    self.SearchedProductQuantity0.configure(text="Product Quantity: ")
    self.SearchedProductQuantity1.configure(text=searchedRecord[3])
    # DateTime
    self.SearchedProductDateTime0.configure(text="Product DateTime: ")
    self.SearchedProductDateTime1.configure(text=searchedRecord[4])

    show_thanks("Done", "Record Found Successfully!")


def SearchByName(self):
    id = self.SearchbyNameEntry.get()
    # checking entry data
    if not id:
        show_error("Error!", "Enter valid Product Name to Search.")
        return

    searchedRecord = DatabaseHandler.viewTransactionbyName(self.dbConnection, id)

    if not searchedRecord:
        show_error("Done", "No Record Found!")
        return

    # Configure
    searchedRecord = searchedRecord[0]
    # ID
    self.Searched1ProductId0.configure(text="Product ID: ")
    self.Searched1ProductId1.configure(text=searchedRecord[0])
    # Name
    self.Searched1ProductName0.configure(text="Product Name: ")
    self.Searched1ProductName1.configure(text=searchedRecord[1])
    # Price
    self.Searched1ProductPrice0.configure(text="Product Price: ")
    self.Searched1ProductPrice1.configure(text=searchedRecord[2])
    # Quantity
    self.Searched1ProductQuantity0.configure(text="Product Quantity: ")
    self.Searched1ProductQuantity1.configure(text=searchedRecord[3])
    # DateTime
    self.Searched1ProductDateTime0.configure(text="Product DateTime: ")
    self.Searched1ProductDateTime1.configure(text=searchedRecord[4])

    show_thanks("Done", "Record Found Successfully!")
