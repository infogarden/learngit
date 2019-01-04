# 捕获键盘事件
from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=True)

for i in range(20):
    listbox.insert(END,str(i))

Label(root, text='Red', bg='red',fg='white').pack(fill=X)
Label(root, text="Green", bg="green", fg="black").pack(fill=X)
Label(root, text="Blue", bg="blue", fg="white").pack(fill=X)

mainloop()