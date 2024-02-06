import datetime
import customtkinter
from PIL import Image
import os


def load_image(path, width, height):
    try:
        return customtkinter.CTkImage(
            light_image=Image.open(path).resize((width, height), Image.ANTIALIAS),
            size=(width, height),
        )
    except FileNotFoundError:
        print(f"Error: Image file not found at path: {path}")
        return None
    except Exception as e:
        print(f"Error opening image: {e}")
        return None


def helpTab(parentFourth_Frame):
    tabview_4 = customtkinter.CTkTabview(parentFourth_Frame, width=900)
    tabview_4.pack(pady=10, padx=10)
    HelpTab = tabview_4.add("Help")
    LicenceTab = tabview_4.add("Licence")
    DeveloperTab = tabview_4.add("Developer")

    # ? Help Tab - Information about Software

    IMAGE_WIDTH = 150
    IMAGE_HEIGHT = 150
    # IMAGE_PATH = os.path.join(os.path.dirname(__file__), "Shop_Logo.png")
    IMAGE_FILENAME = "Shop_Logo.png"
    IMAGE_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "assets", IMAGE_FILENAME)
    )

    Shop_Logo_Image = load_image(IMAGE_PATH, IMAGE_WIDTH, IMAGE_HEIGHT)

    customtkinter.CTkLabel(master=HelpTab, image=Shop_Logo_Image, text="").pack(pady=10)

    customtkinter.CTkLabel(
        HelpTab,
        text="Al-Syed Stationary Management Software",
        font=customtkinter.CTkFont("Times new roman", size=22, weight="bold"),
    ).pack(pady=10)

    customtkinter.CTkLabel(
        HelpTab,
        text="""Al-Syed Stationary Management Software is an management system to manage stationary transaction history and \n maintain record about transactions. This management software holds the functionality of add new transaction,\n modify existing transaction, view report about transactions, and also able to delete transactions.\nThis helps the user to efficiently maintain records about transaction and can view tranasctions report about her profits or losses.""",
    ).pack(pady=5)

    # Software Holders informations
    customtkinter.CTkLabel(
        HelpTab,
        text="Software Holders",
        font=customtkinter.CTkFont(size=12, weight="bold"),
    ).pack(pady=5)

    # stakeholder
    linkedin_label = customtkinter.CTkLabel(HelpTab, text="Stakeholder: ***** ******")
    linkedin_label.pack(pady=2)

    # author
    github_label = customtkinter.CTkLabel(HelpTab, text="Author/developer: Asher Fraz")
    github_label.pack(pady=2)

    # ? Licence about Software
    customtkinter.CTkLabel(
        LicenceTab,
        text="Software Licence",
        font=customtkinter.CTkFont("Times new roman", size=22, weight="bold"),
    ).pack(pady=10)
    # get current year
    currentyear = datetime.date.today().year
    customtkinter.CTkLabel(
        LicenceTab,
        text=f"""Copyright {currentyear} Asher Fraz""",
    ).pack(pady=5)
    customtkinter.CTkLabel(
        LicenceTab,
        text="""Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), \nto deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,\nsublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:""",
    ).pack(pady=5)
    customtkinter.CTkLabel(
        LicenceTab,
        text="""The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.""",
    ).pack(pady=5)
    customtkinter.CTkLabel(
        LicenceTab,
        text="""THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED\nTO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\nIN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,\nDAMAGES OR OTHER LIABILITY,WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""",
    ).pack(pady=10)

    # ? Developer Tab - Information
    customtkinter.CTkLabel(
        DeveloperTab,
        text="Developer Profile",
        font=customtkinter.CTkFont("Times new roman", size=15, weight="bold"),
    ).pack(pady=10)

    customtkinter.CTkLabel(DeveloperTab, text="Name: Asher Fraz - (Developer)").pack(
        pady=5
    )
    # Social Links
    customtkinter.CTkLabel(
        DeveloperTab,
        text="Social Links",
        font=customtkinter.CTkFont(size=12, weight="bold"),
    ).pack(pady=5)
    # LinkedIn
    linkedin_label = customtkinter.CTkLabel(
        DeveloperTab, text="LinkedIn: https://linkedin.com/in/asherfraz"
    )
    linkedin_label.pack(pady=2)
    # GitHub
    github_label = customtkinter.CTkLabel(
        DeveloperTab, text="GitHub: https://github.com/asherfraz"
    )
    github_label.pack(pady=2)
