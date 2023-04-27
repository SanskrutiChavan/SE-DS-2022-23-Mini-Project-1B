from tkinter import *
from PIL import Image,ImageTk


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1100x750+0+0")

        #-----bg IMage------

        self.bg=ImageTk.PhotoImage(file='bg.png')
        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        #-----left image------

        self.left=ImageTk.PhotoImage(file='backg.jpg')
        left=Label(self.root,image=self.left)
        left.place(x=80,y=100,width=400,height=500)

        #------Login Frame-----

        frame2=Frame(self.root,bg='white')
        frame2.place(x=480,y=100,width=500,height=500)

        title=Label(frame2,text="LOGIN HERE",font=('Cambria Bold Italic',28,'underline'), bg='white', fg='green')
        title.place(x=50,y=30)

        #--------------Row1

        email=Label(frame2,text="Email",font=('Constantia', 19), bg='white', fg='black')
        email.place(x=90,y=120)

        txt_email=Entry(frame2,font=('Microsoft Yi Baiti', 16,'bold'), bg='white', border=1,justify=CENTER)
        txt_email.place(x=90, y=160, width=300,height=40)

        #---------------Row2

        password = Label(frame2, text="Password", font=('Constantia', 19), bg='white', fg='black')
        password.place(x=90, y=235)

        txt_password = Entry(frame2, font=('Microsoft Yi Baiti', 16, 'bold'), bg='white', border=1, justify=CENTER,show='*')
        txt_password.place(x=90, y=275, width=300, height=40)

        #-----------Login Button

        btn_login = Button(frame2, text='Login Here', font=('Constantia', 18), border=0, bd=0, bg='#3B7A57',fg='white', cursor='hand2')
        btn_login.place(x=180, y=350)

        btn_register = Button(frame2, text="Create an Account?", font=('Constantia', 13, 'underline'), border=0,bd=0, bg='white', fg='black', cursor='hand2',activebackground='white',command=self.register_page)
        btn_register.place(x=171, y=410)

    def register_page(self):
        self.root.destroy()
        import register


root = Tk()
obj = Login(root)
root.mainloop()
