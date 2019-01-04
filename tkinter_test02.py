from tkinter import *

win1 = Tk()

user_name = Listbox(win1,selectbackground = 'pink')
user_name.pack()

friends = ['LL','里海','打鼓','东湖物业']
for item in friends:
    user_name.insert(END,item)

delet = Button(win1,text = '删除',command=lambda x=user_name:x.delete(ACTIVE))
delet.pack()

mainloop()









