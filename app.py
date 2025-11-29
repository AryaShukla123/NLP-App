from tkinter import *
from mydb import Database
from tkinter import messagebox
import myapi

class NLPApp:

    def __init__(self):

        self.dbo = Database()
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

        heading = Label(
            self.main_frame,
            text='NLP App',
            bg='#1e293b',
            fg='white'
        )
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(
            self.main_frame,
            text='Enter your email',
            font=('Poppins',11),
            fg='white',
            bg='#1e293b'
        )
        label1.pack(anchor='w',pady=(0,5))

        self.email_input = Entry(
            self.main_frame,
            width=30,
            font=('Arial',12),
            bg='white',
            fg='black',
            relief=FLAT,
            insertbackground='black'
        )
        self.email_input.pack(pady=(0,15),ipady=5)

        label2 = Label(
            self.main_frame,
            text='Enter your password',
            font=('Poppins',11),
            fg='white',
            bg='#1e293b'
        )
        label2.pack(anchor='w',pady=(0,5))

        self.password_input = Entry(
            self.main_frame,
            width=30,
            show='*',
            font=('Poppins',12),
            bg='white',
            fg='black',
            relief=FLAT,
            insertbackground='black'
        )
        self.password_input.pack(pady=(0, 20), ipady=5)

        login_btn = Button(
            self.main_frame,
            text='Login',
            width=15,
            height=2,
            bg='#3b82f6',
            fg='white',
            font=('Poppins SemiBold',12),
            relief=FLAT,
            cursor='hand2',
            command=self.perform_login
        )
        login_btn.pack(pady=(0,15))

        bottom_frame = Frame(self.main_frame,bg='#1e293b')
        bottom_frame.pack()

        label3 = Label(
            bottom_frame,
            text='Not a member?',
            bg='#1e293b',
            fg='white',
            font=('Poppins',10)
        )
        label3.pack(side=LEFT,pady=(10,10))

        redirect_btn = Button(
            bottom_frame,
            text='Register Now',
            bg='#0ea5e9',
            fg='white',
            font=('Poppins',10,'bold'),
            relief=FLAT,
            width=12,
            cursor='hand2',
            command= self.register_gui
        )
        redirect_btn.pack(side=LEFT,pady=(5,0))


    def register_gui(self):
        self.clear()

        self.main_frame = Frame(self.root, bg='#1e293b', padx=40, pady=40)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = Label(
            self.main_frame,
            text='NLP App',
            bg='#1e293b',
            fg='white'
        )
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(
            self.main_frame,
            text='Enter your Full Name',
            font=('Poppins',11),
            fg='white',
            bg='#1e293b'
        )
        label0.pack(anchor='w',pady=(10, 5))

        self.name_input = Entry(
            self.main_frame,
            width=30,
            font=('Arial',12),
            bg='white',
            fg='black',
            relief=FLAT,
            insertbackground='black'
        )
        self.name_input.pack(pady=(0,10),ipady=5)

        label1 = Label(
            self.main_frame,
            text='Enter your email',
            font=('Poppins',11),
            fg='white',
            bg='#1e293b'
        )
        label1.pack(anchor='w',pady=(10, 5))

        self.email_input = Entry(
            self.main_frame,
            width=30,
            font=('Arial',12),
            bg='white',
            fg='black',
            relief=FLAT,
            insertbackground='black'
        )
        self.email_input.pack(pady=(0, 10), ipady=5)

        label2 = Label(
            self.main_frame,
            text='Enter your password',
            font=('Poppins',11),
            fg='white',
            bg='#1e293b'
        )
        label2.pack(anchor='w',pady=(10, 5))

        self.password_input = Entry(
            self.main_frame,
            width=30,
            show='*',
            font=('Arial',12),
            bg='white',
            fg='black',
            relief=FLAT,
            insertbackground='black'
        )
        self.password_input.pack(pady=(0, 20), ipady=5)

        register_btn = Button(
            self.main_frame,
            text='Register',
            width=15,
            height=2,
            bg='#3b82f6',
            fg='white',
            font=('Poppins SemiBold',12),
            relief=FLAT,
            cursor='hand2',
            command= self.perform_registration
        )
        register_btn.pack(pady=(10, 10))

        bottom_frame = Frame(self.main_frame, bg='#1e293b')
        bottom_frame.pack()

        label3 = Label(
            bottom_frame,
            text='Already a member?',
            bg='#1e293b',
            fg='white',
            font=('Poppins',10)
        )
        label3.pack(side=LEFT,pady=(10, 10))

        redirect_btn = Button(
            bottom_frame,
            text='Login Now',
            bg='#0ea5e9',
            fg='white',
            font=('Poppins',10,'bold'),
            relief=FLAT,
            width=12,
            cursor='hand2',
            command=self.login_gui
        )
        redirect_btn.pack(side=LEFT,pady=(5, 0))

    def clear(self):

        widgets = ["main_frame", "card", "topbar"]

        for w in widgets:
            if hasattr(self, w):
                getattr(self, w).destroy()

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

        self.scrollable_frame = None

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
        self.main_frame = Frame(self.root, bg="#C0CCED", bd=2, relief="flat")
        self.main_frame.place(relx=0.5, rely=0.55, anchor="center", width=500, height=400)

        # Heading
        self.heading = Label(
            self.main_frame,
            text="Choose an NLP Task",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        self.heading.pack(pady=(20, 10))


        container = Frame(self.main_frame, bg="#C0CCED")
        container.pack(fill="both", expand=True, pady=10)

        canvas = Canvas(container, bg="#C0CCED", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        scroll_frame = Frame(canvas, bg="#C0CCED")
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        def configure_scroll(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scroll_frame.bind("<Configure>", configure_scroll)


        buttons_frame = Frame(scroll_frame, bg="#C0CCED")
        buttons_frame.pack(pady=20)

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

        tasks = [
            ("Sentiment Analysis", self.sentiment_gui),
            ("Named Entity Recognition (NER)", self.ner_gui),
            ("Emotion Prediction", self.emotion_gui),
            ("Language Detection", self.language_gui),
            ("Paraphrasing", self.paraphrase_gui),
            ("Semantic Search", self.semantic_search_gui),
            ("Semantic Similarity", self.semantic_similarity_gui),
            ("Summarization", self.summarization_gui),
            ("Translation", self.translation_gui),
            ("Question Answering", self.qa_gui),
        ]

        for text, command in tasks:
            btn = Button(
                buttons_frame,
                text=text,
                width=50,
                height=2,
                bg="#6E88C9",
                fg="white",
                font=("Arial", 12),
                command=command if command else None
            )
            btn.pack(pady=10)

    def sentiment_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Sentiment Analysis",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Sentiment Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Sentiment Analysis",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))


        text_label = Label(
            self.card,
            text="Enter text to analyze:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        text_label.pack(anchor="w")

        self.sentiment_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.sentiment_input.pack(pady=(5, 20), ipady=8)

        analyze_btn = Button(
            self.card,
            text="Analyze Sentiment",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_sentiment_analysis
        )
        analyze_btn.pack(pady=(0, 20))

        self.sentiment_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.sentiment_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()


    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()

        if not text.strip():
            self.sentiment_result['text'] = "Please enter text!"
            return

        try:
            result = myapi.get_sentiment(text)
            sentiment = result.get("sentiment", "No sentiment found")

            self.sentiment_result['text'] = f"Sentiment: {sentiment}"

        except Exception as e:
            self.sentiment_result['text'] = f"Error: {str(e)}"


    def ner_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - NER",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- NER Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Named Entity Recognition (NER)",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        # Label
        text_label = Label(
            self.card,
            text="Enter text:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        text_label.pack(anchor="w")

        self.ner_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.ner_input.pack(pady=(5, 20), ipady=8)

        analyze_btn = Button(
            self.card,
            text="Run NER",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_ner_analysis

        )
        analyze_btn.pack(pady=(0, 20))

        # OUTPUT
        self.ner_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 13),
            wraplength=400,
            justify="left"
        )
        self.ner_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = myapi.get_ner(text)

        txt = "Detected Entities:\n\n"

        for ent in result["entities"]:
            txt += f"- {ent['text']}  →  {ent['type']}\n"

        self.ner_result["text"] = txt

    def emotion_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Emotion Detection",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)


        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Emotion Detection",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))


        text_label = Label(
            self.card,
            text="Enter text:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        text_label.pack(anchor="w")

        self.emotion_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.emotion_input.pack(pady=(5, 20), ipady=8)

        analyze_btn = Button(
            self.card,
            text="Detect Emotion",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_emotion_analysis

        )
        analyze_btn.pack(pady=(0, 20))

        # OUTPUT
        self.emotion_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 13),
            wraplength=400,
            justify="left"
        )
        self.emotion_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = myapi.get_emotion(text)

        txt = f"Detected Emotion: {result['emotion'].capitalize()}"
        self.emotion_result["text"] = txt

    def language_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Language Detection",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Language Detection Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Language Detection",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))


        text_label = Label(
            self.card,
            text="Enter text to detect language:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        text_label.pack(anchor="w")

        self.language_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.language_input.pack(pady=(5, 20), ipady=8)

        detect_btn = Button(
            self.card,
            text="Detect Language",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_language_detection

        )
        detect_btn.pack(pady=(0, 20))

        self.language_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.language_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_language_detection(self):

        text = self.language_input.get()


        result = myapi.detect_language(text)


        txt = f"Detected Language:\n\n{result['language']}"


        self.language_result["text"] = txt

    def paraphrase_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Paraphrasing",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Paraphrasing Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Paraphrasing",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))


        text_label = Label(
            self.card,
            text="Enter text to paraphrase:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        text_label.pack(anchor="w")

        self.paraphrase_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.paraphrase_input.pack(pady=(5, 20), ipady=8)

        paraphrase_btn = Button(
            self.card,
            text="Paraphrase",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_paraphrase

        )
        paraphrase_btn.pack(pady=(0, 20))

        self.paraphrase_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.paraphrase_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_paraphrase(self):

        text = self.paraphrase_input.get()

        result = myapi.get_paraphrase(text)

        txt = f"Paraphrased Text:\n\n{result['paraphrased_text']}"

        self.paraphrase_result["text"] = txt

    def semantic_search_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Semantic Search",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Semantic Search Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Semantic Search",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        query_label = Label(
            self.card,
            text="Enter your search query:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        query_label.pack(anchor="w")

        self.semantic_input = Entry(
            self.card,
            width=45,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.semantic_input.pack(pady=(5, 20), ipady=8)

        search_btn = Button(
            self.card,
            text="Search",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_semantic_search
        )
        search_btn.pack(pady=(0, 20))

        self.semantic_result = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.semantic_result.pack(pady=(5, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_semantic_search(self):
        query = self.semantic_input.get()
        result = myapi.semantic_search(query)

        txt = "Search Results:\n\n"
        for item in result["results"]:
            txt += f"- {item}\n\n"

        self.semantic_result["text"] = txt

    def semantic_similarity_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Semantic Similarity",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.52, anchor="center")

        heading = Label(
            self.card,
            text="Semantic Similarity",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        Label(
            self.card,
            text="Enter First Text:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        ).pack(anchor="w")

        self.sim_text1 = Text(
            self.card,
            height=4,
            width=50,
            font=("Helvetica", 12),
            bd=0,
            relief="flat",
            wrap="word"
        )
        self.sim_text1.pack(pady=(5, 20))

        Label(
            self.card,
            text="Enter Second Text:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        ).pack(anchor="w")

        self.sim_text2 = Text(
            self.card,
            height=4,
            width=50,
            font=("Helvetica", 12),
            bd=0,
            relief="flat",
            wrap="word"
        )
        self.sim_text2.pack(pady=(5, 20))

        sim_btn = Button(
            self.card,
            text="Check Similarity",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.run_semantic_similarity
        )
        sim_btn.pack(pady=(10, 20))

        self.sim_output = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.sim_output.pack(pady=(10, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def run_semantic_similarity(self):
        t1 = self.sim_text1.get("1.0", "end").strip()
        t2 = self.sim_text2.get("1.0", "end").strip()

        if t1 == "" or t2 == "":
            self.sim_output["text"] = "Please enter both texts."
            return

        result = myapi.semantic_similarity(t1, t2)

        score = result.get("similarity_score", 0)
        explanation = result.get("explanation", "No explanation available.")

        final_text = f"Similarity Score: {score}\n\nExplanation: {explanation}"

        self.sim_output["text"] = final_text

    def summarization_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Summarization",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.52, anchor="center")

        heading = Label(
            self.card,
            text="Text Summarization",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        Label(
            self.card,
            text="Enter text to summarize:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        ).pack(anchor="w")

        self.sum_input = Text(
            self.card,
            height=6,
            width=50,
            font=("Helvetica", 12),
            bd=0,
            relief="flat",
            wrap="word"
        )
        self.sum_input.pack(pady=(5, 20))

        sum_btn = Button(
            self.card,
            text="Generate Summary",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.run_summarization
        )
        sum_btn.pack(pady=(10, 20))

        self.sum_output = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.sum_output.pack(pady=(10, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def run_summarization(self):
        text = self.sum_input.get("1.0", "end").strip()

        if text == "":
            self.sum_output["text"] = "Please enter text to summarize."
            return

        result = myapi.summarize_text(text)

        summary = result.get("summary", "No summary available.")

        final_output = f"Summary:\n\n{summary}"

        self.sum_output["text"] = final_output

    def translation_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Translation",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Translation",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        inp_label = Label(
            self.card,
            text="Enter text to translate:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        inp_label.pack(anchor="w")

        self.trans_input = Text(
            self.card,
            width=45,
            height=5,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat"
        )
        self.trans_input.pack(pady=(5, 20))

        # Language dropdown
        lang_label = Label(
            self.card,
            text="Select target language:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        lang_label.pack(anchor="w")

        self.trans_lang = StringVar()
        languages = ["Hindi", "English", "French", "Spanish", "German", "Tamil", "Telugu"]

        lang_dropdown = OptionMenu(self.card, self.trans_lang, *languages)
        lang_dropdown.config(width=20, font=("Helvetica", 12))
        lang_dropdown.pack(pady=(5, 20))

        trans_btn = Button(
            self.card,
            text="Translate",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_translation
        )
        trans_btn.pack(pady=(0, 20))

        self.trans_output = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.trans_output.pack(pady=(10, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_translation(self):
        text = self.trans_input.get("1.0", "end").strip()
        target = self.trans_lang.get().strip()

        if text == "" or target == "":
            self.trans_output["text"] = "Please enter text and select language."
            return

        result = myapi.translate_text(text, target)

        translated = result.get("translated_text", "No translation available.")

        final_text = f"Translated Text:\n\n{translated}"

        self.trans_output["text"] = final_text

    def qa_gui(self):
        self.clear()

        # ---------- Top Bar ----------
        self.topbar = Frame(self.root, bg="#C0CCED", height=70)
        self.topbar.pack(fill="x")

        title_label = Label(
            self.topbar,
            text="NLP App - Q/A",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 22, "bold")
        )
        title_label.pack(side="left", padx=40, pady=20)

        logout_btn = Button(
            self.topbar,
            text="Logout",
            bg="#E63946",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.login_gui
        )
        logout_btn.pack(side="right", padx=40, pady=20)

        # ---------- Card ----------
        self.card = Frame(
            self.root,
            bg="#C0CCED",
            padx=40,
            pady=40
        )
        self.card.place(relx=0.5, rely=0.55, anchor="center")

        heading = Label(
            self.card,
            text="Question Answering",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 20, "bold")
        )
        heading.pack(pady=(0, 25))

        ctx_label = Label(
            self.card,
            text="Enter context paragraph:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        ctx_label.pack(anchor="w")

        self.qa_context = Text(
            self.card,
            width=45,
            height=5,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat"
        )
        self.qa_context.pack(pady=(5, 20))

        q_label = Label(
            self.card,
            text="Enter your question:",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 12)
        )
        q_label.pack(anchor="w")

        self.qa_question = Text(
            self.card,
            width=45,
            height=3,
            font=("Helvetica", 13),
            bg="white",
            fg="black",
            relief="flat"
        )
        self.qa_question.pack(pady=(5, 20))

        qa_btn = Button(
            self.card,
            text="Get Answer",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=22,
            relief="flat",
            cursor="hand2",
            command=self.do_qa
        )
        qa_btn.pack(pady=(0, 20))

        self.qa_output = Label(
            self.card,
            text="",
            bg="#C0CCED",
            fg="black",
            font=("Helvetica", 14, "bold"),
            wraplength=400,
            justify="center"
        )
        self.qa_output.pack(pady=(10, 20))

        back_btn = Button(
            self.card,
            text="← Back",
            bg="#3D5A80",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
            cursor="hand2",
            command=self.home_gui
        )
        back_btn.pack()

    def do_qa(self):
        question = self.qa_question.get("1.0", "end").strip()
        context = self.qa_context.get("1.0", "end").strip()

        if question == "" or context == "":
            self.qa_output["text"] = "Please enter both question and context."
            return

        result = myapi.answer_question(question, context)

        answer = result.get("answer", "No answer found.")

        final_text = f"Answer:\n\n{answer}"

        self.qa_output["text"] = final_text


nlp = NLPApp()