from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('500x400')
        self.root.configure(bg='#0f172a')
        self.login_gui()
        self.root.mainloop()


    def login_gui(self):
        self.clear()

        self.main_frame = Frame(self.root, bg='#1e293b', padx=40, pady=40)
        self.main_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

        heading = Label(self.main_frame,text='NLP App',bg='#1e293b',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.main_frame,text='Enter your email',font=('Poppins',11),fg='white',bg='#1e293b')
        label1.pack(anchor='w',pady=(0,5))

        self.email_input = Entry(self.main_frame,width=30,font=('Arial',12),bg='white',fg='black',relief=FLAT,insertbackground='black')
        self.email_input.pack(pady=(0,15),ipady=5)

        label2 = Label(self.main_frame, text='Enter your password',font=('Poppins',11),fg='white',bg='#1e293b')
        label2.pack(anchor='w',pady=(0,5))

        self.password_input = Entry(self.main_frame, width=30,show='*',font=('Poppins',12),bg='white',fg='black',relief=FLAT,insertbackground='black')
        self.password_input.pack(pady=(0, 20), ipady=5)

        login_btn = Button(self.main_frame,text='Login',width=15,height=2,bg='#3b82f6',fg='white',font=('Poppins SemiBold',12),relief=FLAT,cursor='hand2',command=self.perform_login)
        login_btn.pack(pady=(0,15))

        bottom_frame = Frame(self.main_frame,bg='#1e293b')
        bottom_frame.pack()

        label3 = Label(bottom_frame,text='Not a member?',bg='#1e293b',fg='white',font=('Poppins',10))
        label3.pack(side=LEFT,pady=(10,10))

        redirect_btn = Button(bottom_frame,text='Register Now',bg='#0ea5e9',fg='white',font=('Poppins',10,'bold'),relief=FLAT,width=12,cursor='hand2',command= self.register_gui)
        redirect_btn.pack(side=LEFT,pady=(5,0))


    def register_gui(self):
        self.clear()

        self.main_frame = Frame(self.root, bg='#1e293b', padx=40, pady=40)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = Label(self.main_frame, text='NLP App', bg='#1e293b', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.main_frame, text='Enter your Full Name',font=('Poppins',11),fg='white',bg='#1e293b')
        label0.pack(anchor='w',pady=(10, 5))

        self.name_input = Entry(self.main_frame,width=30,font=('Arial',12),bg='white',fg='black',relief=FLAT,insertbackground='black')
        self.name_input.pack(pady=(0,10),ipady=5)

        label1 = Label(self.main_frame, text='Enter your email',font=('Poppins',11),fg='white',bg='#1e293b')
        label1.pack(anchor='w',pady=(10, 5))

        self.email_input = Entry(self.main_frame, width=30,font=('Arial',12),bg='white',fg='black',relief=FLAT,insertbackground='black')
        self.email_input.pack(pady=(0, 10), ipady=5)

        label2 = Label(self.main_frame, text='Enter your password',font=('Poppins',11),fg='white',bg='#1e293b')
        label2.pack(anchor='w',pady=(10, 5))

        self.password_input = Entry(self.main_frame, width=30, show='*',font=('Arial',12),bg='white',fg='black',relief=FLAT,insertbackground='black')
        self.password_input.pack(pady=(0, 20), ipady=5)

        register_btn = Button(self.main_frame, text='Register', width=15, height=2,bg='#3b82f6',fg='white',font=('Poppins SemiBold',12),relief=FLAT,cursor='hand2',command= self.perform_registration)
        register_btn.pack(pady=(10, 10))

        bottom_frame = Frame(self.main_frame, bg='#1e293b')
        bottom_frame.pack()

        label3 = Label(bottom_frame, text='Already a member?',bg='#1e293b',fg='white',font=('Poppins',10))
        label3.pack(side=LEFT,pady=(10, 10))

        redirect_btn = Button(bottom_frame, text='Login Now',bg='#0ea5e9',fg='white',font=('Poppins',10,'bold'),relief=FLAT,width=12,cursor='hand2', command=self.login_gui)
        redirect_btn.pack(side=LEFT,pady=(5, 0))

    def clear(self):
        #clear the existing gui
        if hasattr(self,'main_frame'):
            self.main_frame.destroy()

    def perform_registration(self):
        #fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')


    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        self.title_label = Label(
            self.topbar,
            text="NLP App",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        self.title_label.pack(side="left", padx=40, pady=20)

        self.logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            height=1,
            relief="flat",
            activebackground="#D62828",
            cursor="hand2",
            command=self.login_gui
        )
        self.logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Main Frame ----------
        self.main_frame = Frame(self.root, bg="#C0CCED",bd=2,relief="flat")
        self.main_frame.place(relx=0.5,rely=0.53,anchor="center",width=500,height=400)

        # Heading
        self.heading = Label(
            self.main_frame,
            text="Choose an NLP Task",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        self.heading.pack(pady=(50, 30))

        # ---------- Buttons ----------
        button_style = {
            "bg": "#2C4E80",
            "fg": "white",
            "font": ("Helvetica", 13, "bold"),
            "width": 25,
            "height": 2,
            "relief": "flat",
            "activebackground": "#345D99",
            "cursor": "hand2",
        }

        self.sentiment_btn = Button(
            self.main_frame, text="Sentiment Analysis", **button_style,command=self.sentiment_gui
        )
        self.sentiment_btn.pack(pady=15)

        self.ner_btn = Button(
            self.main_frame, text="Named Entity Recognition (NER)", **button_style
        )
        self.ner_btn.pack(pady=15)

        self.emotion_btn = Button(
            self.main_frame, text="Emotion Prediction", **button_style
        )
        self.emotion_btn.pack(pady=15)


    def sentiment_gui(self):
        self.clear()

        self.main_frame = Frame(self.root, bg='#1e293b', padx=40, pady=40)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = Label(self.main_frame, text='NLPApp', bg='#43578E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.main_frame, text='Sentiment Analysis', bg='#43578E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label = Label(self.main_frame, text='Enter the text')
        label.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.main_frame, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=30)

        sentiment_btn = Button(self.main_frame, text='Analyze sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.main_frame, text='',bg='#43578E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.main_frame, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in range(len(result['scored_labels'])):
            label = result['scored_label'][i]['label']
            score = result['scored_label'][i]['score']
            txt += f"{i + 1}.{label} ({score})\n"

            print(txt)

        self.sentiment_result['text'] = txt






nlp = NLPApp()