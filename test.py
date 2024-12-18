def admin_window():
    def clear_right_frame():
        for widget in right_frame.winfo_children():
            widget.destroy()

    def load_results():
        try:
            with open(RESULT_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print("Error loading results:", e)
            return []

    def view_results():
        clear_right_frame()
        results = load_results()
        print("Loaded Results:", results)  
        if not results:
            Label(right_frame, text="Belum ada hasil ujian.", font=('Arial', 14), fg='red').pack(pady=10)
            return
        
        sorted_results = sorted(results, key=lambda x: x.get('score', 0), reverse=True)
        Label(right_frame, text="Hasil Ujian", font=('Arial', 16, 'bold')).pack(pady=10)
        for result in sorted_results:
            Label(right_frame, text=f"{result.get('username', 'Unknown')}: {result.get('score', 0)}", anchor="w").pack(fill=X, padx=10, pady=2)



    def add_question():
        clear_right_frame()
        Label(right_frame, text='Tambah Soal', font=('Arial', 16, 'bold')).pack(pady=10)

        def save_new_question():
            question = question_entry.get()
            options = [option_entries[i].get() for i in range(4)]
            correct = int(correct_option.get())
            questions = load_questions()
            questions.append({'question': question, 'options': options, 'correct_option': correct})
            save_questions(questions)
            messagebox.showinfo('Sukses', 'Soal berhasil ditambahkan!')
            clear_right_frame()

        Label(right_frame, text='Pertanyaan:').pack(anchor="w", padx=10)
        question_entry = Entry(right_frame, width=50)
        question_entry.pack(padx=10, pady=5)

        option_entries = []
        for i in range(4):
            Label(right_frame, text=f'Opsi {i+1}:').pack(anchor="w", padx=10)
            option_entry = Entry(right_frame, width=50)
            option_entry.pack(padx=10, pady=2)
            option_entries.append(option_entry)

        Label(right_frame, text='Jawaban Benar (0-3):').pack(anchor="w", padx=10)
        correct_option = Entry(right_frame, width=10)
        correct_option.pack(padx=10, pady=5)

        Button(right_frame, text='Simpan Soal', command=save_new_question).pack(pady=10)

    def edit_question():
        clear_right_frame()
        questions = load_questions()
        Label(right_frame, text='Edit Soal', font=('Arial', 16, 'bold')).pack(pady=10)
        Label(right_frame, text='Index Soal:').pack(padx=10)
        index_entry = Entry(right_frame, width=10)
        index_entry.pack(pady=5)

        def load_question():
            try:
                index = int(index_entry.get())
                if 0 <= index < len(questions):
                    clear_right_frame()
                    Label(right_frame, text='Edit Soal', font=('Arial', 16, 'bold')).pack(pady=10)

                    question_var = StringVar(value=questions[index]['question'])
                    Label(right_frame, text='Pertanyaan:').pack(padx=10)
                    question_entry = Entry(right_frame, textvariable=question_var, width=50)
                    question_entry.pack(padx=10, pady=5)

                    option_vars = []
                    for i in range(4):
                        option_var = StringVar(value=questions[index]['options'][i])
                        Label(right_frame, text=f'Opsi {i+1}:').pack(padx=10)
                        option_entry = Entry(right_frame, textvariable=option_var, width=50)
                        option_entry.pack(padx=10, pady=2)
                        option_vars.append(option_var)

                    correct_var = StringVar(value=questions[index]['correct_option'])
                    Label(right_frame, text='Jawaban Benar (0-3):').pack(padx=10)
                    correct_entry = Entry(right_frame, textvariable=correct_var, width=10)
                    correct_entry.pack(padx=10, pady=5)

                    def save_edits():
                        questions[index]['question'] = question_var.get()
                        for i in range(4):
                            questions[index]['options'][i] = option_vars[i].get()
                        questions[index]['correct_option'] = int(correct_var.get())
                        save_questions(questions)
                        messagebox.showinfo('Sukses', 'Soal berhasil diperbarui!')
                        clear_right_frame()

                    Button(right_frame, text='Simpan Perubahan', command=save_edits).pack(pady=10)
                else:
                    messagebox.showerror('Error', 'Index soal tidak valid!')
            except ValueError:
                messagebox.showerror('Error', 'Masukkan index yang valid!')

        Button(right_frame, text='Load Soal', command=load_question).pack(pady=5)

    def delete_question():
        clear_right_frame()
        Label(right_frame, text='Hapus Soal', font=('Arial', 16, 'bold')).pack(pady=10)
        Label(right_frame, text='Index Soal:').pack(padx=10)
        index_entry = Entry(right_frame, width=10)
        index_entry.pack(pady=5)

        def confirm_delete():
            try:
                index = int(index_entry.get())
                questions = load_questions()
                if 0 <= index < len(questions):
                    questions.pop(index)
                    save_questions(questions)
                    messagebox.showinfo('Sukses', 'Soal berhasil dihapus!')
                    clear_right_frame()
                else:
                    messagebox.showerror('Error', 'Index soal tidak valid!')
            except ValueError:
                messagebox.showerror('Error', 'Masukkan index yang valid!')

        Button(right_frame, text='Hapus Soal', command=confirm_delete).pack(pady=5)

    admin = Tk()
    admin.title('Admin Dashboard')
    admin.state('zoomed')

    # Left Menu Frame
    left_frame = Frame(admin, bg='#333', width=200)
    left_frame.pack(side=LEFT, fill=Y)

    Button(left_frame, text='Lihat Hasil Ujian', bg='#57a1f8', fg='white', command=view_results).pack(fill=X, pady=5)
    Button(left_frame, text='Tambah Soal', bg='#57a1f8', fg='white', command=add_question).pack(fill=X, pady=5)
    Button(left_frame, text='Edit Soal', bg='#57a1f8', fg='white', command=edit_question).pack(fill=X, pady=5)
    Button(left_frame, text='Hapus Soal', bg='#57a1f8', fg='white', command=delete_question).pack(fill=X, pady=5)

    # Right Content Frame
    right_frame = Frame(admin, bg='white')
    right_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    Label(right_frame, text='Selamat Datang di Admin Dashboard', font=('Arial', 16, 'bold'), bg='white').pack(expand=True)

    admin.mainloop()