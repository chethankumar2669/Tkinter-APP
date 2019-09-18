from tkinter import *
myapp=Tk()
font10 = "-family Arial -size 15 -weight normal -slant italic "\
"-underline 0 -overstrike 0"
myapp.title("LOGIN")
myapp.geometry("709x290+609+162")
myapp.resizable(0,0)
myapp.configure(background="#3aa3d8")
Label(myapp,text="Name",background="#3aa3d8",font=font10,foreground="#ffffff").place(relx=0.169, rely=0.103, height=46, width=182)
Entry(myapp,background="#ffff19",font=font10,foreground="#000000").place(relx=0.451, rely=0.138,height=34, relwidth=0.358)
Label(myapp,text="Mail ID",background="#3aa3d8",font=font10,foreground="#ffffff").place(relx=0.155, rely=0.345, height=46, width=182)
Entry(myapp,background="#ffff19",font=font10,foreground="#000000").place(relx=0.451,rely=0.379,height=34,relwidth=0.358)
Button(myapp,background="#23d83b",cursor="hand2",font=font10,foreground="#fff0f9",relief="groove",text='Exit',command=myapp.destroy).place(relx=0.353, rely=0.655, height=43, width=216)
myapp.mainloop()