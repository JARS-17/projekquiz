from tkinter import *
from tkinter import messagebox
import ast
import os

# Membuat folder 'data' jika belum ada
if not os.path.exists('data'):
    os.makedirs('data')

# Window utama
window = Tk()
window.title("SignUp / SignIn")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# Fungsi untuk Sign Up
def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    # Validasi input
    if not username or not password or not confirm_password:
        messagebox.showerror('Signup', 'Semua kolom harus diisi!')
        return

    if len(password) < 6:
        messagebox.showerror('Signup', 'Password minimal 6 karakter!')
        return

    if password != confirm_password:
        messagebox.showerror('Signup', 'Password tidak cocok!')
        return

    try:
        # Membaca file data
        with open('data/datasheet.txt', 'r+') as file:
            data = file.read()
            users = ast.literal_eval(data) if data else {}

        # Cek username duplikat
        if username in users:
            messagebox.showerror('Signup', 'Username sudah ada!')
            return

        # Menambahkan user baru
        users[username] = password
        with open('data/datasheet.txt', 'w') as file:
            file.write(str(users))

        messagebox.showinfo('Signup', f'Akun "{username}" berhasil dibuat!')
        window.destroy()  # Tutup window Sign Up
        signin_window()   # Buka window Sign In

    except FileNotFoundError:
        # Jika file belum ada, buat file baru
        with open('data/datasheet.txt', 'w') as file:
            file.write(str({username: password}))
        messagebox.showinfo('Signup', f'Akun "{username}" berhasil dibuat!')
        window.destroy()
        signin_window()

# Fungsi untuk Sign In
def signin():
    username = user.get()
    password = code.get()

    try:
        # Membaca file data
        with open('data/datasheet.txt', 'r') as file:
            users = ast.literal_eval(file.read())

        # Validasi login
        if username in users and users[username] == password:
            messagebox.showinfo('Sign In', f'Login berhasil! Selamat datang, {username}!')
            window.destroy()
            open_quiz_window()
        else:
            messagebox.showerror('Sign In', 'Username atau password salah!')

    except FileNotFoundError:
        messagebox.showerror('Sign In', 'Belum ada akun yang terdaftar!')

# Fungsi untuk membuka window Sign In
def signin_window():
    window.destroy()
    signin = Tk()
    signin.title("Sign In")
    signin.geometry('925x500+300+200')
    signin.configure(bg='#fff')
    signin.resizable(False, False)

    frame = Frame(signin, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign In', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # Username
    Label(frame, text="Username", bg="white", font=("Microsoft Yahei UI Light", 11)).place(x=30, y=80)
    username_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    username_entry.place(x=30, y=110)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=137)

    # Password
    Label(frame, text="Password", bg="white", font=("Microsoft Yahei UI Light", 11)).place(x=30, y=150)
    password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show="*")
    password_entry.place(x=30, y=180)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=207)

    # Sign In Button
    Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0,
           command=lambda: signin_from_window(username_entry, password_entry, signin)).place(x=35, y=240)

    signin.mainloop()

# Fungsi untuk validasi Sign In dari window
def signin_from_window(username_entry, password_entry, signin_window):
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open('data/datasheet.txt', 'r') as file:
            users = ast.literal_eval(file.read())

        if username in users and users[username] == password:
            messagebox.showinfo('Sign In', f'Login berhasil! Selamat datang, {username}!')
            signin_window.destroy()
            open_quiz_window()
        else:
            messagebox.showerror('Sign In', 'Username atau password salah!')
    except FileNotFoundError:
        messagebox.showerror('Sign In', 'Belum ada akun yang terdaftar!')

# Fungsi untuk membuka window Quiz
def open_quiz_window():
    quiz_window = Tk()
    quiz_window.title("Quiz")
    quiz_window.geometry('925x500+300+200')
    quiz_window.configure(bg='#fff')
    quiz_window.resizable(False, False)

    Label(quiz_window, text="Selamat Datang di Kuis!", font=("Arial", 24, "bold"), bg="white", fg="#57a1f8").pack(pady=20)
    Label(quiz_window, text="Fitur kuis belum ditambahkan!", font=("Arial", 16), bg="white").pack(pady=10)

    quiz_window.mainloop()

# GUI Layout
img = PhotoImage(file='assets/login.png')  # Gambar harus ada di folder 'assets'
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username Entry
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show="*")
code.place(x=30, y=150)
code.insert(0, 'Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Confirm Password Entry
confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show="*")
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# Sign Up Button
Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)

# Sign In Label and Button
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signin_window)
signin.place(x=200, y=340)

# Main Loop
window.mainloop()
