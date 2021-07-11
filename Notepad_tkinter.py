from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x500")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("Notepad.ico")

    def New_f():
        global file
        root.title("Untitled-Notepad")
        file = None
        textbox.delete(1.0, END)

    def Open_f():
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            textbox.delete(1.0, END)
            f = open(file, "r")
            textbox.insert(1.0, f.read())
            f.close()


    def Save_f():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                f = open(file, "w")
                f.write(textbox.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")

        else:
            f = open(file, "w")
            f.write(textbox.get(1.0, END))
            f.close()

    def Exit_f():
        root.destroy()

    def Copy_f():
        textbox.event_generate(("<<Copy>>"))

    def Cut_f():
        textbox.event_generate(("<<Cut>>"))

    def Paste_f():
        textbox.event_generate(("<<Paste>>"))

    def Exp_f():
        value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
        if value == "yes":
            msg = "Great. Rate us on appstore please"
        else:
            msg = "Tell us what went wrong. We will call you soon"
        tmsg.showinfo("Experience", msg)

    def About_f():
        tmsg.showinfo("Notepad", "Notepad in Tkinter using Python")

    textbox = Text(root, font="Arial 10")
    file = None
    textbox.pack(expand=True, fill=BOTH)

    Mainmenu = Menu(root)
    FileMenu = Menu(Mainmenu, tearoff=0)
    FileMenu.add_command(label="New", command=New_f)
    FileMenu.add_command(label="Open", command=Open_f)
    FileMenu.add_separator()
    FileMenu.add_command(label="Save", command=Save_f)
    FileMenu.add_command(label="Exit", command=Exit_f)
    Mainmenu.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(Mainmenu, tearoff=0)
    EditMenu.add_command(label="Copy", command=Copy_f)
    EditMenu.add_command(label="Cut", command=Cut_f)
    EditMenu.add_separator()
    EditMenu.add_command(label="Paste", command=Paste_f)
    Mainmenu.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(Mainmenu, tearoff=0)
    HelpMenu.add_command(label="Experience", command=Exp_f)
    HelpMenu.add_command(label="About Notepad", command=About_f)
    Mainmenu.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=Mainmenu)

    Slider = Scrollbar(textbox)
    Slider.pack(side=RIGHT, fill=Y)
    Slider.config(command=textbox.yview)
    textbox.config(yscrollcommand=Slider.set)
    root.mainloop()


