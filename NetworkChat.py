# Import Modules
from tkinter import *
from tkinter import filedialog

# Network Chat Window Setup
class NetworkChat(Tk):

    def __init__(self, version):

        # Declare Super Parent
        super().__init__()

        # Setup Window
        self.title("Network Chat Ver: " + version)
        self.state("zoomed")

        # Menubar Setup
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        # Chat Menu Setup
        self.chatMenu = Menu(self.menubar, tearoff=0)

        self.userChatMenu = Menu(self.chatMenu, tearoff=0)
        self.userChatMenu.add_command(label="Save Chat Logs...")
        self.userChatMenu.add_separator()
        self.userChatMenu.add_command(label="Save All Users Chat Logs...")

        self.chatMenu.add_cascade(menu=self.userChatMenu, label="User")
        self.chatMenu.add_separator()
        self.chatMenu.add_command(label="Connect")
        self.chatMenu.add_command(label="Disconnect", state=DISABLED)

        self.menubar.add_cascade(menu=self.chatMenu, label="Chat")

        # Chat Entry Window Setup
        self.chatEntryFrame = Frame(self)
        self.chatEntryLabel = Label(self.chatEntryFrame, text="Message: ")
        self.chatEntryLabel.pack(side=LEFT, anchor=S)

        self.chatEntry = StringVar()
        self.chatEntryInput = Entry(self.chatEntryFrame, textvariable=self.chatEntry, width=1000)
        self.chatEntryInput.pack(side=LEFT, fill=X, expand=True)

        self.chatEntryFrame.pack(side=BOTTOM)

        # Chat Message Window Setup
        self.chatScroll = Scrollbar(self)
        self.chatMessage = Text(self, yscrollcommand=self.chatScroll.set, state=DISABLED)
        self.chatScroll["command"] = self.chatMessage.yview

        self.chatScroll.pack(side=RIGHT, fill=Y)
        self.chatMessage.pack(fill=BOTH, expand=True)

        self.chatEntryInput.bind("<Return>", self.send_chat)

        # Chat Message Tags
        self.chatMessage.tag_configure("self", foreground="red")
        self.chatMessage.tag_configure("other", foreground="blue")

        self.insert_chat("Friend", "Hello World!")
        

    def insert_chat(self, author, message):
        self.chatMessage["state"] = NORMAL
        if author == "Me":
            self.chatMessage.insert(END, author + ": ", ("self"))
        else:
            self.chatMessage.insert(END, author + ": ", ("other"))
        self.chatMessage.insert(END, message + "\n")
        self.chatMessage["state"] = DISABLED

    def send_chat(self, *args):
        chatMessage = self.chatEntry.get()
        self.insert_chat("Me", chatMessage)
        self.chatEntry.set("")

nc = NetworkChat("0.0.1")
nc.mainloop()
