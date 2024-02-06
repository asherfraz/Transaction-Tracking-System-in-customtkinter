import customtkinter
from DatabaseHandler import DatabaseHandler


def ViewTab(self, parentThirdFrame):

    tabview_3 = customtkinter.CTkTabview(parentThirdFrame, width=900)
    tabview_3.pack(pady=10, padx=10)
    viewAll = tabview_3.add("View All Transactions")
    viewReport = tabview_3.add("View Transactions Report")

    # ?############################################################################################
    # ? View Transaction Tab
    # ?############################################################################################
    self.ViewTransactionTabLabel = customtkinter.CTkLabel(
        viewAll,
        text="View All",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).grid(row=0, column=0, padx=50, pady=15)

    self.ViewTotalTransactionsLabel = customtkinter.CTkLabel(
        viewAll,
        text="Total Earnings: ",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    )
    self.ViewTotalTransactionsLabel.grid(row=1, column=0, padx=20, pady=5)

    self.viewallScrollFrame = customtkinter.CTkScrollableFrame(
        viewAll,
        corner_radius=25,
        width=760,
        height=600,
        border_width=5,
        fg_color="lightgray",
    )
    self.viewallScrollFrame.grid(row=2, column=0, padx=30, pady=0, sticky="new")

    viewallRefresh(self)

    # ?############################################################################################
    # ? View Transaction Report Tab
    # ?############################################################################################
    self.ViewTransactionReportTabLabel = customtkinter.CTkLabel(
        viewReport,
        text="View Report\n\n\n\n\n\nComming Soon!",
        compound="left",
        font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
    ).pack(padx=50, pady=50)


def viewallRefresh(self):
    totalEarnings = 0
    data = DatabaseHandler.viewTransactionTable(self.dbConnection)

    for i, rc in enumerate(data):
        labels = [
            "Product ID :",
            "Product Name :",
            "Product Price :",
            "Product Quantity :",
            "DateTime :",
            " ",
        ]
        # print(f"\ni={i}")

        for j, label_text in enumerate(labels):
            # print(f"j={j}")
            # print(f"logic={i * len(labels) + j}")
            customtkinter.CTkLabel(
                self.viewallScrollFrame,
                text=label_text,
                compound="left",
                text_color="black",
                font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
            ).grid(row=i * len(labels) + j, column=0, padx=50, pady=3, sticky="new")

            if j == 0:  # for "Product ID ="
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=rc[0],
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j, column=1, padx=50, pady=3)
            elif j == 1:  # for "Product Name ="
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=rc[1],
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j, column=1, padx=50, pady=3)
            elif j == 2:  # for "Product Price ="
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=rc[2],
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j, column=1, padx=50, pady=3)
            elif j == 3:  # for "Product Quantity ="
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=rc[3],
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j, column=1, padx=50, pady=3)
            elif j == 4:  # for "Product Quantity ="
                # print(type(rc[2]))
                totalEarnings += rc[2] * rc[3]
                # print(f"TotalEarnings= {totalEarnings}")
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=rc[4],
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j, column=1, padx=50, pady=3)
                # Blank Line
                customtkinter.CTkLabel(
                    self.viewallScrollFrame,
                    text=" ",
                    text_color="black",
                    compound="left",
                    font=customtkinter.CTkFont(
                        "Times new roman", size=18, weight="bold"
                    ),
                ).grid(row=i * len(labels) + j + 1, column=1, padx=50, pady=3)

            self.ViewTotalTransactionsLabel.configure(
                text=f"Total Earnings: {totalEarnings}"
            )
