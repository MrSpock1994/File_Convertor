import convertapi
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Convertor")
root.geometry("330x200")


def select_file():
    global x
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("png files", "*.png"),
                                                                                             ("all files", "*.*")))
    x = root.filename


def save_file():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    return


def file_convert():
    convertapi.api_secret = "INSERT YOUR KEY HERE"
    result = convertapi.convert(l2_2.get(), {'File':  x}, timeout=120)
    result.save_files(folder_selected)
    result_label = Label(root, text="You convert " + l1_1.get() + " to " + l2_2.get() + " sucessfully.")
    result_label.grid(row=5, column=1, columnspan=2)
    return


convert = Button(root, text="Convert", command=file_convert)
convert.grid(row=4, column=1, columnspan=2, pady=5, ipadx=140)

file_btn = Button(root, text="Select the file", command=select_file)
file_btn.grid(row=2, column=1, columnspan=2, pady=5, ipadx=126)

save_file_btn = Button(root, text="Select the folder to save it", command=save_file)
save_file_btn.grid(row=3, column=1, columnspan=2, pady=5, ipadx=94)

l1 = Label(root, text="Convert from:")
l1.grid(row=0, column=1, ipadx=20)
l1_1 = Entry(root, width=20)
l1_1.grid(row=1, column=1, ipadx=20)

l2 = Label(root, text="Convert to:")
l2.grid(row=0, column=2, ipadx=20)
l2_2 = Entry(root, width=20)
l2_2.grid(row=1, column=2, ipadx=20)

root.mainloop()

