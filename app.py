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

        self.password_input = Entry(self.main_frame, width=30,show='*',font=('Poppins',12),bg='white',fg='black',relief=FLAT,insertbackground='white')
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

        heading = Label(self.root, text='NLPApp', bg='#0f172a', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter your Full Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root, text='Enter your email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter your password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=20, height=2,command= self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(10, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

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

        heading = Label(self.root, text='NLPApp', bg='#43578E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#43578E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#43578E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label = Label(self.root, text='Enter the text')
        label.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=30)

        sentiment_btn = Button(self.root, text='Analyze sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#43578E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
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