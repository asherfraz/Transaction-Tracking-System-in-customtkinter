import customtkinter


def AddDel_Tab(self, parentHomeFrame):
    tabview_1 = customtkinter.CTkTabview(parentHomeFrame, width=900)
    tabview_1.pack(pady=10, padx=10)
    tab1_add = tabview_1.add("Add Transaction")
    tab1_delete = tabview_1.add("Delete Transaction")

    # ?############################################################################################
    # ? Add Transaction Tab
    # ?############################################################################################
    self.AddTransactionLabel = customtkinter.CTkLabel(
        tab1_add,
        text="Add Transaction",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="ew")
    # Name Label
    self.addnameLabel = customtkinter.CTkLabel(tab1_add, text="Product Name").grid(
        row=1, column=0, padx=20, pady=20, sticky="ew"
    )
    # Name Entry Field
    self.addnameEntry = customtkinter.CTkEntry(tab1_add, placeholder_text="Name")
    self.addnameEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
    # Price Label
    self.addpriceLabel = customtkinter.CTkLabel(tab1_add, text="Product Price").grid(
        row=2, column=0, padx=20, pady=20, sticky="ew"
    )
    # Price Entry Field
    self.addpriceEntry = customtkinter.CTkEntry(tab1_add, placeholder_text="Price")
    self.addpriceEntry.grid(
        row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew"
    )
    # Quantity Label
    self.addquantityLabel = customtkinter.CTkLabel(
        tab1_add, text="Product Quantity"
    ).grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    # Quantity Entry Field
    self.addquantityEntry = customtkinter.CTkEntry(
        tab1_add, placeholder_text="Quantity"
    )
    self.addquantityEntry.grid(
        row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew"
    )

    # save Button
    self.btnsave_AddTransaction = customtkinter.CTkButton(
        tab1_add,
        text="Save",
        hover_color="green",
        command=self.addTransactionData,
    ).grid(row=4, column=2, padx=20, pady=20, sticky="new")
    # Cancel Button
    self.btncancel_AddTransaction = customtkinter.CTkButton(
        tab1_add,
        text="Discard",
        command=self.cancelAddTransactionData,
    ).grid(row=4, column=3, padx=20, pady=20, sticky="new")

    # Previous Transaction Label
    self.addpreviouslytextLabel = customtkinter.CTkLabel(
        tab1_add,
        text="",
    )
    self.addpreviouslytextLabel.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
    self.addpreviouslyLabel = customtkinter.CTkLabel(tab1_add, text="")
    self.addpreviouslyLabel.grid(row=5, column=1, sticky="ew")

    # ?############################################################################################
    # ? Delete Transaction Tab
    # ?############################################################################################
    self.nameLabel = customtkinter.CTkLabel(
        tab1_delete,
        text="Delete Transaction",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="ew")
    # delIDLabel Label
    self.delIDLabel = customtkinter.CTkLabel(
        tab1_delete, text="Enter Product ID: "
    ).grid(row=1, column=0, padx=20, pady=20, sticky="ew")
    # delIDLabel Entry Field
    self.delIDEntry = customtkinter.CTkEntry(tab1_delete, placeholder_text="Product ID")
    self.delIDEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    # delIDLabel Label
    self.deletingRecordLabel0 = customtkinter.CTkLabel(tab1_delete, text="")
    self.deletingRecordLabel0.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    self.deletingRecordLabel1 = customtkinter.CTkLabel(tab1_delete, text="")
    self.deletingRecordLabel1.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

    # delete Button
    self.btndelete_DelTransaction = customtkinter.CTkButton(
        tab1_delete,
        text="Delete",
        hover_color="green",
        command=self.deltransactionID,
    ).grid(row=4, column=2, padx=20, pady=20, sticky="new")
    # Cancel Button
    self.btncancel_DelTransaction = customtkinter.CTkButton(
        tab1_delete,
        text="Cancel",
        command=self.discardDeleteID,
    ).grid(row=4, column=3, padx=20, pady=20, sticky="new")
