from tkinter import *
from PIL import Image,ImageTk



class Register:

    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x750+0+0")
        # ====bg Image====

        self.bg = ImageTk.PhotoImage(file="bg.png")
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ====left Image====

        self.left = ImageTk.PhotoImage(file="backg.jpg")
        left = Label(self.root, image=self.left)
        left.place(x=80, y=100, width=400, height=550)

        # =====register frame=====
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=550)

        title = Label(frame1, text="REGISTER HERE", font=('Cambria Bold Italic', 28,'underline'), bg='white', fg='green')
        title.place(x=50,y=30)

        # ----------------------------------row1
        f_name = Label(frame1, text="First Name", font=('Constantia', 18), bg='white', fg='black')
        f_name.place(x=50,y=100)

        txt_fname = Entry(frame1, font=('Microsoft Yi Baiti', 16,'bold'), bg='white', border=1,justify=CENTER)
        txt_fname.place(x=50, y=135, width=250,height=35)

        l_name = Label(frame1, text="Last Name", font=('Constantia', 18), bg='white', fg='black')
        l_name.place(x=370,y=100)

        txt_lname = Entry(frame1, font=('Microsoft Yi Baiti', 16,'bold'), bg='white', border=1,justify=CENTER)
        txt_lname.place(x=370, y=135, width=250,height=35)

        # ----------------------------------row2
        contact = Label(frame1, text="Contact No.", font=('Constantia', 18), bg='white', fg='black')
        contact.place(x=50,y=190)

        txt_contact = Entry(frame1, font=('Microsoft Yi Baiti', 16,'bold'), bg='white', border=1,justify=CENTER)
        txt_contact.place(x=50, y=225, width=250,height=35)

        email = Label(frame1, text="Email", font=('Constantia', 18), bg='white', fg='black')
        email.place(x=370,y=190)

        txt_email = Entry(frame1, font=('Microsoft Yi Baiti', 16,'bold'), bg='white', border=1,justify=CENTER)
        txt_email.place(x=370, y=225 , width=250,height=35)

        # ----------------------------------row3
        password = Label(frame1, text="Password", font=('Constantia', 18), bg='white', fg='black')
        password.place(x=50, y=285)

        txt_password = Entry(frame1, font=('Microsoft Yi Baiti', 16, 'bold'), bg='white', border=1,justify=CENTER,show='*')
        txt_password.place(x=50, y=320, width=250, height=35)

        cpassword = Label(frame1, text="Confirm Password", font=('Constantia', 18), bg='white', fg='black')
        cpassword.place(x=370, y=285)

        txt_cpassword = Entry(frame1, font=('Microsoft Yi Baiti', 16, 'bold'), bg='white', border=1, justify=CENTER,show='*')
        txt_cpassword.place(x=370, y=320, width=250, height=35)

        #-------Terms
        chk=Checkbutton(frame1,text='I Agree The Terms & Conditions',onvalue=1,offvalue=0,font=('Constantia', 15), bg='white', fg='black',border=2)
        chk.place(x=50,y=370)

        self.btn_image=ImageTk.PhotoImage(file='SIGNUP_BTN.png')
        btn_signup=Button(frame1,image=self.btn_image,bg='white',border=0,bd=0,cursor='hand2',activebackground='white')
        btn_signup.place(x=250,y=395)

        '''btn_signup=Button(frame1,text='Register Here',font=('Constantia', 18),border=0,bd=0,bg='#3B7A57',fg='white',cursor='hand2') 
        btn_signup.place(x=250,y=420)'''

        btn_login=Button(frame1,text="Already have an Account?",font=('Constantia',13,'underline'),border=0,bd=0,bg='white',fg='black',cursor='hand2',command=self.login_page)
        btn_login.place(x=250,y=480)

    def login_page(self):
        self.root.destroy()
        import login


root = Tk()
obj = Register(root)
root.mainloop()