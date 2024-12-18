from tkinter import *
from tkinter import messagebox

QUESTIONS = [
    {
        "question": "Apa ibu kota Indonesia?",
        "options": ["Jakarta", "Bandung", "Surabaya", "Medan"],
        "correct_option": 0
    },
    {
        "question": "Siapa penemu lampu pijar?",
        "options": ["Albert Einstein", "Nikola Tesla", "Thomas Edison", "Isaac Newton"],
        "correct_option": 2
    },
    {
        "question": "Berapa hasil dari 3 x 4?",
        "options": ["7", "12", "15", "10"],
        "correct_option": 1
    },
    {
        "question": "Planet terbesar di tata surya adalah?",
        "options": ["Mars", "Jupiter", "Saturnus", "Bumi"],
        "correct_option": 1
    },
    {
        "question": "Berapakah jumlah sisi pada segitiga?",
        "options": ["2", "3", "4", "5"],
        "correct_option": 1
    },
    {
        "question": "Hewan darat tercepat di dunia adalah?",
        "options": ["Cheetah", "Singa", "Kuda", "Harimau"],
        "correct_option": 0
    },
    {
        "question": "Siapa penulis novel 'Laskar Pelangi'?",
        "options": ["Andrea Hirata", "Pramoedya Ananta Toer", "Tere Liye", "Habiburrahman El Shirazy"],
        "correct_option": 0
    },
    {
        "question": "Pulau terbesar di Indonesia adalah?",
        "options": ["Jawa", "Sumatra", "Kalimantan", "Sulawesi"],
        "correct_option": 2
    },
    {
        "question": "Siapa tokoh yang terkenal dengan teori gravitasi?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "correct_option": 1
    },
    {
        "question": "Berapakah hasil dari 45 - 15?",
        "options": ["25", "30", "35", "40"],
        "correct_option": 1
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Pilihan Ganda")
        self.root.geometry('925x500+300+200')
        self.root.configure(bg='#fff')
        self.root.resizable(False, False)

        # Variabel kuis
        self.current_question_index = 0
        self.score = 0

        # Judul
        self.title_label = Label(self.root, text="Kuis Pilihan Ganda", font=("Arial", 24, "bold"), bg="white", fg="#57a1f8")
        self.title_label.pack(pady=20)

        # Label pertanyaan
        self.question_label = Label(self.root, text="", font=("Arial", 16), wraplength=700, bg="white", justify="center")
        self.question_label.pack(pady=20)

        # Variabel jawaban
        self.answer_var = IntVar()

        # Tombol-tombol pilihan jawaban
        self.option_buttons = []
        for i in range(4):
            btn = Radiobutton(self.root, text="", variable=self.answer_var, value=i, font=("Arial", 14), bg="white")
            btn.pack(anchor="w", padx=50, pady=5)
            self.option_buttons.append(btn)

        # Tombol Submit
        self.submit_btn = Button(self.root, text="Submit", font=("Arial", 14), bg="#57a1f8", fg="white", command=self.check_answer)
        self.submit_btn.pack(pady=20)

        # Memuat pertanyaan pertama
        self.load_question()

    def load_question(self):
        # Cek apakah masih ada pertanyaan
        if self.current_question_index < len(QUESTIONS):
            question_data = QUESTIONS[self.current_question_index]
            self.question_label.config(text=f"Pertanyaan {self.current_question_index + 1}: {question_data['question']}")

            # Update pilihan jawaban
            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option)
            self.answer_var.set(-1)  # Reset pilihan
        else:
            self.show_result()

    def check_answer(self):
        selected_option = self.answer_var.get()
        if selected_option == -1:
            messagebox.showwarning("Peringatan", "Pilih salah satu jawaban!")
            return

        correct_option = QUESTIONS[self.current_question_index]['correct_option']
        if selected_option == correct_option:
            self.score += 1
            messagebox.showinfo("Benar!", "Jawaban Anda benar!")
        else:
            messagebox.showerror("Salah!", "Jawaban Anda salah.")

        self.current_question_index += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Kuis Selesai", f"Skor Anda: {self.score}/{len(QUESTIONS)}")
        self.root.destroy()

# Fungsi utama
if __name__ == "__main__":
    # Membuat window utama
    quiz = Tk()
    app = QuizApp(quiz)
    quiz.mainloop()
