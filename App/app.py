import customtkinter
from components.MessageBox import (
    exit_application,
    show_thanks,
    show_error,
    show_delete_warning,
)
import os
import sqlite3
import datetime
from pages.helpTab import helpTab
from pages.ViewTab import ViewTab, viewallRefresh
from pages.AddDel_Tab import AddDel_Tab
from pages.SearchUpdate_Tab import (
    SearchUpdateTab,
    SearchByID,
    SearchByName,
    UpdateByID,
    UpdatingData,
)
from DatabaseHandler import DatabaseHandler


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Sfotware Start Time
        # self.currentdatetime = self.update_time()
        print("Start Time: " + self.update_time() + "\n")
        # Connect Database
        self.database()
        # Visible Application Frame
        self.AppFrame()

    def database(self):
        # Sqlite3 Database Connection
        try:
            DB_PATH = os.path.join(
                os.path.dirname(__file__), "./database/Transactions.db"
            )

            if os.path.exists(DB_PATH):
                self.dbConnection = DatabaseHandler.DatabaseConnect(DB_PATH)
                print("Database connected already exists!")
            else:
                self.dbConnection = DatabaseHandler.DatabaseConnect(DB_PATH)
                print("Database created and connected!")
            # Create Transactions Table
            DatabaseHandler.createTransactionTable(self.dbConnection)
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def AppFrame(self):
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # *############################################################################################
        # ? left-side navigation frame
        # *############################################################################################
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="Al Syed Stationary Management",
            compound="left",
            font=customtkinter.CTkFont("Times new roman", size=18, weight="bold"),
        )
        self.navigation_frame_label.grid(
            row=0, column=0, padx=20, pady=20, sticky="new"
        )

        # now = datetime.datetime.now()
        # self.currentdatetime = now.strftime("%d %B, %Y, %I:%M:%S %p")

        self.date = customtkinter.CTkLabel(
            self.navigation_frame,
            text=self.update_time,
            corner_radius=10,
            font=customtkinter.CTkFont("Times new roman", size=12, weight="bold"),
        )
        self.date.grid(row=1, column=0)

        self.seperator = customtkinter.CTkLabel(
            self.navigation_frame,
            text="======================================",
            corner_radius=10,
            font=customtkinter.CTkFont("Times new roman", size=12, weight="bold"),
        )
        self.seperator.grid(row=2, column=0)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=5,
            height=40,
            border_spacing=10,
            text="Add / Delete",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=3, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=5,
            height=40,
            border_spacing=10,
            text="Search / Update",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.frame_2_button_event,
        )
        self.frame_2_button.grid(row=4, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=5,
            height=40,
            border_spacing=10,
            text="View",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.frame_3_button_event,
        )
        self.frame_3_button.grid(row=5, column=0, sticky="new")

        self.frame_4_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=5,
            height=40,
            border_spacing=10,
            text="Help",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.frame_4_button_event,
        )
        self.frame_4_button.grid(row=6, column=0, sticky="new")

        # self.frame_5_button = customtkinter.CTkButton(
        #     self.navigation_frame,
        #     corner_radius=5,
        #     height=40,
        #     border_spacing=10,
        #     text="Help",
        #     fg_color="transparent",
        #     text_color=("gray10", "gray90"),
        #     hover_color=("gray70", "gray30"),
        #     anchor="w",
        #     command=self.frame_5_button_event,
        # )
        # self.frame_5_button.grid(row=4, column=0, sticky="new")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # exit Button
        self.btnExitApplication = customtkinter.CTkButton(
            self.navigation_frame,
            text="Exit",
            hover_color="#FF0000",
            command=self.exit_application,
        )
        self.btnExitApplication.grid(column=0, padx=20, pady=20, sticky="s")

        # *############################################################################################
        # ? create Navigation Frame 1 - Add/Delete Transaction
        # *############################################################################################
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(0, weight=1)

        # AddDel_Tab.py - (Add , Delete Transactions)
        AddDel_Tab(self, self.home_frame)

        # *############################################################################################
        # ? Navigation Frame 2 - Search/Update
        # *############################################################################################
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.second_frame.grid_columnconfigure(0, weight=1)

        # SearchUpdateTab.py - Search & update Functionality
        SearchUpdateTab(self, self.second_frame)
        # *############################################################################################
        # ? Navigation Frame 3 - View
        # *############################################################################################
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.third_frame.grid_columnconfigure(0, weight=1)

        # ViewTab.py - View Transactions
        ViewTab(self, self.third_frame)

        # *############################################################################################
        # ? Navigation Frame 4 - Help
        # *############################################################################################
        self.fourth_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.fourth_frame.grid_columnconfigure(0, weight=1)

        # helpTab.py - (Help, Licence, Developer)
        helpTab(self.fourth_frame)

        # *############################################################################################
        # ? Navigation Frama 5 -
        # *############################################################################################
        # self.fifth_frame = customtkinter.CTkFrame(
        #     self, corner_radius=0, fg_color="transparent"
        # )
        # self.fifth_frame.grid_columnconfigure(0, weight=1)

        # select default frame
        self.select_frame_by_name("home")

    # *############################################################################################
    # ? Frame Selecting Function
    # *############################################################################################
    def select_frame_by_name(self, name):
        # set button color for selected button
        # Add / Delete
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        # Search / Update
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent"
        )
        # View
        self.frame_3_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_3" else "transparent"
        )
        # Help
        self.frame_4_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_4" else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def exit_application(self):
        print(">>>: Exiting Application!")
        exit_application(self)

    def validate_Number(self, input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False

    def validate_String(self, input_string):
        # if all(char.isalnum() or char.isspace() for char in input_string):
        if all(
            char.isalnum() or char.isspace() or not char.isprintable()
            for char in input_string
        ):
            print(input_string)
            return True
        else:
            return False

    def addTransactionData(self):
        transactionName = self.addnameEntry.get()
        transactionPrice = self.addpriceEntry.get()
        transactionQuantity = self.addquantityEntry.get()

        self.validate_String(transactionName)

        if not (
            self.validate_String(transactionName)
            and self.validate_Number(transactionPrice)
            and self.validate_Number(transactionQuantity)
        ):
            show_error(
                "Error!", "Enter valid data in Product Name, Price, and Quantity!"
            )
            return

        self.addpreviouslytextLabel.configure(text="Previous Transaction: ")
        self.addpreviouslyLabel.configure(
            text=f"Product Name: {transactionName}, \nProduct Price: {transactionPrice}, \nProduct Quantity: {transactionQuantity}, \nDateTime: {self.update_time()}\n"
        )

        dataFlag = DatabaseHandler.insertTransactionTable(
            self.dbConnection,
            [
                transactionName,
                transactionPrice,
                transactionQuantity,
                self.currentdatetime,
            ],
        )
        if dataFlag:
            # Clear the text in the CTkEntry widget
            self.addnameEntry.delete(0, customtkinter.END)
            self.addpriceEntry.delete(0, customtkinter.END)
            self.addquantityEntry.delete(0, customtkinter.END)
            viewallRefresh(self)
            show_thanks("Done", "Data Saved Successfully!")
        else:
            show_error(
                "Database Error!", "Data saving failed, Please try again later!!!"
            )

    def deltransactionID(self):
        id = self.delIDEntry.get()
        # checking entry data
        if not id and self.validate_Number(id):
            show_error("Error!", "Enter valid Transaction ID to delete record.")
            return
        # Searching Record to be deleting
        record = DatabaseHandler.viewTransactionbyID(self.dbConnection, id)

        if not record:
            show_error("Done", "No Record Found!")
            return
        # set to visible
        rc = record[0]
        self.deletingRecordLabel0.configure(text="Deleting Record: ")
        self.deletingRecordLabel1.configure(
            text=f"Product ID: {rc[0]}, \nProduct name: {rc[1]}, \nProduct price: {rc[2]}, \nProduct quantity: {rc[3]}, \nDateTime: {rc[4]}"
        )
        # Set Warning
        permission = show_delete_warning(
            f"Are you sure to deleting record!\nRecord: {record[0]}"
        )
        if permission:
            # Deleting Record
            delFlag = DatabaseHandler.deleteTransactionbyID(self.dbConnection, id)
            if delFlag:
                self.delIDEntry.delete(0, customtkinter.END)
                show_thanks("Done", "Record Deleted Successfully!")
            else:
                show_error(
                    "Database Error!",
                    "Record deleting failed, Please try again later!!!",
                )
        viewallRefresh(self)

    def discardDeleteID(self):
        self.delIDEntry.delete(0, customtkinter.END)

    def SearchByID1(self):
        SearchByID(self)

    def SearchByName1(self):
        SearchByName(self)

    def UpdateByID1(self):
        UpdateByID(self)

    def Update(self):
        UpdatingData(self)
        viewallRefresh(self)

    def UpdateCancel(self):
        # clear existing data
        self.UpdatedProductId1.configure(text="")
        self.UpdatedProductName1.delete(0, customtkinter.END)
        self.UpdatedProductPrice1.delete(0, customtkinter.END)
        self.UpdatedProductQuantity1.delete(0, customtkinter.END)
        self.UpdatedProductDateTime1.delete(0, customtkinter.END)

    def cancelAddTransactionData(self):
        # Clear the text in the CTkEntry widget
        self.addnameEntry.delete(0, customtkinter.END)
        self.addpriceEntry.delete(0, customtkinter.END)
        self.addquantityEntry.delete(0, customtkinter.END)
        show_thanks("Done", "Data Discarded!")

    def update_time(self):
        now = datetime.datetime.now()
        self.currentdatetime = now.strftime("%d %B, %Y, %I:%M:%S %p")
        try:
            self.date.configure(text=self.currentdatetime)
            self.date.after(
                1000, self.update_time
            )  # Update every 1000 milliseconds (1 second)
        except Exception as e:
            print()
        finally:
            return self.currentdatetime


def main():
    app = App()
    app._set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    # Supported themes : green, dark-blue, blue
    customtkinter.set_default_color_theme(
        "blue"
    )  # Themes: "blue" (standard), "green", "dark-blue"
    # app.attributes("-topmost", True)
    app.state("zoomed")

    ICON_PATH = os.path.join(os.path.dirname(__file__), "./assets/icon.ico")
    app.iconbitmap(ICON_PATH)
    # app.iconbitmap("./assets/icon.ico")
    app.title("Al Syed Stationary Management Software")
    app.geometry("880x600")
    app.minsize(880, 460)

    app.update_time()
    # Application Loop
    app.mainloop()


if __name__ == "__main__":
    main()
